def clasificar_arma(opcion_menu):
    if opcion_menu == 1:
        return "Legendaria"
    elif opcion_menu == 2:
        return "Media"
    else:
        return "Debil"

def es_critico(es_magica, nivel):
    return es_magica or nivel >= 10

def dano_base(ataque, poder, defensa):
    return (ataque + poder) - defensa

def dano_total(ataque, poder, defensa, critico):
    base = dano_base(ataque, poder, defensa)
    if critico == True:
        return base * 2
    else:
        return base

print("1 - escopeta")
print("2 - espada")
print("3 - tirachinas")

opcion = int(input("Escriba el numero de su arma: "))

if opcion == 1:
    es_magica = True
else:
    es_magica = False

nivel = 0

if opcion == 1:
    poder = 50   
elif opcion == 2:
    poder = 25   
else:
    poder = 5    

ataque = 40       
defensa = 15

resultado_arma = clasificar_arma(opcion)
resultado_critico = es_critico(es_magica, nivel)
danio_base_calculado = dano_base(ataque, poder, defensa)
danio_final = dano_total(ataque, poder, defensa, resultado_critico)

print("El poder de tu arma es:", resultado_arma)
print("¿El golpe es crítico?:", resultado_critico)
print("El daño BASE realizado es:", danio_base_calculado)
print("El daño total realizado es:", danio_final)
