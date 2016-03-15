# Diário de bordo - Desenvolvimento
=====================
# 14/03/2016 - 19:00 - 00:18
	Boa noite, hoje comecei o desenvolvimento pela criação do projeto, optei utilizar o 
Python com o Framework Django pois é pra mim um ambiente mais familiar, decidi além de configurar o básico 
iniciar pelos templates contendo a maioria da parte visual da aplicação, fiz um commit inicial no gitHub, 
implementei um prototipo, para testar, foi quando lendo novamente os requisitos percebi a necessidade de 
dividir ainda mais os modelos, para poder obter os dados necessários para gerar informações na aplicação, 

Por enquanto estou utilizando o SQLite pelo fato de não haver necessidade de nada além de um banco para
armazenamento dos dados, porém possívelmente utilizarei o postgresSQL, optei em utilizar o GloboCom Bootstrap
que está disponível no gitHub(http://globocom.github.io/bootstrap/) para auxiliar na criação do template,
utilizei também a biblioteca JQuery, por enquanto só adicionei estas por não haver necessidades até então de 
uma outra, estou analisando se utilizarei a chart.js(http://www.chartjs.org/) para fazer o grafico do resultado.

Finalizei alguns ajustes nos modelos para se adequar nas regras de negócio, logo em seguida fiz algumas alterações
na View VoteView, agora os dados que são necessários para gerar relatórios para informar a quantidade de votos totais,
por horário e por participante, por hoje é só, mas amanhã retornaremos com o desenvolvimento da Página de resultado após o voto,
onde implementarei o chart.js junto com o que vai resultar da requisição POST, logo após, vou implementar relatórios para a equipe
de produção saber detalhadamente sobre os votos, após isso iniciarei os testes mais robustos e ajustes finos no layout.



	