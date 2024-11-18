import urllib.request
from bs4 import BeautifulSoup

# URL da página a ser raspada
url = "https://www.mercadolivre.com.br"

try:
    # Faz a requisição para a página
    page = urllib.request.urlopen(url)
except Exception as e:
    print("Erro ao carregar a página:", e)
    exit()

# Faz o parsing do HTML
soup = BeautifulSoup(page, 'html5lib')

# Encontra todos os produtos na página
products = soup.find_all("li", class_="ui-search-layout__item")

product_list = []

# Loop para extrair informações de cada produto
for product in products:
    # Nome do produto
    name_tag = product.find("h2", class_="ui-search-item__title")
    product_name = name_tag.text.strip() if name_tag else "Nome não encontrado"

    # Link do produto
    link_tag = product.find("a", href=True)
    product_link = link_tag['href'] if link_tag else "Link não encontrado"

    # Preço atual
    current_price_tag = product.find("span", class_="price-tag-fraction")
    current_price = current_price_tag.text.strip() if current_price_tag else "Preço atual não encontrado"

    # Adiciona os dados do produto à lista
    product_list.append({
        "name": product_name,
        "link": product_link,
        "price": current_price
    })

# Encontra o produto com o menor preço
if product_list:
    # Convertendo os preços para números e encontrando o menor
    for product in product_list:
        try:
            product["price_value"] = float(product["price"].replace(".", "").replace(",", "."))
        except ValueError:
            product["price_value"] = float('inf')

    cheapest_product = min(product_list, key=lambda x: x["price_value"])

    print("Produto mais barato encontrado:")
    print(f"Nome: {cheapest_product['name']}")
    print(f"Link: {cheapest_product['link']}")
    print(f"Preço: R$ {cheapest_product['price']}")
else:
    print("Nenhum produto foi encontrado.")
