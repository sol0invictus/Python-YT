import unittest
 
def square(x):
    return x*x
    

class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        self.number = 4
  
    def test_strings_a(self):
        self.assertEqual( square(self.number), 16)
  
    def test_upper(self):        
        self.assertEqual(square(3),8 )
  

if __name__ == '__main__':
    unittest.main()
