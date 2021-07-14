from functools import cache

@cache
def coordinateToMatrixPosition(x:int,y:int) -> tuple:
  linha,coluna = 0,0
  if y == 1:
      linha,coluna = y,x
  else:
    if x == 0:
      coluna = 0
      linha = - (y -2 )
    if x == 1:
      coluna = 1
      linha = 0 if y == 2 else 2
    if x == 2:
      coluna = 2
      linha = -(y-2)
  return (linha,coluna)

if __name__ == '__main__':
  while True:
    x,y = map(int, input("Digite as coordenadas: ").split(" "))
    if x == -1:
      break
    print(coordinateToMatrixPosition(x,y))
