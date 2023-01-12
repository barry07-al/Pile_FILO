import unittest
from ThreeStack import ThreeStack, createThreeStackExample

class TestThreeStack(unittest.TestCase):

    def test_push(self):
        threeStack = ThreeStack()
        self.assertTrue(threeStack.getSize() == 0)
        self.assertTrue(threeStack.getSizeOfStack(1) == 0)
        self.assertTrue(threeStack.getSizeOfStack(2) == 0)
        self.assertTrue(threeStack.getSizeOfStack(3) == 0)
        threeStack.push(1, "{name:\"object1\"}")
        threeStack.push(1, "{name:\"object2\"}")
        self.assertTrue(threeStack.getSize() == 2)
        self.assertTrue(threeStack.getSizeOfStack(1) == 2)
        threeStack.push(2, "{name:\"object3\"}")
        threeStack.push(2, "{name:\"object4\"}")
        threeStack.push(2, "{name:\"object5\"}")
        self.assertTrue(threeStack.getSize() == 5)
        self.assertTrue(threeStack.getSizeOfStack(2) == 3)
        threeStack.push(3, "{name:\"object6\"}")
        threeStack.push(3, "{name:\"object7\"}")
        self.assertTrue(threeStack.getSize() == 7)
        self.assertTrue(threeStack.getSizeOfStack(3) == 2)

    def test_pop(self):
        threeStack = createThreeStackExample()
        self.assertTrue(threeStack.getSize() == 7)
        self.assertTrue(threeStack.getSizeOfStack(1) == 2)
        self.assertTrue(threeStack.getSizeOfStack(2) == 3)
        self.assertTrue(threeStack.getSizeOfStack(2) == 3)
        self.assertEqual(threeStack.pop(2), "{name:\"object5\"}")      
        self.assertTrue(threeStack.getSize() == 6)
        self.assertTrue(threeStack.getSizeOfStack(2) == 2)
        self.assertEqual(threeStack.pop(2), "{name:\"object4\"}")
        self.assertEqual(threeStack.pop(1), "{name:\"object2\"}")
        self.assertEqual(threeStack.pop(1), "{name:\"object1\"}")
        self.assertEqual(threeStack.pop(3), "{name:\"object7\"}")
        self.assertTrue(threeStack.getSize() == 2)
        self.assertTrue(threeStack.getSizeOfStack(1) == 0)
        self.assertTrue(threeStack.getSizeOfStack(2) == 1)
        self.assertTrue(threeStack.getSizeOfStack(3) == 1)
    
    def test_exception_push(self) :
        threeStack = createThreeStackExample()
        with self.assertRaises(Exception) as context:
            threeStack.pop(0)
        self.assertEqual(str(context.exception), 'Stack number must be between 1 and 3')

        with self.assertRaises(Exception) as context:
            threeStack.pop(6)
        self.assertEqual(str(context.exception), 'Stack number must be between 1 and 3')

    def test_exception_pop(self):
        threeStack = createThreeStackExample()
        threeStack.pop(2)
        threeStack.pop(2)
        threeStack.pop(1)
        threeStack.pop(1)
        threeStack.pop(3)

        with self.assertRaises(Exception) as context:
            threeStack.pop(1)
        self.assertEqual(str(context.exception), 'Stack is empty')

        with self.assertRaises(Exception) as context:
            threeStack.pop(4)
        self.assertEqual(str(context.exception), 'Stack number must be between 1 and 3')

       
if __name__ == '__main__':
    unittest.main()