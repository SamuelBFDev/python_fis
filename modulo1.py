#Funções de indicadores de saúde de uma pessoa

def imc(peso,altura):
    '''Calcula o IMC - Índice de Massa Corporal
    Parâmetros:
    peso - valor em quilos
    altura - valor em metros

    Resultado:
    imc - número real
    '''

    return (peso/altura**2)

def idosa(idade):
    '''Indica pessoa legalmente idosa
    Parâmetros:
    idade - valor em anos
    Resultado
    pessoaidosa - Booleano (True/False)
    '''
    legalmenteidosa=60
    return idade>=legalmenteidosa
    
def relatorio(nome, peso, altura, idade):
    '''Gera um relatório com dados
    da pessoa, para serem colocados
    num relatório sobre sua saúde
    Entrada:
    nome= nome da pessoa
    peso= peso em kg
    altura= altura em metros
    idade= idade numérica em anos
    
    Saída:
    faz o print de um texto que contém o IMC
    e o registro se a pessoa já é legalmente idosa

    Retorna: None
    '''
    imc_pessoa=imc(peso,altura)
    eh_idosa= idosa(idade)
   
    stridosa="é legalmente idosa"
    if not eh_idosa:
        stridosa="não "+stridosa
        
    print("{} {} e seu imc é {}".format(nome, stridosa, imc_pessoa))
    return   
       
imc_faixa=(18.5,25.0,30.0)
'''Tupla que indica os limites das faixas de IMC:
x<18.5 subpeso
18.5<=x<25.0 normal
25<=x<30 sobrepeso
x>30 obesidade
'''
