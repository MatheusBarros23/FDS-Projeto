import unittest

from models import Jogo

class TestSalvarDao(unittest.TestCase):

    def setUp(self):

        self.jogo1 = Jogo('CSGO', 'FPS', 'PC')
        self.jogo2 = Jogo('GTA', 'ARCADE', 'PC')

    def test_input_jogo(self):
        jogo = Jogo('CSGO', 'FPS', 'PC')
        self.assertEqual(jogo.nome, 'CSGO')


if __name__ == '__main__':

    unittest.main()
