"""
# pip install zenrows

from zenrows import ZenRowsClient

client = ZenRowsClient("2900b6a1f8dae35051043ea0c2eb9327155ba2ec")
url = "https://ekosnegocios.com/articulo/guayaquil-es-la-principal-puerta-de-entrada-y-salida-del-pais-al-extranjero-lo-que-se-mantiene-desde-la-pandemia"

response = client.get(url)

print(response.text)

"""

# pip install zenrows
from zenrows import ZenRowsClient

client = ZenRowsClient("2900b6a1f8dae35051043ea0c2eb9327155ba2ec")
url = "https://www.ecuadorlegalonline.com/divorcios/divorcio-ecuador/"

params = {"css_extractor":"{\"links\":\"a @href\",\"images\":\"img @src\"}"}

response = client.get(url, params=params)

print(response.text)


