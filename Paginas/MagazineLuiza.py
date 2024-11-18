import urllib.request
from bs4 import BeautifulSoup

def consultar_produto():
    url = "https://www.magazinevoce.com.br/magazinebusca360/busca/teclado+yamaha+psr+e473/?from=submit"
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        page = urllib.request.urlopen(req)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        return None

    soup = BeautifulSoup(page, 'html.parser')
    products = soup.find_all("li", class_="nm-product-item")


    products = soup.find_all("a", {"data-testid": "product-card-container"})

    product_list = []
    for product in products:

        name_tag = product.find("h2", {"data-testid": "product-title"})
        product_name = name_tag.text.strip() if name_tag else "Nome não encontrado"

        price_tag = product.find("p", {"data-testid": "price-value"})
        if price_tag:
            current_price = price_tag.text.strip()
            try:
                current_price_value = float(
                    current_price.replace("ou ","").replace("R$", "").replace(".", "").replace(",", ".").strip()
                )
            except Exception as e:
                print(f"Erro ao processar o preço '{current_price}': {e}")
                current_price_value = float('inf')
        else:
            current_price = "Preço não encontrado"
            current_price_value = float('inf')

        link_tag = product['href'] if 'href' in product.attrs else "Link não encontrado"
        product_link = f"https://www.magazineluiza.com.br{link_tag}" if link_tag else "Link não encontrado"
        

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

        print("Nenhum produto foi encontrado.")

consultar_produto()
