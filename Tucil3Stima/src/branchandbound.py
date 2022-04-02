# 13520127 Adzka Ahmadetya Zaidan
import numpy as np

# Mengembalikan nilai dari Kurang(i)
def Kurang(flatM, i):
  idx = np.where(flatM == i)[0][0]
  count = 0
  for j in range(idx+1, 16):
    if (int(flatM[j]) > int(flatM[idx])):
      count += 1
  return count

# Mengembalikan nilai SigmaKurangi dari M
def SigmaKurang(M):
  flatM = M.flatten()
  emptyIdx = np.where(flatM == '-')
  flatM[emptyIdx] = '16'
  arrOfKurangi = [Kurang(flatM, i) for i in flatM]
  return sum(arrOfKurangi)

# Mengembalikan array of row, col dari nilai '-' simpul M
def IdxofEmpty(M):
  emptyIndexes = np.where(M == '-')
  return [emptyIndexes[0][0], emptyIndexes[1][0]]

# Mengembalikan X
def X(M):
  X = sum(IdxofEmpty(M)) % 2
  return X

# Mengembalikan boolean apakah simpul M reachable atau tidak
def Reachable(M):
  return (SigmaKurang(M) + X(M)) % 2 == 0

# Mengembalikan suatu simpul hasil dari simpul sebelumnya yang sudah digerakkan
def Move(M, direction):
  coords = IdxofEmpty(M)
  tempM = []
  for i in range(len(M)):
    cols = []
    for j in range(len(M[0])):
      cols.append(M[i][j])
    tempM.append(cols)
  if direction == 'UP':
    tempM[coords[0]][coords[1]] = tempM[coords[0]-1][coords[1]]
    tempM[coords[0]-1][coords[1]] = '-'
  elif direction == 'RIGHT':
    tempM[coords[0]][coords[1]] = tempM[coords[0]][coords[1]+1]
    tempM[coords[0]][coords[1]+1] = '-' 
  elif direction == 'DOWN':
    tempM[coords[0]][coords[1]] = tempM[coords[0]+1][coords[1]]
    tempM[coords[0]+1][coords[1]] = '-'
  elif direction == 'LEFT':
    tempM[coords[0]][coords[1]] = tempM[coords[0]][coords[1]-1]
    tempM[coords[0]][coords[1]-1] = '-'
  return np.array([tempM[0], tempM[1], tempM[2], tempM[3]])

# Mengembalikan estimasi g dari simpul M
def EstimationG(M):
  count = 0
  flatM = M.flatten()
  idx = IdxofEmpty(M)[0]*4 + IdxofEmpty(M)[1]
  flatM[idx] = '16'
  for i in range(16):
    if int(flatM[i]) != i+1:
      if i != idx:
        count += 1
  return count

# Mengembalikan estimasi cost dari simpul M
def Cost(M, steps):
  return steps + EstimationG(M)

# Mengembalikan boolean apakah suatu direction adalah valid untuk simpul M atau tidak
def ValidMove(M, direction, prevMove):
  coords = IdxofEmpty(M)
  if (direction == 'UP'):
    return prevMove != 'DOWN' and coords[0] != 0
  elif (direction == 'RIGHT'):
    return prevMove != 'LEFT' and coords[1] != 3
  elif (direction == 'DOWN'):
    return prevMove != 'UP' and coords[0] != 3
  elif (direction == 'LEFT'):
    return prevMove != 'RIGHT' and coords[1] != 0

# Melakukan checking apakah M merupakan goalstate atau bukan
def IsGoalState(M):
  tempM = M.flatten()
  for i in range(15):
    if tempM[i] == '-':
      return False
    if int(tempM[i]) != i+1:
      return False
  return True

# Mengembalikan Simplice yang terbentuk dengan sequence of directions dari startS
def SimpliceFromPath(startS, path):
  # path = array of direction
  tempM = []
  for i in range(len(startS)):
    cols = []
    for j in range(len(startS[0])):
      cols.append(startS[i][j])
    tempM.append(cols)
  tempM = np.array([tempM[0], tempM[1], tempM[2], tempM[3]])
  for i in range(len(path)):
    tempM = Move(tempM, path[i])
  return np.array([tempM[0], tempM[1], tempM[2], tempM[3]])

# Display sequence simpul hingga menuju simpul startS
def DisplaySimplices(startS, path):
  tempM = []
  for i in range(len(startS)):
    cols = []
    for j in range(len(startS[0])):
      cols.append(startS[i][j])
    tempM.append(cols)
  tempM = np.array([tempM[0], tempM[1], tempM[2], tempM[3]])
  PrintSimplice(tempM) # PRINTING MATRIX
  for i in range(len(path)):
    tempM = Move(tempM, path[i])
    print(path[i])
    PrintSimplice(np.array([tempM[0], tempM[1], tempM[2], tempM[3]]))

# Print suatu simpul M
def PrintSimplice(M):
  print('━━━━━━━━━━━━━━━')
  for i in range(4):
    for j in range(4):
      if j == 0:
        print('| ', end='')
      if (len(M[i][j]) == 2):
        print(M[i][j]+' ',end='')
      else:
        print(M[i][j]+'  ',end='')
      if j == 3:
        print('|')
  print('━━━━━━━━━━━━━━━')