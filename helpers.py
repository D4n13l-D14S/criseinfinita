from time import sleep
def printWSleep():
    for i in range(9):
        sleep(0.25)
        print('=', end= " ", flush= True)
    print('=')
  
def separador():
    print('||✝'*30)

def separador10s():
  for i in range(9):
    sleep(0.1)
    print('.', end= " ", flush= True)
  sleep(0.1)
  print('.')