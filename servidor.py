import http.server
import socketserver
import json

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        print('content_length:', content_length)
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None
        
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        dicionario = self.PegaUrl()
        
        if self.Pesquisa(dicionario['rg']) == None:    
            self.BancoDeDados(dicionario)
            usuario = json.dumps(dicionario)
            self.wfile.write(usuario.encode('utf-8'))
        else:
            resposta = 'Usuario ja existente!'
            self.wfile.write(resposta.encode('utf-8'))
        
        
    def PegaUrl(self):
        dicionario = {}
        novalista = []
        
        url = self.path[2:]
        url = url.split('&')
        for i in url:
            i = i.split('=')
            novalista.append(i)
        for i in novalista:
            dicionario[i[0]] = i[1]
            
        return dicionario
            
        
    def BancoDeDados(self,dicionario_pessoa):
        dicionario_pessoa['nome'] = dicionario_pessoa['nome'].replace("+"," ")
        dicionario_pessoa['endereco'] = dicionario_pessoa['endereco'].replace("+"," ")
        dicionario_pessoa['senha'] = dicionario_pessoa['senha'].replace("+"," ")
        with open('persistencia.json','a') as f:
            dicionario = json.dumps(dicionario_pessoa)
            f.write(dicionario+'\n')
            
        
    def Pesquisa(self,rg):
        repositorio = open('persistencia.json', 'r')
        for i in repositorio:
            linha = json.loads(i)
            if(linha['rg'] == rg):
                return linha
            
            
    def PesquisaSenha(self,rg,senha):
        encontrado = False
        repositorio = open('persistencia.json', 'r')
        for i in repositorio:
            linha = json.loads(i)
            if linha['rg'] == rg:
                encontrado = True
                if linha['senha'] == senha:
                    return 'Senha Correta'
                else:
                    return 'Senha Incorreta'
        if encontrado == False:
            return 'Usuario nao encontrado!'
        
            
    def PesquisaRemove(self,rg):
        lista = []
        encontrado = True
        repositorio = open('persistencia.json', 'r')
        
        if(self.Pesquisa(rg) == None):
            encontrado = False
        
        for i in repositorio:
            linha = json.loads(i)
            if(linha['rg'] != rg):
                lista.append(linha)
        repositorio.close()
        
        if encontrado == False:
            resposta = 'Usuario nao encontrado!'
        else:
            resposta = 'Usuario de rg {} removido com sucesso!'.format(rg)
            
        with open('persistencia.json', 'w') as f:
            pass
        repositorio = open('persistencia.json','a')
        for i in lista:
            repositorio.write(json.dumps(i)+'\n')
        return resposta
            
    def TrocarSenha(self,rg,senha):
        nova_lista = []
        encontrado = False
        repositorio = open('persistencia.json', 'r')
        for i in repositorio:
            linha = json.loads(i)
            if(linha['rg'] == rg):
                encontrado = True
                linha['senha'] = senha
                resposta = 'Senha alterada!'
            nova_lista.append(linha)
        if encontrado == False:
            resposta = 'Usuario nao encontrado!'
        with open('persistencia.json','w') as f:
            pass
        repositorio = open('persistencia.json','a')
        for i in nova_lista:
            repositorio.write(json.dumps(i)+'\n')
        return resposta
    
    
    def AlterarDados(self,rg,nome,rgnovo,matricula,endereco):
        encontrado = False
        dados_novos = []
        repositorio = open('persistencia.json', 'r')
        for i in repositorio:
            linha = json.loads(i)
            if(linha['rg'] == rg):
                encontrado = True
                if self.Pesquisa(rgnovo) == None:
                    linha['nome'] = nome
                    linha['rg'] = rgnovo
                    linha['matricula'] = matricula
                    linha['endereco'] = endereco
                    resposta = 'Dados alterados com sucesso!'
                else:
                    resposta = 'Esse rg ja existe!'
            dados_novos.append(linha)
        if encontrado == False:
            resposta = 'Usuario nao encontrado!'
        with open('persistencia.json','w') as f:
            pass
        repositorio = open('persistencia.json','a')
        for i in dados_novos:
            i['nome'] = i['nome'].replace("+"," ")
            i['endereco'] = i['endereco'].replace("+"," ")
            repositorio.write(json.dumps(i)+'\n')
        return resposta
    
                    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        url = self.path[2:]
        if(url == ''):
            lista_todos = self.RetornaTodos()
            for i in lista_todos:
                self.wfile.write(i.encode('utf-8'))
                
        elif(len(self.PegaUrl()) == 2):
             url = self.PegaUrl()
             resposta = self.PesquisaSenha(url['rg'], url['senha'])
             self.wfile.write(resposta.encode('utf-8'))
             
        else:
            url = self.PegaUrl()
            rg  = url['rg']
            user = self.Pesquisa(rg)
            if(user == None):
                retorno = 'Usuario nao encontrado!'
            else:
                retorno = json.dumps(user)
            self.wfile.write(retorno.encode('utf-8'))
    
        
    def do_PUT(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        dados = self.PegaUrl()
        if(len(dados) == 2):
            resposta = self.TrocarSenha(dados['rg'], dados['senha'])
            self.wfile.write(resposta.encode('utf-8'))
        else:
            print(dados)
            resposta = self.AlterarDados(dados['rg1'],dados['nome'],dados['rg'],dados['matricula'],dados['endereco'])
            self.wfile.write(resposta.encode('utf-8'))
    
    def do_DELETE(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        url = self.PegaUrl()
        retorno = self.PesquisaRemove(url['rg'])
        self.wfile.write(retorno.encode('utf-8'))
        
        
    def RetornaTodos(self):
        listaTodos = []
        with open('persistencia.json','r') as f:
            for i in f:
                listaTodos.append(i)
        return listaTodos
        
Handler = MyHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Iniciando conexão em http://localhost:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Stopping by Ctrl+C")
    httpd.server_close() 
