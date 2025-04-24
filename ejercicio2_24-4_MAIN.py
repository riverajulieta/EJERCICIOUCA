#generar grilla
import random
 
def generar_grilla():
     grilla= []
     for i in range(46):
         grilla.append(i)
         return grilla
         
#generar grilla jugador
def generar_jugador():
    return random.sample(range(46),6)

jugador1= generar_jugador
jugador2= generar_jugador

#sorteo
def sorteo_quini6(grilla, player1, player2):
    sorteo = []
    while grilla and player1 and player2:
        numero_sorteo = random.choice(grilla)
        sorteo.append(numero_sorteo)
        print(f"Numero sorteado: {numero_sorteo}")
        
        if numero_sorteo in player1:
            player1.remove(numero_sorteo)
        print("Player1 tenía el número")
        
        if numero_sorteo in player2:
            player2.remove(numero_sorteo)
            print("Player2 tenía el número")
            
    grilla.remove(numero_sorteo)
    return sorteo, plater1, player2
    
#mostrar resultados 
def mostrar_resultados(sorteo, player1,player2):
    print("\n Números sorteados", sorteo)
    print("Player1 restantes:", player1)
    print("Player2 restantes:", player2)
    
    if not player1 and not player2:
        print("Empate")
    elif not player1: 
        print("Player1 ganó")
    elif not player2:
        print("Player2 ganó")
        
def main():
    
    grilla = generar_grilla()
    player1 = generar_jugador()
    player2 = generar_jugador()
    
    print("Player1: ", player1)
    print("Player2: ", player2)
    
    sorteo, restante1,restante2 = sorteoquini6(grilla,player1,player2)
    mostrar_resultados(sorteo,restante1,restante2)
    
if __name__=="__main__":
    main()