import { traduzirMensagem } from "./traducaoService";

describe("traduzirMensagem", () => {
  it("traduz corretamente Olá mundo pt->en", async () => {
    const resultado = await traduzirMensagem({ texto: "Olá mundo", idiomaOrigem: "pt", idiomaDestino: "en" });
    expect(resultado).toBe("Hello world");
  });

  it("retorna texto traduzido genérico", async () => {
    const resultado = await traduzirMensagem({ texto: "Teste", idiomaOrigem: "pt", idiomaDestino: "en" });
    expect(resultado).toBe("Teste (traduzido)");
  });
});
