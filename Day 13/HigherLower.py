import random

from game_data import data

game = True
score  = 0

while game:

  account1 = ''
  account2 = ''
  
  account1 = random.choice(data)
  account2 = random.choice(data)
  while account1 == account2:
    account2 = random.choice(data)
  
  print(
  f"Compare A: {account1['name']},a {account1['description']},from{account1['country']}"
  )
  
  print(
  f"Compare B: {account2['name']},a {account2['description']},from{account2['country']}"
  )
  
  answer = input('Who has more followers? Type "A" or "B":')
  
  isCorrect =False
  if answer == 'A':
    isCorrect = account1['follower_count'] > account2['follower_count']
  elif answer == 'B':
    isCorrect = account1['follower_count'] < account2['follower_count']
  
  if isCorrect:
    print('You are right')
    score+=1
  else:
    print('You are wrong')
    game = False

print(f'Your score is {score}')

