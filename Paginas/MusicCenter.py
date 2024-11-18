import urllib.request
from bs4 import BeautifulSoup

def consultar_produto():
    wiki = "https://loja.music-center.art.br/loja/busca.php?loja=1154666&palavra_busca=teclado+yamaha+psr+e473"

    try:
        page = urllib.request.urlopen(wiki)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        exit()

    soup = BeautifulSoup(page, 'html5lib')

    products = soup.find_all("li", class_="item flex")
    product_list = []

    for product in products:
        name_tag = product.find("div", class_="product-name")
        product_name = name_tag.text.strip() if name_tag else "Nome não encontrado"

        link_tag = product.find("a", href=True)
        product_link = link_tag['href'] if link_tag else "Link não encontrado"
        current_price_tag = product.find("span", class_="current-price")
        if current_price_tag:
            current_price = current_price_tag.text.strip()
            try:
                current_price_value = float(
                    current_price.replace("R$", "").replace(".", "").replace(",", ".").strip()
                )
            except Exception as e:
                print(f"Erro ao processar o preço '{current_price}': {e}")
                current_price_value = float('inf')
        else:
            current_price = "Preço atual não encontrado"
            current_price_value = float('inf')
        product_list.append({
            "name": product_name,
            "link": product_link,
            "price": current_price_value
        })

    if product_list:
        valid_products = [p for p in product_list if p["price"] != float('inf')]
        if valid_products:
            cheapest_product = min(valid_products, key=lambda x: x["price"])
            print("Produto mais barato encontrado:")
            print(f"Nome: {cheapest_product['name']}")
            print(f"Link: {cheapest_product['link']}")
            print(f"Preço: R$ {cheapest_product['price']:.2f}")
        else:
            print("Nenhum produto com preço válido foi encontrado.")
    else:
        print("Nenhum produto foi encontrado.")

consultar_produto()