def calcular_idade(idade):
    """
    Verifica se a idade informada corresponde a uma pessoa maior de idade.

    Parâmetros:
        idade (int): A idade a ser verificada.

    Retorna:
        str: 'É maior de idade' se idade >= 18, caso contrário 'É menor de idade'.
    """
    if idade >= 18:
        return "É maior de idade"
    else:
        return "É menor de idade"


def avaliar_paridade(numero):
    """
    Verifica se o número informado é par.

    Parâmetros:
        numero (int): O número a ser avaliado.

    Retorna:
        bool: True se o número for par, False caso contrário.
    """
    return numero % 2 == 0


def dobrar(valor):
    """
    Retorna o dobro do valor informado.

    Parâmetros:
        valor (int ou float): O valor a ser dobrado.

    Retorna:
        int ou float: O valor multiplicado por 2.
    """
    return valor * 2
