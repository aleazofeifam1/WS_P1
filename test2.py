from collections import  Counter
import os
import re
frequency = {}

pronombresComunes = ['yo', 'me', 'mí', 'nos', 'nosotras','nosotros','conmigo','te','ti','tú','os','usted','ustedes','vos','vosotras','vosotros',
                     'contigo','él','ella','ellas','ello','ellos','las','lo','los','le','les','se','sí','consigo','aquéllas','aquélla','aquéllos',
                     'aquél','aquellas','aquella','aquellos','aquel','aquello','ésas','ésa','esos','ese','ésos','ése','eso','esotra','esotro','esta',
                     'éstas','ésta','estas','esta','estos','este','éstos','éste','esto','mía','mías','mío','míos','nuestra','nuestras','nuestro',
                     'nuestros','suya','suyas','suyo','suyos','tuya','tuyas','tuyo','tuyos','vuestra','vuestras','vuestro','vuestros','algo','alguien',
                     'alguna','algunas','alguno','algunos','cualesquiera','cualquiera','demás','misma','mismas','mismo','mismos','mucha','muchas','mucho',
                     'muchos','nada','nadie','ninguna','ningunas','ninguno','ningunos','otra','otras','otro','otros','poca','pocas','poco','pocos','quienquier',
                     'quienesquiera','quienquiera','tanta','tantas','tanto','tantos','toda','todas','todo','todos','última','últimas','último','últimos','una',
                     'unas','uno','unos','varias','varios','adónde','cómo','cuál','cuáles','cuándo','cuánta','cuántas','cuánto','cuántos','dónde','qué','quién',
                     'quiénes']

directory = os.path.normpath("C:/Alejandro/TxtProyecto")
for subdir, dirs, files in os.walk(directory):
    bibTXT = open(os.path.join(subdir, "ReinaValera1960.txt"), 'r')
    leeBiblia = bibTXT.read().__str__()

s1 = set(leeBiblia.split())
s2 = set(pronombresComunes)

#print (s1.intersection(s2))
#

#_____________________Funciona el codigo de aqui para arriba, pero no cuenta las palabras_____________________________

inter = (s1.intersection(s2))
  #  cuenta = Counter(inter)
#print(inter.__str__())
#print(cuenta)

#____________________Ensena cada vez que se usa palabra e indica que solo se uso una vez______________________________


# for word in inter:
#     count = frequency.get(word, 0)
#     frequency[word] = count + 1
#
#     frequency_list = frequency.keys()
#     for words in frequency_list:
#      #   print (words, frequency[words])
#

#__________________Abajo si imprime cada uno de los pronombres que existen________________

#print (re.findall(r"(?=("+'|'.join(pronombresComunes)+r"))",leeBiblia))

pronombreAnalisadoIndividualmente = re.findall(r"(?=("+'|'.join(pronombresComunes)+r"))",leeBiblia)

#________________ Detalla la cantidad de veces que se repite cada palabra_________________

for word in pronombreAnalisadoIndividualmente:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
for words in frequency_list:
    print(words, frequency[words])

#__________________
#Upload txt file to flask
#Hace falta poner bullets en el menu principal
#Hace falta hacer un link en el menu principal que ligue las dos paginas

