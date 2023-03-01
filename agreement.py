class Color:
  purple = '\033[1;35;48m'
  cyan = '\033[1;36;48m'
  blue = '\033[1;34;48m'
  green = '\033[1;32;48m'
  yellow = '\033[1;33;48m'
  red = '\033[1;31;48m'

  bold = '\033[1;37;48m'
  underline = '\033[4;37;48m'

  end = '\033[1;37;0m'

text = f"""
This is a guide to the popularly established convention in python, to standardize the code and improve both understandability and readability.
{Color.red}IMPORTANT:{Color.end} It is neither mandatory nor necessary to follow these examples, each programmer chooses his own programming style.

{Color.underline}Types of syntax{Color.end}:
- {Color.cyan}lowerCamelCase{Color.end} -> {Color.red}example:{Color.end} helloWord

- {Color.green}UpperCamelCase{Color.end} -> {Color.red}example:{Color.end} HelloWord

- {Color.blue}snake_case{Color.end} -> {Color.red}example:{Color.end} hello_word

- {Color.purple}SCREAMING_SNAKE_CASE{Color.end} -> {Color.red}example:{Color.end} HELLO_WORD

{Color.underline}Types of syntax{Color.end}:
{Color.underline}Class{Color.end} -> {Color.green}UpperCamelCase{Color.end}

{Color.red}example:{Color.end}
  class MyClass():
      pass

{Color.underline}Exceptions{Color.end} -> {Color.green}UpperCamelCase{Color.end}

{Color.red}example:{Color.end}
  try:
      pass
  except SyntaxError:
      pass

{Color.underline}Functions{Color.end} and {Color.underline}variables{Color.end} -> {Color.blue}snake_case{Color.end}

{Color.red}example:{Color.end}
  code = 'Python'

  def my_functions():
      pass

{Color.underline}Constants{Color.end} -> {Color.purple}SCREAMING_SNAKE_CASE{Color.end}

{Color.red}example:{Color.end}
  CONST_NAME = 'Name'

{Color.underline}Non-public methods and variables{Color.end}

- Protected variables or functions -> dash prefix under {Color.purple}"_"{Color.end}

{Color.red}example:{Color.end}
  class MyClass: 
      {Color.purple}_{Color.end}name = "Name"

      def {Color.purple}_{Color.end}print(self):
        print(self.{Color.purple}_{Color.end}name)

- Private variables or functions -> double hyphen prefix under {Color.blue}"__"{Color.end}

{Color.red}example:{Color.end}
  class MyClass: 
      {Color.blue}__{Color.end}number = 4

{Color.underline}Arguments of functions and methods{Color.end}:

- 1st arg of functions -> {Color.green}self{Color.end}

{Color.red}example:{Color.end}
  class MyClass():
      def __init__({Color.green}self{Color.end}):
        {Color.green}self{Color.end}.name = "Hello"

      def my_func({Color.green}self{Color.end}):
          print({Color.green}self{Color.end}.name)

- 1st arg of methods -> {Color.cyan}cls{Color.end}

{Color.red}example:{Color.end}
  class MyClass():
      @classmethod
      def my_func({Color.cyan}cls{Color.end}):
          return

{Color.underline}Passing arguments{Color.end}:

- Non-Keyword Arguments -> *{Color.purple}args{Color.end}

{Color.red}example:{Color.end}
  def my_func(*{Color.purple}args{Color.end}):
      for arg in {Color.purple}args{Color.end}:
          print(arg)
  
  my_func('Hello', 'Word')

- Keyword Arguments -> **{Color.blue}kwargs{Color.end}

{Color.red}example:{Color.end}
  def my_func(**{Color.blue}kwargs{Color.end}):
      for key, value in {Color.blue}kwargs{Color.end}.items():
          print("%s == %s" % (key, value))
  
  my_func(first='1', mid='2', last='3')

 """

print(text)
