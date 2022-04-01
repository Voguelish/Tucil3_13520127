import random
import branchandbound as f
import numpy as np

NumberOfTC = int(input('Enter number of test cases: '))

for ntc in range(NumberOfTC):
  N = int(input('Steps: '))
  print('```')
  arr = ['1', '2', '3', '4', 
        '5', '6', '7', '8', 
        '9', '10', '11', '12', 
        '13', '14', '15', '-']
  arr = np.array(arr)
  simplice = arr.reshape(4, 4)

  directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
  prevMove = ''

  i = 0
  while i < N:
    random.shuffle(directions)
    if f.ValidMove(simplice, directions[0], prevMove):
      simplice = f.Move(simplice, directions[0])
      prevMove = directions[0]
      i += 1
      
  for i in range(len(simplice)):
    for j in range(len(simplice[i])):
      if j < 3:
        print(simplice[i][j], end=' ')
      else:
        print(simplice[i][j])
  print('```')