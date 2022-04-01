import numpy as np
import branchandbound as f
import time as t
import os

cwd = os.path.dirname(os.getcwd())
os.chdir(cwd+'\\test')

while True:
  filename = str(input('Enter file name:\n>>> '))
  if (len(filename) < 4):
    filename += '.txt'
  elif (filename[len(filename)-1] != 't' or filename[len(filename)-2] != 'x' or filename[len(filename)-3] != 't' or filename[len(filename)-4] != '.'):
    filename += '.txt'
  simplice = np.loadtxt(filename, dtype='str', delimiter=' ')

  # Inisialisasi
  startS = simplice
  path = [[]]
  costs = [f.EstimationG(startS)+len(path[0])]
  directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
  
  print()
  # BRANCH AND BOUND
  if not f.Reachable(startS): # Jika puzzle unsolvable
    f.DisplaySimplices(startS, path[0])
    print('Puzzle is unsolvable.')
    print('SigmaKurang(i) + X = '+str(f.SigmaKurang(startS) + f.X(startS))+'\n')
  else: # Jika simpul awal memiliki suatu solusi
    start = t.time()
    idx = 0
    # Melakukan loop jika belum ditemukan solusi
    # Jika jumlah simpul yang dibangkitkan sudah terlalu banyak, pencarian berhenti
    while not f.IsGoalState(f.SimpliceFromPath(startS, path[idx])) and len(path) < 100000:
      currS = f.SimpliceFromPath(startS, path[idx])
      if len(path[idx]) != 0:
        prevMove = path[idx][len(path[idx])-1]
      else:
        prevMove = ''
      # Melakukan branching dari suatu simpul hidup
      for dir in directions:
        if f.ValidMove(currS, dir, prevMove):
          path.append([])
          for i in range(len(path[idx])):
            path[len(path)-1].append(path[idx][i])
          path[len(path)-1].append(dir)
          costs.append(f.Cost(f.Move(currS, dir), len(path[idx])+1))
      costs[idx] = 999 # Berikan nilai cost yang sangat tinggi agar tidak lagi di-expand
      idx = costs.index(min(costs)) # Memilih cost terrendah untuk di-expand
    
    # Jika ditemukan suatu solusi
    if f.IsGoalState(f.SimpliceFromPath(startS, path[idx])):
      end = t.time()
      timeTaken = round((end-start), 4)
      print('━━━━━━━ Solution Found !!! ━━━━━━━')
      f.DisplaySimplices(startS, path[idx])
      print('Solution Sequence'+' ('+str(len(path[idx]))+'): ', end='')
      for i in range(len(path[idx])):
        print(path[idx][i], end=' ')
      print('\nTime taken:', str(timeTaken), 'seconds')
      print('Simplices created:', len(path), '\n')
      
    else: # Jumlah simpul yang dibangkitkan sudah terlalu banyak
      print('Too many simplices created. Stopped searching.')
      print('Simplices created:', len(path), '\n')
  
  flag = True
  while flag:
    exit = str(input('Continue program? (Y/N)\n>>> '))
    if (exit == 'Y' or exit == 'y'):
      flag = False
    elif (exit == 'N' or exit == 'n'):
      break
    else:
      print('Invalid input.')
  if (exit == 'N' or exit == 'n'):
    break
print('\nProgram successfully closed.\n')