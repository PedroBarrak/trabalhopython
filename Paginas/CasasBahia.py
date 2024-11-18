import urllib.request
from bs4 import BeautifulSoup

def consultar_produto_casas_bahia():
    url = "https://www.casasbahia.com.br/teclado-yamaha-psr-e473/b"

    # Adicionar cabeçalho para simular um navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        return

    # Parsear o HTML com BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')

    # Encontrar todos os produtos listados
    products = soup.find_all("a", {"title": True})  # Filtra links com o atributo 'title'
    product_list = []

    for product in products:
        # Nome do produto
        product_name_tag = product.find("span", {"aria-hidden": "true"})
        # Preço do produto
        product_price_tag = product.find_next("span", class_="css-1vmkvrm")  # Localiza o próximo preço no HTML

        if product_name_tag and product_price_tag:
            product_name = product_name_tag.text.strip()
            product_price = product_price_tag.text.strip()
            product_link = product['href']

            product_list.append({
                "Nome": product_name,
                "Preço": product_price,
                "Link": product_link
            })

    # Exibir os produtos encontrados
    if product_list:
        for idx, prod in enumerate(product_list, 1):
            print(f"Produto {idx}:")
            print(f"  Nome: {prod['Nome']}")
            print(f"  Preço: {prod['Preço']}")
            print(f"  Link: {prod['Link']}\n")
    else:
        print("Nenhum produto encontrado ou estrutura da página alterada.")

# Chamar a função para testar
consultar_produto_casas_bahia()
