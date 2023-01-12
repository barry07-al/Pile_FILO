class ThreeStack:

    def __init__(self) :
        """
        Initialize the data structure here
        """
        self.arrayOfStacks = []
        self.sizesOfStacks = [0, 0, 0]


    def getArrayStacks(self) :
        """
        :return: the array of stacks
        """
        return self.arrayOfStacks


    def getSizesOfStacks(self) :
        """
        :return: the array of stacks
        """
        return self.sizesOfStacks


    def getSize(self):
        """
        This function returns the number of elements in the array of stacks
        :return: (int) the number of elements in the array of stacks
        """
        return len(self.arrayOfStacks)


    def getSizeOfStack(self, stackNum):
        """
        This function returns the size of the stack stackNum
        :param stackNum: (int) the stack number
        :return: (int) the size of the stack
        """
        if self.compare(stackNum) :
            return self.getSizesOfStacks()[stackNum-1]
        raise Exception ('Stack number must be between 1 and 3')


    def isEmpty(self, stackNum):
        """
        This function returns true if the stack is empty or not
        :param stackNum: (int) the stack number
        :return: (Boolean) which returns true if the stacknum is empty
        """
        if self.compare(stackNum) :
            return self.getSizesOfStacks()[stackNum-1] == 0
        raise Exception ('Stack number must be between 1 and 3')
    

    def push(self, stackNum, value) :
        """
        This function adds an element to the top of the stack stackNum
        :param stackNum: (int) the stack number
        :param value: (int) the element to add
        :return: (void) this function returns nothing
        """
        if self.compare(stackNum) :
            index = self.getTopIndex(stackNum) # On recupère l'index du sommet de la pile numéro stackNUm
            self.arrayOfStacks.insert(index, value) # on insère la valeur value à l'index index (sommet de la pile stackNum)
            self.getSizesOfStacks()[stackNum-1] += 1 # Et on incrémente la taille de la pile satckNum de 1
        else :
            raise Exception ('Stack number must be between 1 and 3')


    def pop(self, stackNum):
        """
        This function removes and returns the top element of the stack stackNum
        :param stackNum: (int) the stack number
        :return: (int) the top element of the stack
        """
        if self.isEmpty(stackNum) :
            raise Exception ("Stack is empty")
        elif not self.compare(stackNum) :
            raise Exception ('Stack number must be between 1 and 3')
        index = self.getTopIndex(stackNum)
        value = self.arrayOfStacks[index] # on recupère la valeur du sommet de la pile avant le dépilement (suppression)
        del self.arrayOfStacks[index] # on dépile
        self.getSizesOfStacks()[stackNum-1] -= 1
        return value


    def peek(self, stackNum):
        """
        This function returns the top element of the stack stackNum
        :param stackNum: (int) the stack number
        :return: (int) the top element of the stack
        """
        if self.isEmpty(stackNum):
            raise Exception ("Stack is empty.")
        return self.arrayOfStacks[self.getTopIndex(stackNum)-1]


    def getTopIndex(self, stackNum):
        """
        This functon returns the index of the top element of the stack stackNum
        :param stackNum: (int) the stack number
        :return: (int) the index of the top element
        """
        if self.compare(stackNum) :
            return sum(self.getSizesOfStacks()[:stackNum-1])
        raise Exception ('Stack number must be between 1 and 3')


    def compare(self, stackNum) :
        """
        This function returns true if the stacknum is between 1 and 3 or false otherwise
        :param stackNum: (int) the stack number
        :return: (Boolean) which returns true if the stacknum is between 1 and 3 and false otherwise
        """
        return 0 < stackNum <= 3


    def printStack(self, stackNum):
        """
        This function prints the stack number stackNum
        """
        if not self.compare(stackNum):
            raise Exception ("Stack number must be between 1 and 3")
        indexBeginning = sum(self.sizesOfStacks[:stackNum-1])
        stack = self.arrayOfStacks[indexBeginning:indexBeginning+self.sizesOfStacks[stackNum-1]]
        print(f"Stack {stackNum}: {stack}")


def createThreeStackExample () :
    """
    This function creates an example of a three stack
    :return: (ThreeStack) this function returns a three stack
    """
    threeStack = ThreeStack()
    threeStack.push(1, "{name:\"object1\"}")
    threeStack.push(1, "{name:\"object2\"}")
    threeStack.push(2, "{name:\"object3\"}")
    threeStack.push(2, "{name:\"object4\"}")
    threeStack.push(2, "{name:\"object5\"}")
    threeStack.push(3, "{name:\"object6\"}")
    threeStack.push(3, "{name:\"object7\"}")
    return threeStack


if __name__ == "__main__":
    threeStack = createThreeStackExample()
    print("Array of Stacks : " + str(threeStack.getArrayStacks()))
    print("Size of Stacks : " + str(threeStack.getSizesOfStacks()))
    threeStack.printStack(1)
    threeStack.printStack(2)
    threeStack.printStack(3)