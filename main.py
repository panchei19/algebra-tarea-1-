import numpy as np
import re
import pandas as pd

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



def vectorSentimientos(frase):
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

def vectorPalabrasclave(frase):
    palabras = re.sub(r'[.,]', '', frase).split()
    w=[]
    for palabra in palabras:
        if palabra in palabras_clave["negativas"]:
            w.append(1)
        if palabra in palabras_clave["positivas"]:
            w.append(1)
        if palabra in palabras_clave["neutrales"]:
            w.append(1)
        else: 
            w.append(0)
    return w


#CALIDAD PROMEDIO

def avg(frase):      
    s=vectorSentimientos(frase)
    return (s[0]+s[1]+s[2])/(len(palabras_clave["negativas"])+len(palabras_clave["positivas"])+len(palabras_clave["neutrales"]))

def pcj(vector):
    positivo=0
    neutro=0
    negativo=0
    if((vector[0]+vector[1]+vector[2])!=0):
        positivo= vector[0]/(vector[0]+vector[1]+vector[2])
        neutro=vector[1]/(vector[0]+vector[1]+vector[2])
        negativo=vector[2]/(vector[0]+vector[1]+vector[2])
    return [positivo, neutro, negativo]

def promedioSentimiento(frase):
    fraseSentimientos= vectorSentimientos(frase)
    a= np.array([1,0,-1])
    b=np.array(fraseSentimientos)
    if np.dot(a,b) > 0:
        return "Positivo"
    if np.dot(a,b) < 0:
        return "Negativo"
    if np.dot(a,b) == 0:
        return "Neutro"
    

def frase_mas_positiva(frases):
    max_positividad = -float('inf')
    frase_positiva = ""
    
    for frase in frases:
        valor_sentimiento = np.dot(np.array([1, 0, -1]), np.array(vectorSentimientos(frase)))
        if valor_sentimiento > max_positividad:
            max_positividad = valor_sentimiento
            frase_positiva = frase
    
    return frase_positiva

def frase_mas_negativa(frases):
    max_negatividad = float('inf')
    frase_negativa = ""
    
    for frase in frases:
        valor_sentimiento = np.dot(np.array([1, 0, -1]), np.array(vectorSentimientos(frase)))
        if valor_sentimiento < max_negatividad:
            max_negatividad = valor_sentimiento
            frase_negativa = frase
    
    return frase_negativa




frasesImprimir = []
calidad = []
positiva = []
neutra = []
negativa = []

datos = {
    "Frase": frasesImprimir,
    "Calidad promedio": calidad,
    "positiva": positiva,
    "neutra": neutra,
    "negativa": negativa
}

for frase in frases:
    frasesImprimir.append(frase)
    calidad.append(avg(frase))
    positiva.append(pcj(vectorSentimientos(frase))[0])
    neutra.append(pcj(vectorSentimientos(frase))[1])
    negativa.append(pcj(vectorSentimientos(frase))[2])
    #print(frase + " || " + "Calidad promedio: " + str(avg(frase)) + " || Promedio de sentimientos: " + promedioSentimiento(frase)+ " || W: " + str(vectorPalabrasclave(frase)) + " || S:" + str(vectorSentimientos(frase)) + " || " + pcj(vectorSentimientos(frase)))

df = pd.DataFrame(datos)
print(df)

frase_positiva = frase_mas_positiva(frases)
frase_negativa = frase_mas_negativa(frases)

print(" ")
print(f"La frase más positiva es: '{frase_positiva}'")
print(f"La frase más negativa es: '{frase_negativa}'")