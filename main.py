from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import randint, sample
from secrets import choice
from string import punctuation
from zxcvbn import zxcvbn
from pprint import pprint
import argparse

# Download the list of words from github if not already in the folder
if not isfile('words.txt'):
  print('Downloading words.txt ...')
  url='https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
  words=urlopen(url).read().decode('utf-8')
  with open('words.txt','w',encoding='utf-8') as f:
    f.write(words)

# Open the file and init the list of words and special chars
# To use for passwords
words=open('words.txt','r').read().split("\n")
special_chars=punctuation


# Method used for generating the password
def create_password(num_words=2,num_numbers=4,num_special=3):
  pass_str=''

  # choose a number of words from the word list
  for _ in range(num_words):
    pass_str+=choice(words).lower().capitalize()
  pass_str=''.join(choice((str.upper,str.lower))(c) for c in pass_str)
  # choose digits to add to the password
  for _ in range(num_numbers):
    pass_str+=str(randint(0,9))
  # choose a number of special chars to add to the password
  for _ in range(num_special):
    pass_str+=choice(special_chars)
  pass_str=''.join(sample(pass_str,len(pass_str)))
  return pass_str

def positive_int(value):
  ivalue=int(value)
  if ivalue < 0:
    raise argparse.ArgumentTypeError(f"{value} must be a positive integer")
  return ivalue

def get_args():
  parser=argparse.ArgumentParser(
    description="A simple tool for generating a strong password",
    epilog="example usage: python main.py -w 3 -d 6 -s 4"
  )
  parser.add_argument('-w','--words',type=positive_int,default=2,help='The number of words used for generating the password(default 2)')
  parser.add_argument('-d','--digits',type=positive_int,default=4,help='The number of digits used for generating the password(default 4)')
  parser.add_argument('-s','--specials',type=positive_int,default=3,help='The number of special characters used for generating the password(default 3)')
  parser.add_argument('-q','--quiet',action='store_true',default=False,help='Disables the strength analyzer part of the tool and only shows the generated password')

  return parser.parse_args()


# Analyzes the given password in terms of strength
# and in terms of how easy it it to brute force it
def analyze_password(password):
  strength,suggestion=test(password)
  z_res=zxcvbn(password)

  print('Passwordmeter score: %.5f' %strength)
  print('Passwordsmeter suggesions: ', suggestion)
  print('Zxcvbn strength:')
  pprint(z_res)


def main():
  
  args=get_args()
  pass_str=create_password(args.words,args.digits,args.specials)

  pass_google='ZXVbk,ZA=7!^g6s'
  
  if(not args.quiet):
    analyze_password(pass_str)
    analyze_password(pass_google)
  else:
    print(pass_str)



if __name__=='__main__':
  main()