import unittest
from singleton import ConfiguracaoSistema

class TestConfiguracaoSistema(unittest.TestCase):
    def test_singleton_instance(self):
        a = ConfiguracaoSistema()
        b = ConfiguracaoSistema()
        self.assertIs(a, b)

    def test_obter_config(self):
        config = ConfiguracaoSistema()
        self.assertEqual(config.obter_config("max_tentativas_login"), 3)
        self.assertIn("pt", config.obter_config("idiomas_suportados"))

if __name__ == "__main__":
    unittest.main()
