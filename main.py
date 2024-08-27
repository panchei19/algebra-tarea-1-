import numpy as np
import re

frases = [
    "Me siento muy feliz con mi progreso este mes.",
    "Este proyecto ha sido un fracaso total.",
    "La presentación fue buena, pero pudo ser mejor.",
    "Qué gran día para salir a pasear y disfrutar.",
    "Este lugar es horrible, no vuelvo más.",
    "Es una película interesante con momentos aburridos.",
    "La atención al cliente fue excelente, estoy satisfecho.",
    "Todo estuvo regular, ni bien ni mal.",
    "El servicio fue pésimo y la comida no tenía sabor.",
    "Estoy agradecido por la ayuda que recibí.",
    "El clima está muy agradable hoy.",
    "Qué decepción, esperaba mucho más de este evento.",
    "El evento estuvo bien organizado y fue divertido.",
    "No tengo opinión, me pareció indiferente.",
    "Fue una experiencia enriquecedora y gratificante."
]

# Palabras clave
palabras_clave = {
    "positivas": [
        "feliz", "gran", "excelente", "satisfecho", "agradecido", 
        "agradable", "bien", "organizado", "divertido", 
        "enriquecedora", "gratificante"
    ],
    "neutrales": [
        "progreso", "regular", "interesante", "bien", 
        "indiferente", "opinión"
    ],
    "negativas": [
        "fracaso", "horrible", "aburridos", "pésimo", 
        "sin sabor", "decepción"
    ]
}



def vector(frase):
    # Usar re para eliminar los signos de puntuación y luego hacer el split
    palabras = re.sub(r'[.,]', '', frase).split()
    s=[0,0,0]
    for palabra in palabras:
        if palabra in palabras_clave["positivas"]:
            s[0]+=1
        if palabra in palabras_clave["neutrales"]:
            s[1]+=1
        if palabra in palabras_clave["negativas"]:
            s[2]+=1
    return s



def avg(w):
    s=vector(w)
    print(s)
    return (s[0]+s[1]+s[2])/len(w.split())

def promedioSentimiento(s):
    a= np.array([1,0,-1])
    b=np.array(s)
    return np.dot(a,b)


for frase in frases:
    print(frase,avg(frase))
    print(promedioSentimiento(vector(frase)))