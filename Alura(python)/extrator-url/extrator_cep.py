endereco = "Rua da Flores 72, Apartamento 1002, Laranjeiras, Rio de Janeiro, Rj, 23440-120"

import re # Regular Expression == RegEx


# 5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #match
if busca:
    cep = busca.group()
    print(cep)