import string
import random

def randomLetter():
  first = random.choice(string.ascii_letters)
  second = random.choice(string.ascii_letters)
  third = random.choice(string.ascii_letters)
  fourth = random.choice(string.ascii_letters)
  y = first + second + third + fourth
  return y

def randomInt():
  first = random.randint(1,9)
  second = random.randint(1,9)
  third = random.randint(1,9)
  fourth = random.randint(1,9)
  z = str(first) + str(second) + str(third) + str(fourth)
  return z
  
def randomPassword():
  print("You random password is", randomLetter() + randomInt())

randomPassword()
