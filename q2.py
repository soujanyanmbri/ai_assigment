
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
  turn = int(input("Enter 1 for BotVsBot and 2 for HumanVsBot: "))
  p1=int(input("Enter the number of stones in pile 1: "))
  p2=int(input("Enter the number of stones in pile 2: "))
  piles=[p1,p2]
  if(turn == 1):
    while( not isGameOver(piles)):
      gameState(piles)
      t,agent1_stones,agent1_pile=botPlay(piles,False)
      piles[agent1_pile]-=agent1_stones
      player1 = True
      print("Agent 1 has removed "+str(agent1_stones)+" stones from Pile "+str(agent1_pile+1))
      if not isGameOver(piles):
        gameState(piles)
        t,agent1_stones,agent1_pile=botPlay(piles,True)
        piles[agent1_pile]-=agent1_stones
        print("Agent 2 has removed "+str(agent1_stones)+" stones from Pile "+str(agent1_pile+1))
        player1 = False
    if(player1):
      gameState(piles)
      print("Player 1 Won!")
    else:
      gameState(piles)
      print("Player 2 Won!")
  else:
    turnH = int(input("Enter 1 if you want to start first, 2 otherwise: "))
    if(turnH == 1):
      while(not isGameOver(piles)):
        gameState(piles)
        pile=int(input("Enter the pile you want to remove from: "))
        stones=(int(input("Enter the number of stones you want to remove: ")))
        human_player=True
        piles[pile-1]-=stones
        gameState(piles)
        if not isGameOver(piles):
          t,agent_stones,agent_pile=botPlay(piles,False)
          piles[agent_pile]-=agent_stones
          print("Agent has removed "+str(agent_stones)+" stones from Pile "+str(agent_pile+1))
          human_player=False
      if(human_player):
        gameState(piles)
        print("You Won!")
      else:
        gameState(piles)
        print("You lost!")  
    else:
      while(not isGameOver(piles)):
        gameState(piles)
        t,agent_stones,agent_pile=botPlay(piles,False)
        piles[agent_pile]-=agent_stones
        print("Agent has removed "+str(agent_stones)+" stones from Pile "+str(agent_pile+1))
        human_player=False
        if not isGameOver(piles):
          gameState(piles)
          pile=int(input("Enter the pile you want to remove from: "))
          stones=(int(input("Enter the number of stones you want to remove: ")))
          human_player=True
          piles[pile-1]-=stones
      if(human_player):
        gameState(piles)
        print("You Won!")
      else:
        gameState(piles)
        print("You lost!")  

