import urllib.request
from bs4 import BeautifulSoup

def consultar_produto_carrefour():
    url = "https://www.carrefour.com.br/busca/teclado%20yamaha%20psr%20e473"

    # Cabeçalho para simular um navegador
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
    products = soup.find_all("a", class_="border rounded-lg border-[#f2f2f2] p-2 cursor-pointer")
    product_list = []

    for product in products:
        # Nome do produto
        product_name_tag = product.find("h2", class_="text-xs leading-4 text-[#333] text-left my-3 truncate-text h-12")
        # Preço do produto
        product_price_tag = product.find("span", class_="text-base font-bold text-primary")
        # Link para o produto
        product_link_tag = product['href'] if 'href' in product.attrs else None

        if product_name_tag and product_price_tag and product_link_tag:
            product_name = product_name_tag.text.strip()
            # Verifica se o nome do produto contém o termo "PSR-E473"
            if "PSR-E473" in product_name:
                product_price = product_price_tag.text.strip().replace("R$", "").replace(".", "").replace(",", ".")

                try:
                    # Convertendo o preço para float
                    product_price = float(product_price)
                    product_list.append({
                        "Nome": product_name,
                        "Preço": product_price,
                        "Link": "https://www.carrefour.com.br" + product_link_tag
                    })
                except ValueError:
                    # Ignorar preços que não puderam ser convertidos
                    continue

    # Encontrar o menor preço
    if product_list:
        min_price_product = min(product_list, key=lambda x: x['Preço'])
        print(f"Produto com o menor preço:")
        print(f"  Nome: {min_price_product['Nome']}")
        print(f"  Preço: R$ {min_price_product['Preço']:.2f}")
        print(f"  Link: {min_price_product['Link']}\n")
    else:
        print("Nenhum produto encontrado ou estrutura da página alterada.")

# Chamar a função para testar
consultar_produto_carrefour()
