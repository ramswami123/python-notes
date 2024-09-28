def decorator(func , x ,y):
    def add():
      print(x+y,":first execution")
      
    def sub():
      print(x-y,":last execution")
    
    def wrapper():
        add()
        func()
        sub()
    return wrapper

def say_hello():
    print("in say hello func")

say_hello = decorator(say_hello,8,8)

say_hello()
