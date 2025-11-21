import threading

class ConfiguracaoSistema:
    _instancia = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
                    cls._instancia._inicializar()
        return cls._instancia
    
    def _inicializar(self):
        self.configs = {
            "max_tentativas_login": 3,
            "tempo_expiracao_token": 3600,
            "tamanho_maximo_mensagem": 5000,
            "idiomas_suportados": ["pt", "en", "es", "fr", "de"]
        }
    
    def obter_config(self, chave: str):
        return self.configs.get(chave)

# Teste básico
if __name__ == "__main__":
    config = ConfiguracaoSistema()
    print("Max tentativas login:", config.obter_config("max_tentativas_login"))
    print("Idiomas suportados:", config.obter_config("idiomas_suportados"))
