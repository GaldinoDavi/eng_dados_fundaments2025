# Eng_Dados_Fundamentos 2025

Esse é um repositório básico. Ele recebe vários arquivos ".xlsx" e agrega em um único arquivo.

Ele faz parte uma série de estudos a serem seguidas para fortalecer alguns fundamentos de engenharia e ciência de dados.

Esse primeiro repositório a parte mais importante é o passo a passo de como estruturar um projeto de dados.

# Iniciando um Novo Projeto de Dados do Zero

Sempre foque em trabalhar com o terminal. Independente do sistema operacional, a linguaguem no terminal se mantém. E como as maioria dos programas são Linux, ao trabalhar com windows utilizar o bash para padronizar a linguagem.

## Ao iniciar um novo projeto de dados algumas etapas são fundamentais de serem seguidas:

Estruturação Básica do Projeto
	Primeiro verificar a versão global do python. "python --version"
	Setar a versão local do python "pyenv local (Versão)" 

	Criar o Ambiente Virtual: É possível criar o ambiente virtual via pyenv ou poetry.

	** Criando o ambiente virtual com Poetry**

	Criar o ambiente virtual
		Podemos criar o ambiente virtual com pyenv ou poetry
		
		poetry init
			Esse comando irá guiar de forma prática as principais informações para criar o ambiente virtual.
			preencher as informações
			
	
	Ativar o ambiente virtual
		source .venv/Scripts/activate
	
	Criar a branch
		Iniciar o Git "git init"
		criar o .gitignore para não subir os arquivos confidenciais
		Dica: https://www.toptal.com/developers/gitignore um compilado automático para o gitignore
		
## Estruturar o projeto em 4 pastas básicas
app
	Aqui onde fica o código do projeto

tests
	Pasta para testes unitários

docs
	**Algumas das bibliotecas para documentação e organização.**
	Mkdocs
	black
	blue
	isort
	docstring
	pydocstyle
	pip-audit
	taskpy

data
	Dados onde os arquivos ficam

	
Referência git	
https://blog.geekhunter.com.br/o-que-e-commit-e-como-usar-commits-semanticos/	

Guia seguido material da jornada de dados.
	
