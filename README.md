# WebServiceNoFramework
⚙️ Implementação de um Web Service Cliente e Servidor sem uso de framework

## A aplicação
Implementação de uma pequena aplicação distribuída, aqui serão detalhados algumas informações importantes em relação a essa aplicação e a forma com que deve se executá la. Nela existem dois projetos, o projeto do servidor e o projeto do Cliente.

## Dependencias
O Cliente foi feito em java, utilizando os imports: `java.io.OutputStream`, `java.netHtppURLConnection`, `java.net.MalformedURLException`, `java.net.URL`, e um
servidor feito em Python utilizando os imports: `http.server`, `socketserver` e `json`.

Caso não tenha instalado em seu computador algum desses imports, eles são nativos do
java. Para essa implementação de Cliente e Servidor não foi necessário fazer
download de nenhuma dependência. Tanto o Cliente quanto o servidor foram
desenvolvidos sem o auxílio de frameworks ou microframeworks. A versão do java
utilizada foi a `1.8.0_301`, com o `java SE 17`, e a versão do Python
utilizada foi o `python 3.8.8`.

## Execução

Para executar o servidor basta clicar no arquivo servidor.py que ele será
iniciado por padrão no localhost na porta 8000, provavelmente em outra máquina
será necessário configurar o ip no lado do cliente, para que as duas máquinas
possam conversar.

A pasta desse projeto também contém uma pasta chamada Cliente, em que
dentro dela contém o projeto feito em Java a partir da IDE Eclipse, toda a aplicação
foi desenvolvida no Sistema Operacional Windows 10. Neste projeto existem dois
arquivos .java, o primeiro é o Cliente.java, onde foram implementadas todas as
funções no que diz respeito às chamadas GET, PUT, POST e DELETE que foram
realizadas à API servidor. O segundo arquivo .java desta pasta Cliente é chamado
de ClienteAPP.java, é nele que será executado o cliente, contendo neste arquivo um
Menu que mostra as opções que o usuário pode executar, por exemplo remover um
usuário, adicionar usuário, listar usuários.
