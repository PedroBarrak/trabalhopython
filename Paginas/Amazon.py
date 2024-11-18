import urllib.request
from bs4 import BeautifulSoup

def consultar_produto():
    url = "https://www.amazon.com.br/s?k=teclado+yamaha+psr+e473&crid=H4RZRQFWYZFO&sprefix=teclado+yamaha+psr+e473%2Caps%2C175&ref=nb_sb_ss_ts-doa-p_1_23"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        page = urllib.request.urlopen(req)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        return None


    soup = BeautifulSoup(response, 'html.parser')

    products = soup.find_all("div", {"data-component-type": "s-search-result"})

    product_list = []
    for product in products:
        name_tag = product.find("span", class_="a-size-medium a-color-base a-text-normal")
        product_name = name_tag.text.strip() if name_tag else "Nome não encontrado"
        link_tag = product.find("a", class_="a-link-normal", href=True)
        product_link = f"https://www.amazon.com.br{link_tag['href']}" if link_tag else "Link não encontrado"
        price_tag = product.find("span", class_="a-price-whole")
        decimal_tag = product.find("span", class_="a-price-fraction")
        product_price = price_tag.text.strip() if price_tag else "Preço não encontrado"
        if decimal_tag:
            product_price += f",{decimal_tag.text.strip()}"

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

        print("Nenhum produto encontrado ou estrutura da página alterada.")

consultar_produto()

