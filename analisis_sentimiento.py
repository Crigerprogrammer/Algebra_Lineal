import numpy as np
import pandas as pd
def feeling(Tweet):
  tweet = Tweet.replace("!","").replace(",","").replace(".","").lower().split(" ")

  palabras =['muerte','pérdida','luto','excelente','gran','positivo','bueno','inteligente','ignorante','platzi','aprender','estudio','bien','queiro']

  palabras_positivas =["excelente","gran","quiero","positivo",'bien','positivo','bueno','inteligente']
  palabras_neutras = ["pérdida",'aprender','estudio','platzi']
  palabras_negativas = ["muerte","luto",'ignorante']

  w = []
  positivas = 0
  neutras = 0
  negativas = 0
  

  for i in palabras:
    w.append(tweet.count(i))
    if i in tweet and i in palabras_positivas:
      positivas += 1
    elif i in tweet and i in palabras_neutras:
      neutras += 1
    elif i in tweet and i in palabras_negativas:
      negativas += 1

  s = np.array([positivas,neutras,negativas])
  w = np.array(w)

  avg = (np.ones(w.size)/w.size).T.dot(w)
  score = s/(s[0]+s[1]+s[2])
  return Tweet,avg,score[0],score[1],score[2]

tweet1 = "Gran mexicano y excelente en su área, su muerte es una enorme perdida y debería ser luto nacional!!!"

tweet2 = "Vaya señora que bueno que se asesora por alguien inteligente no por el ignorante del Gatt"

tweet3 = "Se me ocurre y sin ver todos los videos de Plazti que me informéis por dónde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo"

tweet4 = "Soy docente universitario, estoy intentando preparar mis clases en modo platzi bien didáctico, (le llamo modo noticiero), descargue una plataforma gratuita de grabación y transmisión de vídeo, se llama Obs estudio!bueno la sigo remando con sus funciones pero sé que saldrá algo!"

tweets = [tweet1,tweet2,tweet3,tweet4]
resultados = []

for j in tweets:
  resultados.append(feeling(j))
  
df = pd.DataFrame(resultados, columns=["Tweet","Calidad","P_positiva","P_neutra","P_negativa"])
df