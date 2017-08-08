import unittest

class clazzA(unittest.TestCase):
    def testa(self):
       pass

    def testb(self):
    	pass

    def testa1(self):
    	pass

    def testac(self):
    	pass

    def test9(self):
    	pass

    def test0(self):
    	pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(clazzA)
    unittest.TextTestRunner(verbosity=2).run(suite)
