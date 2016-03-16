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
	uma outra, estou analisando se utilizarei a charts.js(http://www.chartjs.org/) para fazer o grafico do resultado.

	Finalizei alguns ajustes nos modelos para se adequar nas regras de negócio, logo em seguida fiz algumas alterações
	na View VoteView, agora os dados que são necessários para gerar relatórios para informar a quantidade de votos totais,
	por horário e por participante, por hoje é só, mas amanhã retornaremos com o desenvolvimento da Página de resultado após 	o voto,
	onde implementarei o chart.js junto com o que vai resultar da requisição POST, logo após, vou implementar relatórios para 	a equipe
	de produção saber detalhadamente sobre os votos, após isso iniciarei os testes mais robustos e ajustes finos no layout.
=====================
# 14/03/2016 - 09:00 -  (Next Day)01:02
	Bom dia, hoje iniciei criando uma página do resultado da votação, resultando o objeto do participante,
	iniciei a implementação do charts.js para fazer o gráfico de resultado de votação, e fiz alguns ajustes no repositório
	adicionado um gitIgnore para remover os arquivos de configurações da IDE, também o arquivo do SQLite, após isso, irei desenvolver
	toda a página de resultado, com o gráfico e o countdown da votação, logo após irei fazer alguns gráficos para a produção do programa.
	Já estou me preocupando sobre o teste de performance, porém quero fazer todo o Core necessário para me preocupar com a performance,
	lógico que tudo está sendo desenvolvido pensando sobre a performance, optei por deixar o captcha e alguns ajustes finos dos layouts
	mais pra frente, quando estiver mais avançado no escopo do projeto, implementei o charts.js de forma basica sem utilizar os dados, 
	da votação real para implementar ajustes no FrontEnd, comecarei a desenvolver a respeito dos dados do chart dinâmicamente com o backEnd.
	Quero iniciar ainda hoje a implementação do Captcha, fazer os reports para a produção com a quantidade de votos totais, por participante e 
	quebrando por hora, estou pensando em implementar uma tarefa assíncrona com o celery para ajustar os relatorios a cada x(ainda não definido) minutos 
	pra facilitar a performance da consulta dos dados finais, dependendo de como tudo caminhará implementarei, irei implementar a conexão com o MySQL ou PostgreSQL,
	ainda não decidi, mas acredito que vá utilizar o PostgreSQL, estou empolgado para finalizar o desenvolvimento para poder iniciar os testes de performance, para
	verificar como está, estou pensando se tiver problemas futuros com isso, implementar os métodos com ThreadPools ou utilizando coroutines Asyncio, ainda não sei.
	Estou um pouco preocupado com a automação de Deploy, estou planejando/estudando utilizar o Fabric(http://www.fabfile.org/), até agora não encherguei alguma restrição
	mas só quando implementar de fato, saberei.
	
	Estive pensando, e com dúvidas se deveria ser dynamico a criação dos participantes, mas como foi enviada apenas duas sprite e o layout seguido, tomei em consideração
	que seria apenas estes participantes, porém enviarei um e-mail para confirmar, corretamente.
	Iniciei o desenvolvimento da parte de visualização da equipe de produção, criarei um link com controle de acesso, com login e senha,  para verificar alguns reports,
	conforme solicitado nos requisitos, bom agora foi criado um formulário de autenticação, com algumas validações, criando uma sessão para quem deseja verificar os relatórios de votos,
	estou implementando o Django Messages Framewok, para responder as mensagens de erros na autenticação do form.



	
