#LÓGICA E (and)
# é a lógica do login
#email e a senha sejam true

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

    #Lógica OU (or)

    logica_ou= False or True or False
    print(logica_ou)

    #NOT
    negacao= not True
    print(negacao)

    if not verifica_login:
        print("Acerta ai")

