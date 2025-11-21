from abc import ABC, abstractmethod
from typing import List

class EstrategiaSugestao(ABC):
    @abstractmethod
    def sugerir_amigos(self, usuario_id: int) -> List[dict]:
        pass

class SugestaoPorIdioma(EstrategiaSugestao):
    def sugerir_amigos(self, usuario_id: int) -> List[dict]:
        # Busca usuários que querem aprender o idioma nativo do usuário
        return [{"id": 101, "nome": "João", "idioma": "inglês"}]

class SugestaoPorInteresses(EstrategiaSugestao):
    def sugerir_amigos(self, usuario_id: int) -> List[dict]:
        # Busca usuários com tags/interesses similares
        return [{"id": 102, "nome": "Maria", "interesse": "música"}]

class GerenciadorSugestoes:
    def __init__(self, estrategia: EstrategiaSugestao):
        self._estrategia = estrategia
    
    def definir_estrategia(self, estrategia: EstrategiaSugestao):
        self._estrategia = estrategia
    
    def obter_sugestoes(self, usuario_id: int) -> List[dict]:
        return self._estrategia.sugerir_amigos(usuario_id)

# Testes básicos
if __name__ == "__main__":
    idioma = SugestaoPorIdioma()
    interesses = SugestaoPorInteresses()
    gerenciador = GerenciadorSugestoes(idioma)
    print("Sugestão por idioma:", gerenciador.obter_sugestoes(1))
    gerenciador.definir_estrategia(interesses)
    print("Sugestão por interesses:", gerenciador.obter_sugestoes(1))
