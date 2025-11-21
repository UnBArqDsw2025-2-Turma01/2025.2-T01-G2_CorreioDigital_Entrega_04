from abc import ABC, abstractmethod

# Interface comum para serviços de tradução
class ServicoTraducao(ABC):
    @abstractmethod
    def traduzir(self, texto: str, idioma_origem: str, idioma_destino: str) -> str:
        pass

# Adaptador para Google Translate
class GoogleTranslateAdapter(ServicoTraducao):
    def __init__(self):
        from googletrans import Translator
        self.tradutor = Translator()
    
    def traduzir(self, texto: str, idioma_origem: str, idioma_destino: str) -> str:
        resultado = self.tradutor.translate(texto, src=idioma_origem, dest=idioma_destino)
        return resultado.text

# Adaptador para DeepL
class DeepLAdapter(ServicoTraducao):
    def __init__(self, api_key: str):
        import deepl
        self.tradutor = deepl.Translator(api_key)
    
    def traduzir(self, texto: str, idioma_origem: str, idioma_destino: str) -> str:
        resultado = self.tradutor.translate_text(texto, source_lang=idioma_origem.upper(), 
                                                   target_lang=idioma_destino.upper())
        return resultado.text

# Testes básicos
if __name__ == "__main__":
    # Teste GoogleTranslateAdapter
    try:
        google_adapter = GoogleTranslateAdapter()
        print("Google Translate PT->EN:", google_adapter.traduzir("Olá mundo", "pt", "en"))
    except Exception as e:
        print("Google Translate não disponível:", e)
    # Teste DeepLAdapter (requer API key)
    # deepL_adapter = DeepLAdapter("YOUR_DEEPL_API_KEY")
    # print("DeepL PT->EN:", deepL_adapter.traduzir("Olá mundo", "pt", "en"))
