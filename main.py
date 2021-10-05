#WRITE YOUR CODE IN THIS FILE
#define function 
def hasL(w): 
    w == w.lower()
    for i in range(0, len(w)):
        if (w[i]) == "l":
            return True
    else:
        return False 
hasL("dog") 