from collections import Counter
lista_ejemplo = ['6E', '7E', '4E']

def dividirmano(mano):
    carta1 = mano[0]
    carta2 = mano[1]
    carta3 = mano[2]

    return carta1, carta2, carta3

def extraerDatos(carta):
    palo = carta[-1]        
    aux = carta[0:-1]
    valor = int(aux)     

    if (valor >= 10):             
        valor = 0
    
    return palo, valor

def contarEnvido(mano):
    carta1,carta2,carta3 = dividirmano(mano)
    palo1, aux1 = extraerDatos(carta1)
    palo2, aux2 = extraerDatos(carta2)
    palo3, aux3 = extraerDatos(carta3)

    if ((palo1 == palo2) and (palo2 == palo3)):
        valores = [aux1, aux2, aux3]
        valores.sort()
        canto = valores[1:]
        suma = 20 + canto[0] + canto[1]
        texto = "La suma del envido es: " + str(suma)
        
    elif ((palo1 == palo2) and (palo2 != palo3)):
        suma = 20 + aux1 + aux2
        texto = "La suma del envido es: " + str(suma)
        #print("La suma del envido es: {}".format(suma))

    elif ((palo1 == palo3) and (palo1 != palo2)):
        suma = 20 + aux1 + aux3
        texto = "La suma del envido es: " + str(suma)
        #print("La suma del envido es: {}".format(suma))
        
    elif ((palo2 == palo3) and (palo1 != palo2)):
        suma = 20 + aux2 + aux3
        texto = "La suma del envido es: " + str(suma)
        #print("La suma del envido es: {}".format(suma))
        
    else:
        #print("Mentiste. No tenias nada para el envido")
        suma = max([aux1,aux2,aux3])
        texto = "La suma del envido es: " + str(suma)
        #print("La suma del envido es: {}".format(suma))
    
    
    return texto

envido = contarEnvido(lista_ejemplo)