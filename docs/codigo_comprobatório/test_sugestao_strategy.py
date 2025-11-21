import unittest
from sugestao_strategy import (
    SugestaoPorIdioma, SugestaoPorInteresses, GerenciadorSugestoes
)

class TestSugestaoStrategy(unittest.TestCase):
    def test_sugestao_por_idioma(self):
        gerenciador = GerenciadorSugestoes(SugestaoPorIdioma())
        sugestoes = gerenciador.obter_sugestoes(1)
        self.assertEqual(sugestoes[0]["nome"], "João")

    def test_sugestao_por_interesses(self):
        gerenciador = GerenciadorSugestoes(SugestaoPorInteresses())
        sugestoes = gerenciador.obter_sugestoes(1)
        self.assertEqual(sugestoes[0]["nome"], "Maria")

    def test_troca_estrategia(self):
        gerenciador = GerenciadorSugestoes(SugestaoPorIdioma())
        gerenciador.definir_estrategia(SugestaoPorInteresses())
        sugestoes = gerenciador.obter_sugestoes(1)
        self.assertEqual(sugestoes[0]["nome"], "Maria")

if __name__ == "__main__":
    unittest.main()
