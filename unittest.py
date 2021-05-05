import unittest
 
def square(x):
    return x*x
    

class TestSquare(unittest.TestCase):
      
    def setUp(self):
        self.number = 4
  
    def test1(self):
        self.assertEqual( square(self.number), 16)
  
    def test2(self):        
        self.assertEqual(square(3),8 )
  

if __name__ == '__main__':
    unittest.main()
