# Di�rio de bordo - Desenvolvimento
=====================
# 14/03/2016 - 19:00 - 00:18
	Boa noite, hoje comecei o desenvolvimento pela cria��o do projeto, optei utilizar o 
Python com o Framework Django pois � pra mim um ambiente mais familiar, decidi al�m de configurar o b�sico 
iniciar pelos templates contendo a maioria da parte visual da aplica��o, fiz um commit inicial no gitHub, 
implementei um prototipo, para testar, foi quando lendo novamente os requisitos percebi a necessidade de 
dividir ainda mais os modelos, para poder obter os dados necess�rios para gerar informa��es na aplica��o, 

Por enquanto estou utilizando o SQLite pelo fato de n�o haver necessidade de nada al�m de um banco para
armazenamento dos dados, por�m poss�velmente utilizarei o postgresSQL, optei em utilizar o GloboCom Bootstrap
que est� dispon�vel no gitHub(http://globocom.github.io/bootstrap/) para auxiliar na cria��o do template,
utilizei tamb�m a biblioteca JQuery, por enquanto s� adicionei estas por n�o haver necessidades at� ent�o de 
uma outra, estou analisando se utilizarei a chart.js(http://www.chartjs.org/) para fazer o grafico do resultado.

Finalizei alguns ajustes nos modelos para se adequar nas regras de neg�cio, logo em seguida fiz algumas altera��es
na View VoteView, agora os dados que s�o necess�rios para gerar relat�rios para informar a quantidade de votos totais,
por hor�rio e por participante, por hoje � s�, mas amanh� retornaremos com o desenvolvimento da P�gina de resultado ap�s o voto,
onde implementarei o chart.js junto com o que vai resultar da requisi��o POST, logo ap�s, vou implementar relat�rios para a equipe
de produ��o saber detalhadamente sobre os votos, ap�s isso iniciarei os testes mais robustos e ajustes finos no layout.



	