#url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = ''

# Sanitização da Utl
url = url.strip()
#url = url.replace(' ','')

# Validação url
if url == '':
    raise ValueError("A Url está vazia ")

# Separa a base e os parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o Valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)# onde começa
indice_valor = indice_parametro + len(parametro_busca) + 1# len retorna o tamanho da string
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == - 1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

# url.strip() tira os espaços em branco do começo e do fim