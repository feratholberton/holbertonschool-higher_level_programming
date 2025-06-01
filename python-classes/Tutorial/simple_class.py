class MyClass:
  """Doc String for testing"""
  i = 12345

  def f(self):
    return 'hello world!'
  

test_1 = MyClass()
print(test_1.__doc__)
print(test_1.f())
# print(test_1)
# test_2 = MyClass()
# print(test_2)