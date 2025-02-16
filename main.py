import pip._vendor.requests as requests
from bs4 import BeautifulSoup 
fer = "Python (lenguaje de programación)"
url = f"https://es.wikipedia.org/wiki/{fer}"
response = requests.get(url)
if response.status_code == 200:
					# Parsear el contenido HTML usando BeautifulSoup
				soup = BeautifulSoup(response.content, 'html.parser')
					
					# Encontrar el primer párrafo del artículo de Wikipedia
				primer_parrafo = soup.find('div', class_='mw-parser-output').p.get_text()
					
					# Imprimir el resultado por pantalla
				print(f"Información de Wikipedia sobre '{fer}':")
				print(primer_parrafo)
else:
				print(f"No se pudo obtener la información de Wikipedia para '{fer}'")
