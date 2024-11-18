import urllib.request
from bs4 import BeautifulSoup

def consultar_produto():
    url = "https://www.carrefour.com.br/busca/teclado%20yamaha%20psr%20e473"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    req = urllib.request.Request(url, headers=headers)
    try:
        page = urllib.request.urlopen(req)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        return None


    soup = BeautifulSoup(response, 'html.parser')

    products = soup.find_all("a", class_="border rounded-lg border-[#f2f2f2] p-2 cursor-pointer")

    product_list = []
    for product in products:

        product_name_tag = product.find("h2", class_="text-xs leading-4 text-[#333] text-left my-3 truncate-text h-12")
        product_price_tag = product.find("span", class_="text-base font-bold text-primary")
        product_link_tag = product['href'] if 'href' in product.attrs else None

        if product_name_tag and product_price_tag and product_link_tag:
            product_name = product_name_tag.text.strip()
            if "PSR-E473" in product_name:
                product_price = product_price_tag.text.strip().replace("R$", "").replace(".", "").replace(",", ".")

                try:
                    product_price = float(product_price)
                    product_list.append({
                        "Nome": product_name,
                        "Preço": product_price,
                        "Link": "https://www.carrefour.com.br" + product_link_tag
                    })
                except ValueError:
                    continue

    if product_list:
        cheapest_product = min(product_list, key=lambda x: float(x["price"].replace(".", "").replace(",", ".")))
        print("Produto mais barato encontrado:")
        print(f"Nome: {cheapest_product['name']}")
        print(f"Link: {cheapest_product['link']}")
        print(f"Preço: R$ {cheapest_product['price']}")
    else:

        print("Nenhum produto encontrado ou estrutura da página alterada.")

consultar_produto()

