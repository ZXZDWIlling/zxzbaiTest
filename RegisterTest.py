import unittest

class clazzA:
    def testa(self):
        estb()

    def estb(self):
        pass

c = clazzA()
c.estb()
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(clazzA)
#     unittest.TextTestRunner(verbosity=2).run(suite)
