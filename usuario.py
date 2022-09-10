class Usuario():
    def __init__(self, nome, rg, matricula, endereco, senha):
        self.__nome = nome
        self.__rg = rg
        self.__matricula = matricula
        self.__endereco= endereco
        self.__senha = senha
        
    def GetNome(self):
        return self.__nome
    
    def GetRg(self):
        return self.__rg
    
    def GetMatricula(self):
        return self.__matricula
    
    def GetEndereco(self):
        return self.__endereco
    
    def GetSenha(self):
        return self.__senha
    
    def SetNome(self, nome):
        self.__nome = nome
    
    def SetRg(self, rg):
        self.__rg = rg
    
    def SetMatricula(self, matricula):
        self.__matricula = matricula
    
    def SetEndereco(self, endereco):
        self.__endereco = endereco
    
    def SetSenha(self, senha):
        self.__senha = senha
    
        