from art import logo
import random

def find_number():
    print(logo)
    print("Bienvenido al juego del número aleatorio!")
    
    while True:
        dificultad = input("Elige tu dificultad: 'easy' para 10 intentos, 'hard' para 5: ")
        n_intentos = 0
        
        if dificultad == "easy":
            n_intentos = 10
        elif dificultad == "hard":
            n_intentos = 5
    
        numero_random = random.randint(1, 100)

        
        while n_intentos > 0:
            eleccion = int(input(f"Tienes {n_intentos} intentos. Elige tu número: "))
            
            if eleccion < numero_random:
                print("Tu número tiene que ser más grande.")
            elif eleccion > numero_random:
                print("Tu número tiene que ser más pequeño.")
            else:
                print(f"Ganaste. El número era {eleccion}")
                break
            
            n_intentos -= 1

        if eleccion == numero_random:
            volver_jugar = input("¿Quieres volver a jugar? 'si' o 'no': ")
            if volver_jugar.lower() != "si":
                break
        else:
            print(f"Perdiste. Te quedaste sin intentos. El número era {numero_random}")
            volver_jugar = input("¿Quieres volver a jugar? 'si' o 'no': ")
            if volver_jugar.lower() != "si":
                break
        
        print("------------------------------------------------")
        

find_number()
