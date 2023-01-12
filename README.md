# Structure de donnée Pile FILO

## Objectif

Ce mini-projet consiste à effectuer le test technique fournit par **Talosi**, qui consiste à implémenter une classe ThreeStack, qui implémente 3 piles FILO (First In, Last Out), avec comme seule structure de donnée, un tableau (liste ici) de chaine de caractères (string), à l'aide de la programmation orientée objet de python.

Pour cloner ce dépôt, éxecuter l'une des deux commandes ci-dessous :

En ssh,
```console
$ git clone git@github.com:barry07-al/Pile_FILO.git
```

En https,
```console
$ git clone https://github.com/barry07-al/Pile_FILO.git
```

## Organisation du dépôt

```console
.
├── Makefile
├── README.md
└── src
    ├── ThreeStack.py
    └── ThreeStackTest.py

1 directory, 4 files
```

## Ecplications et Exécution

La classe **ThreeStack** est implementée dans le fichier **src/ThreeStack.py**, avec les principales méthodes qui l'accompagne **push**, **pop**, **peek**, qui permettent respectivement d'empiler, de dépiler et d'afficher le sommet d'une pile dont le numéro est donné en paramètre.

**NB** : Le numéro de pile est compris entre 1 et 3 inclus.

Pour l'implémenter on a utilsé une liste python **arrayOfStacks** pour stocker les données des 3 piles, la première partie de liste représente la pile 1, la deuxième partie la pile 2, et la troisième partie la pile 3. Pour pouvoir gérer ces 3 piles dans la même liste **arrayOfStacks**, on a utilisé une autre liste **sizeOfStacks** qui permet de stocker les longueurs des 3 piles, cette liste nous permet principalement de retrouver le sommet des piles, pour pouvoir effectuer les opérations d'empilement et de dépilement.


Dans le fichier **src/ThreeStack.py**, on a défini une fonction **createThreeStackExample**, qui retourne un exemple de pile, que j'ai affiché dans le main de ce fichier **src/threeStack.py**.

Pour l'afficher, il suffit d'éxcuter la commande ci-dessous depuis la racine de ce dépôt,

```console
$ make
```

ou

```console
$ make run
```

Pour éxécuter les test fournis en exemple par l'entreprise **Talosi**, il faudra éxécuter la commande ci-dessous, depuis la racine de ce dépôt

```console
$ make runTests
```

**NB** : Dans le fichier de test **src/ThreeStackTest.py**, on teste le bon fonctionnement des fonctions **push** et **pop**.

## Complexités

- **push** : la fonction qui permet d'empiler un element dans une pile, en spécifiant le numéro de la pile dans laquelle on veut empiler l'élément, cette opération est effectuée une seule fois au sommet de la pile, à l'aide de la fonction **getTopIndex**, qui renvoi l'index du sommet de la pile, donc on a une complexité en O(1).

- **pop** : cette fonction, qui dépile a une complexité de O(1), car la fonction **del** est appelé une seule fois pour supprimer l'élément à l'indice renvoyé par la fonction **getTopIndex**.

## Autre façon de l'implémenter**

Une autre façon de l'implémenter est d'utiliser une liste de trois listes pour **arrayOfStacks**, chaque sous liste representera une pile, et on peux se passer de la liste **sizeOfStacks** pour connaitre la longueur de chaque pile, à la place on appellera la fonction **len** fournit par python pour les listes.

En ce qui concerne l'empilement et le dépilement des elements, on utilisera, respectivement, les focntions **append** et **pop** fournit par python.

Donc la nouvelle classe ThreeStack sera sera :

```python

class ThreeStack :

    def __init__(self) :
        """
        Initialize the data structure
        """
        self.arrayOfStacks = [[],[], []]

    def isEmpty(self, stackNum):
        """
        This function returns true if the stack is empty or not
        :param stackNum: (int) the stack number
        :return: (Boolean) which returns true if the stacknum is empty
        """
        return len(self.arrayOfStacks[stackNum-1]) == 0

    def push(self, stackNum, value) :
        """
        This function adds an element to the top of the stack stackNum
        :param stackNum: (int) the stack number
        :param value: (int) the element to add
        :return: (void) this function returns nothing
        """
        if not self.compare(stackNum) :
            raise Exception ("Stack number must be between 1 and 3")
        self.arrayOfStacks[stackNum-1].append(value)
    
    def pop(self, stackNum):
        """
        This function removes and returns the top element of the stack stackNum
        :param stackNum: (int) the stack number
        :return: (int) the top element of the stack
        """
        if self.isEmpty(stackNum):
            raise Exception ("Stack is empty")
        return self.arrayOfStacks[stackNum-1].pop()
    
    def peek(self, stackNum):
        """
        This function returns the top element of the stack stackNum
        :param stackNum: (int) the stack number
        :return: (int) the top element of the stack
        """
        if self.isEmpty(stackNum):
            raise Exception("Stack is empty.")
        return self.arrayOfStacks[stackNum-1][-1]

    def compare(self, stackNum) :
        """
        This function returns true if the stacknum is between 1 and 3 or false otherwise
        :param stackNum: (int) the stack number
        :return: (Boolean) which returns true if the stacknum is between 1 and 3 and false otherwise
        """
        return 1 <= stackNum <= 3
```