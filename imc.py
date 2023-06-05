# Função que calcula o índice de massa corporal de uma pessoa
def imc(peso, altura):
    '''
    Calcula o IMC − Índice de Massa Corporal
    5 Parâmetros:
    peso − real em quilos
    altura − real em metros
    Resultado:
    imc - número real
    '''
    return (peso / altura ** 2)
