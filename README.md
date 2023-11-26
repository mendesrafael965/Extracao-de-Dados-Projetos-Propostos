# Extracão de Dados dos Projetos Propostos por Vereadores de São Paulo
<a href="https://mendesrafael965.github.io/Extracao-de-Dados-Projetos-Propostos/"> Link para página do projeto</a>
<h2>Introdução</h2>
<p align="justify">
  Observatório Social do Brasil em São Paulo (OSB-SP) é uma associação civil sem fins lucrativos, dedicada à promoção da transparência, educação fiscal e cidadania ativa. E dentre as atividades realizadas por essa instituição está o monitoramento dos projetos propostos      pelos vereadores de São Paulo.
  Atualmente essa tarefa e realizada pelos vonlutários que acessam a pagina da <a href="https://splegisconsulta.saopaulo.sp.leg.br/">Câmara Municipal de São Paulo</a>, coletam as informações uma a uma e em seguinda inserem essas informações em planilhas.
</p> 

<p align="justify">
  O presente projeto tem como objetivo realizar a extração e transformações dos dados dos projetos propostos pelos vereadores da Câmara Municipal de São Paulo e também gerar planilhas com estes dados. Isso com intuito de reduzir o tempo de execução bem como a chance de      erro na realização desta tarefa.
</p>

<h2>Arquitetura</h2>
<p align="justify">
  A imagem a seguir apresenta a arquitetura utilizada no projeto.
</p>

<img src="assets/imgs/Diagrama ETL.png"/>

<p align="justify">
  Os dados são extraídos da API do SPLEGIS em seguida são realizadas algumas transformações nos dados e por fim estes dados são armazenados em planilhas.
</p>

<p align="justify">
Para o projeto em questão foram utilizados os seguintes endpoints:
<ul>
  <li><a href="https://splegisws.saopaulo.sp.leg.br/ws/ws2.asmx?op=ProjetosPorAno">Projetos Por Ano</a> que retorna todos os projetos de um determinado ano. Caso a informação de ano não seja fornecida, será considerado o ano corrente.</li>
  <li><a href="https://splegisws.saopaulo.sp.leg.br/ws/ws2.asmx?op=ProjetosAutoresJSON">Projetos Autores</a> que retorna os projetos de um determinado ano com a informação de seus autores e subscritores, se houver. Caso a informação de ano não seja fornecida, será           considerado o ano corrente.</li>
</ul>
  A lista completa com todos os endpoints disponível pode ser acessada <a href="https://splegisws.saopaulo.sp.leg.br/ws/ws2.asmx">aqui</a>.
</p>
