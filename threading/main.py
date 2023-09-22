import threading
import time

class Library:
    """Создаем класс, который работает с запросами
    на поиск книги, что одновременно можно обслуживать только 
    1 посетителя, ибо библиотекарь всего один
    """
    def __init__(self):
        #Value не передается ибо поумолчанию value = 1
        self.visitors_count = threading.Semaphore()
    
    def meet_visitor(self, visitor):
        print(f"\nПриглашаем посетителя {visitor}")
        self.visitors_count.acquire()
        print(f"\n Спрашиваем у посетителя {visitor} какую книгу он хочет")
        print("\nУсиленно ищем")
        time.sleep(3)
        print("\nНАШЛИ")
        self.visitors_count.release()
    
    def visitors(self, count):
        
        for visitor in range(1, count+1):
            
            visitor_thread = threading.Thread(  target=   self.meet_visitor,
                                              args= [visitor]).start()
        
if __name__ == "__main__":
    Visitors = Library()
        
    Visitors.visitors(4)