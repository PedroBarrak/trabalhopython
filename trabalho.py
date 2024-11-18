from validate_docbr import CPF
import re


nome = input("Digite seu nome: ")
cpf = input("Digite seu cpf: ")

#VALIDAÇÃO DE CPF
cpf_validacao = CPF ()

print("CPF VALIDADO!", cpf_validacao.validate(cpf) )


#VALIDAÇÃO DE EMAIL

def email_validacao(email):
    validado = re.fullmatch(r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$', email)
    if validado:
        return True
    return False

email = input("Digite seu e-mail: ")

if email_validacao(email):
    print("O e-mail é válido: VALIDO")
else:
    print("O e-mail é inválido: INVALIDO")

#VALIDAÇÃO TELEFONE

def telefone_validacao(telefone):
    validado = re.fullmatch(r"\(\d{2}\) \d{5}-\d{4}", telefone)
    if validado:
        return True
    return False

telefone = input("Digite seu Telefone: ")

print("TELEFONE: ", telefone_validacao(telefone))


def site_por_matricula(matricula):
    
    lista = [
        "Music Center",    # 0
        "Amazon",          # 1
        "Mercado Livre",   # 2
        "Magazine Luiza",  # 3
        "Casas Bahia",     # 4
        "Mundomax",        # 5
        "Carrefour",       # 6
        "Americanas",      # 7
        "Ponto Frio",      # 8
        "Extra"            # 9
    ]
    
    
    ultimo_digito = int(str(matricula)[-1])
    site = lista[ultimo_digito]
    print("O site correspondente ao último dígito da matrícula é: ", site)

    if ultimo_digito == 0:
        import Paginas.MusicCenter as music
        resultado = music.consultar_produto()
        print("Resultado da consulta em MusicCenter:", resultado)
    return site

matricula = input("Digite o número da matrícula: ")
site_por_matricula(matricula)


