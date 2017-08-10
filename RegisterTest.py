import unittest

class clazzA(unittest.TestCase):
    def __init__(self):
        unittest.TestCase.__init__(self)
        pass

    def testa(self):
        self.estb()

    def estb(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(clazzA)
    unittest.TextTestRunner(verbosity=2).run(suite)
