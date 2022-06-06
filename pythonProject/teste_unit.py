import unittest
from models import Jogo, Usuario


class TestSalvarDao(unittest.TestCase):

    def setUp(self):

        self.jogo1 = Jogo('CSGO', 'FPS', 'PC')
        self.jogo2 = Jogo('GTA', 'ARCADE', 'PC')
        self.user1 = Usuario('ADE', 'Dzr', 'sportcampeao87')
        self.user2 = Usuario('3705', 'Kryno', 'lolmaster')

        self.user1 = Usuario('1987', 'Dzr', 'sportcampeao87')
        self.user2 = Usuario('arroz', 'Kryno', 'PEChamp2022')


    def test_input_jogo(self):

        self.assertEqual(self.jogo1.nome, 'CSGO')
        self.assertEqual(self.jogo1.categoria, 'FPS')
        self.assertEqual(self.jogo1.console, 'PC')

        self.assertEqual(self.jogo2.nome, 'GTA')
        self.assertEqual(self.jogo2.categoria, 'ARCADE')
        self.assertEqual(self.jogo2.console, 'PC')

    def test_input_usuario(self):

        self.assertEqual(self.user1.id, '1987')
        self.assertEqual(self.user1.nome, 'Dzr')
        self.assertEqual(self.user1.senha, 'sportcampeao87')

        self.assertEqual(self.user2.id, 'arroz')
        self.assertEqual(self.user2.nome, 'Kryno')
        self.assertEqual(self.user2.senha, 'PEChamp2022')


if __name__ == 'main':
    unittest.main()
    