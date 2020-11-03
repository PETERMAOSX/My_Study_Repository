from threading import Thread

class MyThread(Thread):
    def __init__(self,id):
        super(MyThread,self).__init__()
        self.id = id
    def run(self):
        print("task",self.id)

if __name__ == "__main__":
    t1 = MyThread("t1")
    t2 = MyThread("t2")

    t1.start()
    t2.start()