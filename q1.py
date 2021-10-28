import random
class env: 
    def __init__ (self, e):
        self.loc = e
    def  __str__ (self):
        return "The environment is : [A:%s, B:%s]" % (("Dirty" if self.loc[0] == 1 else "Clean"),("Dirty" if self.loc[1] == 1 else "Clean"))
class bot:
    def __init__ (self, pos, environment):
        self.pos = pos
        self.score = 0
        self.environment = env(environment)
    def suck(self):
        print(self.pos," is clean now.")
        self.environment.loc[self.pos] = 0
        self.score += 1
   
    def run(self):
        print(self.environment)
        print("Start Position: ", self.pos)
        moves = 0
        state = []
        while moves < 1000:
            if self.environment.loc[self.pos]:
                self.environment.loc[self.pos] = 0
                self.score +=1
                state.append(self.pos)
            else:
                new = random.randint(0, 1)
                #print(("Moved %s" % ("Left" if new==0 else "Right")), end = '')
                #if self.pos== new:
                #    print(". But bot was already here.")
                #else:
                #    print()
                self.pos = new
                state.append(self.pos)
            moves += 1
        print("Performance Score: ", self.score)
        print("State space search graph: ")
        state_space_search_graph=str(state[0])
        for i in range(0,len(state)-1):
            state_space_search_graph+= " -> "+str(state[i]) 
        print(state_space_search_graph)
if __name__ == '__main__':
    for startPos in range(2):
        for A in range(2):
            for B in range(2):
                Bot = bot(startPos, [A, B])
                Bot.run()
                print()

