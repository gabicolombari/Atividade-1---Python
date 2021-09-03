#---- Exercicio 1 ----

def eh_primo(n):
    divisores= 0
    i = 1 # número candidato
    while i <= n:
        if n % i == 0: 
            divisores +=1
        i +=1

    if divisores == 2:
        return True
    else:
        return False
    
pass

#---- Exercicio 2 ----
def lista_primos(n):
    encontrados = []
    for i in range(2, n):
        if eh_primo(i):
            encontrados.append(i)
    return encontrados
pass

#---- Exercicio 3 ----
def conta_primos(d):
    dic = {}
    for i in d:
        if eh_primo(i):
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    return dic
pass

#---- Exercicio 4 ----
def eh_armstrong(n):
    lista_vazia = []
    divid = 0 
    for i in str(n):
        carry = pow(int(i),len(str(n)))
        lista_vazia.append(carry)
    for i in lista_vazia:
        divid = divid+i
    if n == divid:
        return True
    else:
        return False 
pass

# ---- Exercicio 5 ----
def lista_armstrong(n):
    number_lista = []
    for i in range(0, n):
        if eh_armstrong(i):
            number_lista.append(i)
    return number_lista

lista_armstrong(1000)
print(lista_armstrong(1000))
pass

# ---- Exercicio 6 ----
def eh_perfeito(n):
    soma=0
    for g in range(1,n):
        if n % g == 0:
            soma += g

    if soma==n:
        return True
    else:
        return False
pass

# ---- Exercicio 7 ----

def lista_perfeitos(n):
    qtd_primos = []
    soma = 0
    for i in range(2, n):
        if eh_perfeito(i):
            qtd_primos.append(i)
    return qtd_primos
pass
