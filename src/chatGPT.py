class ThreeStack:

    def __init__(self) :
        self.arrayStacks = []
        self.sizesOfStacks = [0, 0, 0]

    def isEmpty(self, stackNum):
        match stackNum :
            case 1 :
                return self.sizesOfStacks[0] == 0
            case 2 :
                return self.sizesOfStacks[1] == 0
            case 3 :
                return self.sizesOfStacks[2] == 0
            case default :
                raise Exception ('this stack does not exist')
        
    def getTopIndex(self, stackNum):
        if self.arrayStacks != [] and stackNum == 1 :
            return 0
        elif self.arrayStacks != [] and stackNum == 2 or stackNum == 3:
            return sum(self.sizesOfStacks[:stackNum-1])
        else :
            raise Exception ('this stack does not exist or the array of stacks is empty')

    def push(self, stackNum, value) :
        if stackNum >= 1 and stackNum <= 3 :
            index = self.getTopIndex(stackNum) # On recupère l'index de debut de la pile numéro stackNUm
            self.arrayStacks.insert(index, value) # on insère la valeur value à l'index index (sommet de la pile stackNum)
            self.sizesOfStacks[stackNum] += 1 # Et on incrémente la taille de la pile satckNum de 1
        else :
            raise Exception ('this stack is wrong')
    
    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception ("Stack is empty.")
        elif stackNum >= 1 and stackNum <= 3 :
            index = self.getTopIndex(stackNum) - 1
            value = self.arrayStacks[index]
            del self.arrayStacks[index]
            self.sizesOfStacks[stackNum] -= 1
            return value
        else :
            raise Exception ('this stack is wrong')
    
    def printArrayStacks(self) :
        print(self.arrayStacks)

    """
    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise ValueError("Stack is empty.")
        index = self.getTopIndex(stackNum) - 1
        return self.arrayStacks[index]
    """

if __name__ == '__main__':
    threeStack = ThreeStack()

    threeStack.push(1, "{name:\"object1\"}")
    threeStack.printArrayStacks()
    threeStack.push(1, "{name:\"object2\"}")
    threeStack.printArrayStacks()
    threeStack.push(2, "{name:\"object2\"}")
    threeStack.push(2, "{name:\"object2\"}")
    threeStack.push(2, "{name:\"object2\"}")
    threeStack.printArrayStacks()
    threeStack.push(3, "{name:\"object2\"}")
    threeStack.push(3, "{name:\"object2\"}")
    threeStack.printArrayStacks()

    print(threeStack.pop(2)); # display {name:"object5"}
    print(threeStack.pop(2)); # display {name:"object4"}
    print(threeStack.pop(1)); # display {name:"object2"}
    print(threeStack.pop(1)); # display {name:"object1"}
    print(threeStack.pop(3)); # display {name:"object7"}
    print(threeStack.pop(1)); # throw Exception
    print(threeStack.pop(4)); # throw Exception