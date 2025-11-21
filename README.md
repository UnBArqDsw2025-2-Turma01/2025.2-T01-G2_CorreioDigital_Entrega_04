# RepositorioTemplate

Repositório que deve ser utilizado como template inicial pelos grupos da matéria de Arquitetura e Desenho de Software.

## Introdução

Este repositório traz um template de repo de documentação a ser seguido pelos grupos de arquitetura e desenho de software.

## Tecnologia

A geração do site estático é realizada utilizando o [docsify](https://docsify.js.org/).

```shell
"Docsify generates your documentation website on the fly. Unlike GitBook, it does not generate static html files. Instead, it smartly loads and parses your Markdown files and displays them as a website. To start using it, all you need to do is create an index.html and deploy it on GitHub Pages."
```

### Instalando o docsify

Execute o comando:

```shell
npm i docsify-cli -g
```

### Executando localmente

Para iniciar o site localmente, utilize o comando:

```shell
docsify serve ./docs
```

## Códigos Comprobatórios dos Padrões de Projeto

Os exemplos de código dos padrões GoF utilizados no projeto estão na pasta `codigo_comprobatório`.

### Estrutura

- `traducao_adapter.py`: Adapter para serviços de tradução (Google Translate, DeepL)
- `singleton.py`: Singleton para configuração do sistema
- `sugestao_strategy.py`: Strategy para sugestão de amigos
- `traducaoService.ts`: Adapter frontend (simulação Next.js/React)

### Como executar os exemplos Python

1. Instale as dependências necessárias:
	```bash
	pip install googletrans==4.0.0-rc1 deepl
	```
2. Execute cada arquivo diretamente para ver exemplos de uso:
	```bash
	python codigo_comprobatório/traducao_adapter.py
	python codigo_comprobatório/singleton.py
	python codigo_comprobatório/sugestao_strategy.py
	```
3. Para rodar os testes automáticos:
	```bash
	python -m unittest codigo_comprobatório/test_singleton.py
	python -m unittest codigo_comprobatório/test_sugestao_strategy.py
	python -m unittest codigo_comprobatório/test_traducao_adapter.py
	```

### Como executar o exemplo TypeScript

1. Instale Node.js e um framework de testes (ex: Jest):
	```bash
	npm install jest ts-jest @types/jest --save-dev
	```
2. Execute o teste:
	```bash
	npx jest codigo_comprobatório/test_traducaoService.ts
	```

### Observações
- O exemplo DeepL requer uma chave de API válida para funcionar.
- Os testes Python e TypeScript são independentes e podem ser executados separadamente.
- Os exemplos são didáticos e podem ser adaptados para uso real no sistema.
