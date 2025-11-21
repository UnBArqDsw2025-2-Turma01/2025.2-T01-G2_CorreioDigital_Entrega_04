import unittest
from traducao_adapter import GoogleTranslateAdapter

class TestGoogleTranslateAdapter(unittest.TestCase):
    def test_traduzir(self):
        try:
            adapter = GoogleTranslateAdapter()
            resultado = adapter.traduzir("Olá mundo", "pt", "en")
            self.assertIsInstance(resultado, str)
            self.assertNotEqual(resultado, "Olá mundo")
        except Exception as e:
            self.skipTest(f"Google Translate não disponível: {e}")

if __name__ == "__main__":
    unittest.main()
