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

- Protected variables or functions -> dash prefix under {Color.bold}"_"{Color.end}

{Color.red}example:{Color.end}
  class MyClass: 
      _name = "Name"

      def _print(self):
        print(self._name)

- Private variables or functions -> double hyphen prefix under {Color.bold}"__"{Color.end}

{Color.red}example:{Color.end}
  class MyClass: 
      __number = 4

{Color.underline}Arguments of functions and methods{Color.end}

- 1st arg -> self

- 1st arg -> cls
"""

print(text)
