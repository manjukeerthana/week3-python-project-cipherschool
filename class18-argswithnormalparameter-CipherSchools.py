def multiply_nums(*args):
          mul=1
          for i in args:
                    mul*=i
          return mul
print(multiply_nums(6,33))



def manjukeerthana(*manju):
          multiply=1
          for i in manju:
                    multiply*=i
          return multiply
print(manjukeerthana(43,24,22,43,45,33,43))


def func(num1,num2,*args):
          add=1
          print(num1)
          print(num2)
          for i in args:
                    add*=i
          return add
print(func(24,23))























