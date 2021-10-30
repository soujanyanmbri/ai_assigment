
import numpy as np

def isGameOver(piles):
  if(np.sum(piles)!=0):
    return False
  return True

def gameState(piles):
  print("Game State: (" + str(piles[0]) + ", " +str(piles[1]) + ")")

def botPlay(piles,maxPlayer):
  if(((piles[0]==0 and piles[1]>0) or (piles[1]==0 and piles[0]>0)) and maxPlayer): 
    if(piles[0]>0):
      return 1,piles[0],0
    else:
      return 1,piles[1],1
  if(((piles[0]==0 and piles[1]>0) or (piles[1]==0 and piles[0]>0)) and  (not maxPlayer)): 
    if(piles[0]>0):
      return -1,piles[0],0
    else:
      return -1,piles[1],1
  if maxPlayer:
    res_max=-float('inf')
    for i in range(2):
      for removed in range(1,piles[i]+1):
        tem=piles.copy()
        maxp=not maxPlayer
        tem[i]-=removed
        ret,t1,t2=botPlay(tem,maxp)
        if ret > res_max :
          res_max=ret
          stone_remove=removed
          pile_remove=i
    return res_max,stone_remove,pile_remove  

  else:
    res_min= float('inf')
    for i in range(2):
      for removed in range(1,piles[i]+1):
        tem=piles.copy()
        maxp=not maxPlayer
        tem[i]-=removed
        ret,t1,t2=botPlay(tem,maxp)
        if (ret < res_min) :
          res_min=ret
          stone_remove=removed
          pile_remove=i
    return res_min,stone_remove,pile_remove

if __name__ == '__main__':
  p1=int(input("Enter the number of stones in pile 1: "))
  p2=int(input("Enter the number of stones in pile 2: "))
  piles=[p1,p2]
  while(not isGameOver(piles)):
    gameState(piles)
    pile=int(input("Enter the pile you want to remove from: "))
    stones=(int(input("Enter the number of stones you want to remove: ")))
    human_player=True
    piles[pile-1]-=stones
    gameState(piles);
    if not isGameOver(piles):
      t,agent_stones,agent_pile=botPlay(piles,False)
      piles[agent_pile]-=agent_stones
      print("Agent has removed "+str(agent_stones)+" stones from Pile "+str(agent_pile+1))
      human_player=False
  if(human_player):
    print("You Won!")
  else:
    print("You lost!")

