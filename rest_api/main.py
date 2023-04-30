import typing as t
from flask import Flask, jsonify, request, json
from model.twit import Twit
from model.comments import comments
from model.user import User
twits = []
users = []
app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'id': obj.id,"body": obj.body, "author": obj.author}
        if isinstance(obj, User):
            return {'id': obj.id, "user_name": obj.username}
        if isinstance(obj, comments):
            return {'id': obj.id, 'body': obj.body, "twit_id": obj.username}
        return super().default(obj)
    

app.json_encoder = CustomJSONEncoder


@app.route('/ping',methods = ['GET'])
def ping():
    return jsonify({'status':'pong'})


@app.route('/twit', methods = ['GET'])
def read_twit():
    return jsonify({'twits': twits})

@app.route('/twit', methods = ['POST'])
def create_twit():
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'], twit_json['user_id'])
    twits.append(twit)
    return jsonify({'status': 'success'})

@app.route ("/twit/<int:twit_id>/comments", methods=["POST"])
def create_comment(twit_id):
    comment_json = request.get_json()
    comment = comments(comment_json['body'], id=comment_json['id'], id_twit=twit_id)
    comments.append(comment)
    return jsonify(comments)

@app.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    comment = next((comment for comment in comments if comment["id"] == comment_id), None)
    if comment:
        comments.remove(comment)
        return jsonify({"message": "Comment deleted"})
    else:
        return jsonify({"error": "Comment not found"}), 404
    
    
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify('users', users)
    
    
@app.route("/users", methods=["POST"])
def create_user():
    username_json = request.get_json()
    new_user = User(username=username_json['username'], id=username_json['id'])
    users.append(new_user)
    return jsonify({"success": "user added"})

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if (user.get_id() == user_id):
            break
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)