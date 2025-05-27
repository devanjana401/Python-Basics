def decorator_function(func):
      def message():
          print("HELLO WORLD")
      return message
@decorator_function
def hello():
    print("HELLO WORLD")
hello()