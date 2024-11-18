import urllib.request
from bs4 import BeautifulSoup
def consultar_produto():
    url = "https://lista.mercadolivre.com.br/teclado-yamaha-psr-473#D[A:teclado%20yamaha%20psr-473]"

    try:
        page = urllib.request.urlopen(url)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        exit()

    soup = BeautifulSoup(page, 'html5lib')

    products = soup.find_all("li", class_="ui-search-layout__item")

    product_list = []

    for product in products:
        name_tag = product.find("h2", class_="poly-component__title")
        product_name = name_tag.text.strip() if name_tag else "Nome não encontrado"

        link_tag = product.find("a", href=True)
        product_link = link_tag['href'] if link_tag else "Link não encontrado"

        current_price_tag = product.find("span", class_="andes-money-amount")
        current_price = current_price_tag.text.strip() if current_price_tag else "Preço atual não encontrado"

        product_list.append({
            "name": product_name,
            "link": product_link,
            "price": current_price
        })

    if product_list:
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

consultar_produto()