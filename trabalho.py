from validate_docbr import CPF
import re

cpf = input("Digite seu CPF: ")
cpf_validacao = CPF()
print("CPF VALIDADO:", cpf_validacao.validate(cpf))

def email_validacao(email):
    return bool(re.fullmatch(r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$', email))

email = input("Digite seu e-mail: ")
print("E-MAIL:", "VÁLIDO" if email_validacao(email) else "INVÁLIDO")

def telefone_validacao(telefone):
    return bool(re.fullmatch(r"\(\d{2}\) \d{5}-\d{4}", telefone))

telefone = input("Digite seu telefone: ")
print("TELEFONE:", "VÁLIDO" if telefone_validacao(telefone) else "INVÁLIDO")

def site_por_matricula(matricula):
    lista = [
        "Music Center", "Amazon", "Mercado Livre", "Magazine Luiza",
        "Casas Bahia", "Mundomax", "Carrefour", "Americanas", 
        "Ponto Frio", "Extra"
    ]
    ultimo_digito = int(str(matricula)[-1])
    site = lista[ultimo_digito]
    print("O site correspondente ao último dígito da matrícula é:", site)
    if ultimo_digito == 0:
        import Paginas.MusicCenter as music
        resultado = music.consultar_produto()
    elif ultimo_digito == 1:
        import Paginas.Amazon as amz
        resultado = amz.consultar_produto()
    elif ultimo_digito == 2:
        import Paginas.MercadoLivre as mec
        resultado = mec.consultar_produto()
    elif ultimo_digito == 3:
        import Paginas.MagazineLuiza as ml
        resultado = ml.consultar_produto()
    elif ultimo_digito == 4:
        import Paginas.CasasBahia as cb
        resultado = cb.consultar_produto()
    elif ultimo_digito == 5:
        import Paginas.Mundomax as mx
        resultado = mx.consultar_produto()
    elif ultimo_digito == 6:
        import Paginas.Carrefour as cf
        resultado = cf.consultar_produto()
    elif ultimo_digito == 7:
        import Paginas.Americanas as am
        resultado = am.consultar_produto()
    elif ultimo_digito == 8:
        import Paginas.PontoFrio as pf
        resultado = pf.consultar_produto()
    elif ultimo_digito == 9:
        import Paginas.Extra as ex
        resultado = ex.consultar_produto()
    print("Resultado da consulta em", site, ":", resultado)

matricula = input("Digite o número da matrícula: ")
site_por_matricula(matricula)