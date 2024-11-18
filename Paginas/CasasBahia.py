import urllib.request
from bs4 import BeautifulSoup


def consultar_produto():
    url = "https://www.casasbahia.com.br/teclado-yamaha-psr-e473/b"
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        page = urllib.request.urlopen(req)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        return None

    soup = BeautifulSoup(page, 'html.parser')
    products = soup.find_all("div", class_="product-card")

    product_list = []
    for product in products:
        name_tag = product.find("h2", class_="product-card-name")
        product_name = name_tag.text.strip() if name_tag else "Nome não encontrado"

        link_tag = product.find("a", href=True)
        product_link = f"https://www.casasbahia.com.br{link_tag['href']}" if link_tag else "Link não encontrado"

        price_tag = product.find("span", class_="price__sale")
        product_price = price_tag.text.strip() if price_tag else "Preço não encontrado"

        product_list.append({
            "name": product_name,
            "link": product_link,
            "price": product_price
        })

    if product_list:
        cheapest_product = min(product_list, key=lambda x: float(x["price"].replace(".", "").replace(",", ".")))
        print("Produto mais barato encontrado:")
        print(f"Nome: {cheapest_product['name']}")
        print(f"Link: {cheapest_product['link']}")
        print(f"Preço: R$ {cheapest_product['price']}")
    else:
        print("Nenhum produto encontrado.")

