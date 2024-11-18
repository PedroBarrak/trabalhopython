import urllib.request
from bs4 import BeautifulSoup

def consultar_produto():
    url = "https://www.mundomax.com.br/busca/?q=teclado%20yamaha%20psr%20e473"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        return

    soup = BeautifulSoup(response, 'html.parser')

    products = soup.find_all("div", class_="col-xs-6 col-sm-6 col-md-4 product-box")
    product_list = []

    for product in products:
        product_name_tag = product.find("span", class_="hidden-xs")
        product_price_tag = product.find("div", class_="product-priceBlue")
        product_link_tag = product.find("a", class_="product-link")

        if product_name_tag and product_price_tag and product_link_tag:
            product_name = product_name_tag.text.strip()
        
      
            product_price = product_price_tag.text.strip().replace("R$", "").replace(".", "").replace(",", ".")
            product_link = "https://www.mundomax.com.br" + product_link_tag['href']

            try:
                product_price = float(product_price)
                product_list.append({
                    "Nome": product_name,
                    "Preço": product_price,
                    "Link": product_link
                })
            except ValueError:
                continue

    if product_list:
        min_price_product = min(product_list, key=lambda x: x['Preço'])
        if "PSR-E473" not in min_price_product['Nome']:
            print("Produto Pesquisado Não encontrado. Produto Mais Barato da Busca")
        print(f"  Nome: {min_price_product['Nome']}")
        print(f"  Preço: R$ {min_price_product['Preço']:.2f}")
        print(f"  Link: {min_price_product['Link']}\n")
    else:
        print("Nenhum produto encontrado ou estrutura da página alterada.")

consultar_produto()

