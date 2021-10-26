import random
import numpy as np

def initialise(n,dirt):
    env=np.ones(n)
    for i in dirt:
        env[i-1]=0
    return env
def simulate(n,dirt,pos):
    env=initialise(n,dirt)
    measure=[]
    states=[]
    print("ENVIRONMENT:")
    print("START POSITION - "+str(pos)+"\tPERFORMANCE MEASURE - "+str(int(np.sum(env))))
    print("AGENT ACTIONS:")
    for i in range(0,1000):
        if(env[pos-1]==0):
            env[pos-1]=1
            clean=np.sum(env)
            measure.append(clean)
            print("START POSITION - "+str(pos)+"\tACTION TAKEN - SUCK\tPERFORMANCE MEASURE - "+str(int(clean)))
            states.append(pos)
        else:
            direction=random.randint(0,1)
            if (direction==0):
                if(pos>1):
                    pos-=1
                clean=np.sum(env)
                measure.append(clean)
                states.append(pos)
                print("START POSITION - "+str(pos)+"\tACTION TAKEN - LEFT\tPERFORMANCE MEASURE - "+str(int(measure[-1])))
            else :
                if(pos<n):
                    pos+=1
                clean=np.sum(env)
                measure.append(clean)
                states.append(pos)
                print("START POSITION - "+str(pos)+"\tACTION TAKEN - RIGHT\tPERFORMANCE MEASURE - "+str(int(measure[-1])))
    return measure,states    


def main():
    # Iterate through all possible combinations
    # No dirt start at 1:
    print("Simulation 1: No dirt, Start at 1: \n")
    dirt=[]
    performance,graph=simulate(2,dirt,1)
    state_space_graph=str(graph[0])
    for i in range(0,len(graph)-1):
        state_space_graph+= " -> "+str(graph[i]) 
    print(state_space_graph)

    print("Simulation 2: No dirt, Start at 2: \n")
    dirt=[]
    performance,graph=simulate(2,dirt,2)
    state_space_graph=str(graph[0])
    for i in range(0,len(graph)-1):
        state_space_graph+= " -> "+str(graph[i]) 
    print(state_space_graph)

    print("Simulation 3: Dirt at 1, Start at 2: \n")
    dirt=[1]
    performance,graph=simulate(2,dirt,2)
    state_space_graph=str(graph[0])
    for i in range(0,len(graph)-1):
        state_space_graph+= " -> "+str(graph[i]) 
    print(state_space_graph)

    print("Simulation 4: Dirt at 1, Start at 1: \n")
    dirt=[1]
    performance,graph=simulate(2,dirt,1)
    state_space_graph=str(graph[0])
    for i in range(0,len(graph)-1):
        state_space_graph+= " -> "+str(graph[i]) 
    print(state_space_graph)

    print("Simulation 5: Dirt at 1,2, Start at 1: \n")
    dirt=[1,2]
    performance,graph=simulate(2,dirt,1)
    state_space_graph=str(graph[0])
    for i in range(0,len(graph)-1):
        state_space_graph+= " -> "+str(graph[i]) 
    print(state_space_graph)

    print("Simulation 4: Dirt at 1,2, Start at 2: \n")
    dirt=[1,2]
    performance,graph=simulate(2,dirt,2)
    state_space_graph=str(graph[0])
    for i in range(0,len(graph)-1):
        state_space_graph+= " -> "+str(graph[i]) 
    print(state_space_graph)

if __name__ == '__main__':
    main()