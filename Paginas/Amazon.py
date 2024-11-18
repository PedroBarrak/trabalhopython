import urllib.request
from bs4 import BeautifulSoup

def consultar_produto():
    url = "https://www.amazon.com.br/s?k=teclado+yamaha+psr+e473&crid=3VIMXBYNJ4RGI&sprefix=%2Caps%2C463"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        return

    soup = BeautifulSoup(response, 'html.parser')

    products = soup.find_all("div", {"data-component-type": "s-search-result"})
    product_list = []

    for product in products:
        product_name_tag = product.find("span", class_="a-size-base-plus a-color-base a-text-normal")
        product_price_tag = product.find("span", class_="a-offscreen")
        product_link_tag = product.find("a", class_="a-link-normal")

        if product_name_tag and product_price_tag and product_link_tag:
            product_name = product_name_tag.text.strip()
            product_price = product_price_tag.text.strip()
            product_link = "https://www.amazon.com.br" + product_link_tag['href']

            product_list.append({
                "Nome": product_name,
                "Preço": product_price,
                "Link": product_link
            })

    if product_list:
        for idx, prod in enumerate(product_list, 1):
            print(f"Produto {idx}:")
            print(f"  Nome: {prod['Nome']}")
            print(f"  Preço: {prod['Preço']}")
            print(f"  Link: {prod['Link']}\n")
    else:
        print("Nenhum produto encontrado ou estrutura da página alterada.")

consultar_produto()
