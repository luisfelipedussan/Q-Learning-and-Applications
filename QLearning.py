import numpy as numpy
import ramdom

#REINFORMENT LEARNING

alpha = 0.1 
gamma= 0.9 
epsilon= 0.2 

n_states = 10
n_acctions = 2
Q=  np.zeros((n_states,n_acctions))

'''se genera un numero aleatorio en 0,1 , si el numero es menor a epsilon , opta por explorar , 
epsilon es la tasa de eploracion , significa que si epsilon es 0.2 epsilon explorara el 20% del tiempo

Luego sigue la expliracion , si explora , la funcion selecciona una accion aleatoria entre todas las posibles 

explotacion: si no elige explorar , la funcion selecciona la accion que tiene el mayor valor Q en el estado actual, np.argmax encuentra el indice de la accion con el Q mas alto

Este balance entre exploración y explotación es crucial para que el agente pueda aprender de manera efectiva y
 descubrir nuevas estrategias que podrían resultar en recompensas más altas en el largo plazo.
'''
def elegir_accion(estado):
    if random.uniform(0,1) < epsilon:
        return random.choice(range(n_acctions))
    else: 

        return np.argmax(Q[estado])

def entrenar_agente(n_episodios):
    for episodio in range(n_episodios)
        estado =random.choice(range(n_states))
        while True:
            accion = elegir_accion(estado)
            siguiente_estado = (estado + accion) % n_states
            recompensa = -1

            #se actualiza la tabla Q, aqui ocurre el aprendizaje 
            Q[estado,accion] = Q[estado,accion] + alpha *(recompensa + gamma * np.max(Q[siguiente_estado])-Q[estado,accion])
            estado = siguiente_estado

            if estado == 0:  # Condición de finalización del episodio (ejemplo)
                break

# Entrenar el agente
entrenar_agente(1000)

# Mostrar la tabla Q aprendida
print(Q)
