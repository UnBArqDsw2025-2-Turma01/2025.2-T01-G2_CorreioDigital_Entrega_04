export interface TraducaoRequest {
  texto: string;
  idiomaOrigem: string;
  idiomaDestino: string;
}

export const traduzirMensagem = async (dados: TraducaoRequest): Promise<string> => {
  // Simulação de chamada à API
  // Em ambiente real, use fetch('/api/traduzir', ...)
  if (dados.texto === "Olá mundo" && dados.idiomaOrigem === "pt" && dados.idiomaDestino === "en") {
    return "Hello world";
  }
  return dados.texto + " (traduzido)";
};

// Teste básico
(async () => {
  const resultado = await traduzirMensagem({ texto: "Olá mundo", idiomaOrigem: "pt", idiomaDestino: "en" });
  console.log("Tradução simulada:", resultado);
})();
