import urllib.request
from bs4 import BeautifulSoup

def consultar_produto():
    url = "https://www.magazineluiza.com.br/busca/teclado+yamaha+psr+e473/?from=submit"

    try:
        page = urllib.request.urlopen(url)
    except Exception as e:
        print("Erro ao carregar a página:", e)
        return

    soup = BeautifulSoup(page, 'html.parser')

    # Encontrar todos os produtos listados
    products = soup.find_all("a", {"data-testid": "product-card-container"})
    product_list = []

    for product in products:
        # Nome do produto
        name_tag = product.find("h2", {"data-testid": "product-title"})
        product_name = name_tag.text.strip() if name_tag else "Nome não encontrado"

        # Preço do produto
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

        # Link do produto
        link_tag = product['href'] if 'href' in product.attrs else "Link não encontrado"
        product_link = f"https://www.magazineluiza.com.br{link_tag}" if link_tag else "Link não encontrado"
        
        product_list.append({
            "name": product_name,
            "link": product_link,
            "price": current_price_value
        })

    # Verificar e imprimir o produto mais barato
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

# Chamar a função para testar
consultar_produto()
