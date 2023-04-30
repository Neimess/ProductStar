import typing as t
from flask import Flask, jsonify, request, json
from model.twit import Twit
from model.comments import Comment
from model.user import User
twits = []
users = []
comments = []
app = Flask(__name__)
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'id': obj.id,"body": obj.body, "author": obj.author, 'user_id': obj.user_id}
        if isinstance(obj, User):
            return {'id': obj.id, "user_name": obj.username}
        if isinstance(obj, Comment):
            return {'id': obj.id, 'body': obj.body, "twit_id": obj.twit_id}
        return super().default(obj)
app.json_encoder = CustomJSONEncoder


@app.route('/ping',methods = ['GET'])
def ping():
    return jsonify({'status':'pong'})

@app.route('/user/<int:user_id>/twit', methods = ['GET'])
def read_user_twit(user_id):
    twit = next((u for u in twits if twit.get_user_id() == user_id), None)
    if twit:
        return jsonify(twit)
    return jsonify({"error": "User not found"}), 404


@app.route('/twits', methods = ['GET'])
def read_twits():
    return jsonify({'twits': twits})

@app.route('/user/<int:id_user>/twit', methods = ['POST'])
def create_twit(id_user):
    twit_json = request.get_json()
    twit = Twit(body=twit_json['body'], author=twit_json['author'], 
                user_id=id_user, id=twit_json['id'])
    twits.append(twit)
    return jsonify({'status': 'success'})

@app.route ("/twit/<int:id_twit>/comments", methods=["POST"])
def create_comment(id_twit):
    comment_json = request.get_json()
    comment = Comment(body=comment_json['body'],
                      twit_id = id_twit, 
                      id=comment_json['id'])
                    
    comments.append(comment)
    return jsonify({'status': 'success'})

@app.route ("/twit/<int:id_twit>/comments/", methods=["GET"])
def read_comment(id_twit):
    comment = next((u for u in comments if u.get_twit_id() == id_twit), None)
    if comment:
        return jsonify(comment)
    return jsonify({"error": "User not found"}), 404



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
    user = next((u for u in users if u.get_id() == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)