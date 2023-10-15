import requests
from bs4 import BeautifulSoup

def encontrar_dir(target, box_words):
    try:
        with open(box_words, 'r') as f:
            box_words = f.read().splitlines()
        
        response = requests.get(target)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            
            dir = []
            for link in links:
                href = link.get('href')
                if href.endswith('/'):
                    for word in box_words:
                        if word in href:
                            dir.append(href)
                            break
            
            return dir
        else:
            print(f"Falha encontrada. Status code: {response.status_code}")
    except Exception as e:
        print(f"Um erro ocorrido: {e}")

if __name__ == "__main__":
    host_input = input("Entre com a URL ou IP do host: ")
    wordlist_file = input("Entre com o nome do arquivo: ")
    
    dir = encontrar_dir(host_input, wordlist_file)
    
    if dir:
        print("Diretorio Encontrado:")
        for direct in dir:
            print(direct)
    else:
        print("Diretorio não encontrado.")
