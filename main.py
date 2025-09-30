
from passwordmeter import test
from urllib.request import urlopen
from os.path import isfile
from random import choice, randint

if not isfile('words.txt'):
  print('Downloading words.txt ...')
  url='https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
  words=urlopen(url).read().decode('utf-8')
  with open('words.txt','w',encoding='utf-8') as f:
    f.write(words)

words=open('words.txt','r').read().split("\n")
special_chars=['!','?','#','%','$','=','@','^','&','(',')','<','>']

def create_password(num_words=2,num_numbers=6,num_special=6):
  pass_str=''

  for _ in range(num_words):
    pass_str+=choice(words).lower().capitalize()
  for _ in range(num_numbers):
    pass_str+=str(randint(0,9))
  for _ in range(num_special):
    pass_str+=choice(special_chars)
  return pass_str
    

def main():
  pass_str=create_password()
  strength,suggestion=test(pass_str)

  pass_google='ZXVbk,ZA=7!^g6s'
  str_g,suggestion_g=test(pass_google)

  print('\nOWN')
  print('\nPassword: ', pass_str)
  print('Strength: %.5f' %strength)
  print('Suggestions: ', suggestion)

  print('\nGoogle')
  print('\nPassword: ', pass_google)
  print('Strength: %.5f' %str_g)
  print('Suggestions: ', suggestion_g)



if __name__=='__main__':
  main()