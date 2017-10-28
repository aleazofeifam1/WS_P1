from flask import Flask, render_template, request, send_from_directory
import os
import re
from werkzeug.utils import secure_filename

ALLOWED_EXTENTIONS = set(['txt'])
UPLOAD_FOLDER = os.path.dirname(__file__)
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join(UPLOAD_FOLDER,'static')
directory = os.path.normpath("C:/Alejandro/TxtProyecto")
frequency = {}


app.config['UPLOADED_TEXT_DEST'] = 'static/txt'

@app.route('/')
def Hello_World():
    return render_template('index.html')

@app.route('/upload')
def upload_file():
   return render_template('UploadText.html')
  #  return render_template('Up2.html')

# @app.route('/uploader', methods = ['GET', 'POST'])
# def uploader1():
#     if request.method == 'POST':
#         resultado = request.files['archivo']
#         resultado.save(secure_filename(resultado.filename))
#     else:
#         resultado = request.args.get['archivo']
#     return resultado
#
# @app.route('/upload2',methods = ['GET', 'POST'])
# def upload():
# #   return render_template('UploadText.html')
#     return render_template('Up2.html')


@app.route('/getfile', methods=['GET','POST'])
def getfile():
    if request.method == 'POST':
        result = request.files['myfile']
    else:
        result = request.args.get['myfile']
    return result

@app.route('/TextoCompleto')
def el_Texto():

    directory = os.path.normpath("C:/Alejandro/TxtProyecto")
    for subdir, dirs, files in os.walk(directory):
            bibTXT = open(os.path.join(subdir, "ReinaValera1960.txt"), 'r')
            leeBiblia = bibTXT.read()
            #print(leeBiblia)
            return "<h1>Biblia Reina Valera 1960</h1>" + leeBiblia

@app.route('/CantidadTotal')
def clasificacion_Del_Total():
    for subdir, dirs, files in os.walk(directory):
        bibTXT = open(os.path.join(subdir, "ReinaValera1960.txt"), 'r')
        textSting = bibTXT.read()
        TotalMatch = re.findall(r'\b[a-z]{2,20}\b', textSting) #Esta expresion regular, busca palabras con un lenght de minimo 2 y maximo 20 caracteres

    for word in TotalMatch:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()
    for words in frequency_list:
        print ( words, frequency[words])
        #print('Palabras: [' + words + '] Frequencia: ' + frequency[words])
    return "El detalle de la cantidad de palabras en todo el texto se ensena en consola"

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
@app.route('/Pronombres')
def clasificacion_De_Pronombre():

    return "El detalle de la cantidad de pronombres en todo el texto se ensena en consola"

adjetivosComunes = ['promedio','grande', 'colosal','gordo','gigante','gigantesco','gran','enorme', 'inmenso', 'grande',
	'chico', 'pequeño', 'largo', 'massivo', 'pequeño', 'chico', 'corto', "pequeño","alto","diminuto","amplio","rechoncho",
	"gordito","chueco","torcido" ,"curvo","profundo","plano","alto","hueco","ajo","estrecho","redondo","flaco","cuadrado",
	"inclinado","derecho","ancho","amargo","delicioso","fresco","jugoso","maduro","podrido","salado","acido","picante","rancio",
	"pasado","pegajos","fuerte","dulce","sin sabor","sabroso","sediento","grasoso","sucio","duro","aliente","elado","flojo",
	"suelto","derretido","plastico","lluvioso","aspero","disperso","filoso","sedoso","resbaloso","suave" ,"solido"  ,"firme"    ,
	"tierno"  ,"ajustado","desnivelado","debil" ,"enojado","asutado" ,"enojado" ,"molesto" ,"harto" "ansioso" ,"arrogante",
	"avergonzado","terrible"  ,"aburrido","confundido","confuso"   ,"cruel" ,"peligroso" ,"derrotado","desafiante" ,"deprimido","perturbado" ,
	"verguenza" ,"envidioso","malvado","malo","feroz","tonto","absurdo" ,"frenetico","asustado","aflijido","desamparado" ,"hambriento",
	"herido","celoso","solo","misterioso","travieso","malcriado","nervioso","repulsivo","egoista","adolorido","inflamado","tenso","terrible","preocupado",
	"molesto","cansado","preocupado","valiente","calmado","encantador","alegre","comodo","cooperativo","valeroso","resuelto","impaciente","exaltado","energico",
	"entusiasta","emocionado","exuberante","justo" ,"fiel","fantastico","bien","amigable","gracioso","gentil","glorioso","saludable","util","hilarante","feliz",
	"bueno","gentil","afortunado","obediente","perfecto","agradable","orgulloso","tonto","esplendido","exitoso","victorioso","vivaz","ingenioso","maravilloso","entusiasta"]
@app.route('/Adjetivo')
def clasificacion_De_Adjetivo():
    return "El detalle de la cantidad de adjetivos en todo el texto se ensena en consola"

verbosComunes = ["aceptar","permitir","dejar","preguntar","creer","prestar","romper","traer","comprar","poder","cancelar","cambiar","limpiar","peinar","quejarse","toser","contar",
"cortar","bailar","dibujar","beber","conducir","comer","explicar","caerse","llenar","encontrar","terminar","cerrar","organizar","pagar","jugar","poner","llover","leer","responder",
"correr","decir","ver","vender","enviar","firmar","cantar","sentarse","dormir","fumar","hablar","deletrear","gastar","ponerse","comenzar","estudiar","tener","nadar","tomar","caber",
"reparar","volar","dar","ir","tener","oir","danar","herir","saber","conocer","aprender","salir","marcharse","escuchar","vivir","mirar","perder","hacer","necesitar","abrir","hablar",
"ensenar","decir","pensar","traducir","viajar","intentar","apagar","encender","entender","utilizar","usar","esperar","despertar","querer","desear","mirar","trabajar","preocuparse","escribir",
"Ser","Estar" ,"Decir" ,"Venir" ,"Ir" ,"Hablar" ,"Tener" ,"Hacer" ,"Haber" ,"Poner" ,"Deber" ,"Poder" ,"Salir","Entrar" ,"Escribir","Llamar" ,"Bailar" ,"Visitar" ,"Viajar" ,"Buscar","Encontrar"
,"Celebrar" ,"Regalar" ,"Arreglar" ,"Trabajar" ,"Estudiar" ,"Formar" ,"Aprender" ,"Crear" ,"Rodar","Filmar","Investigar" ,"Preparar" ,"Cocinar" ,"Cenar"	,"Desayunar" ,"Almorzar" ,"Merendar","Beber" ,"Volar",
"Pasear" ,"Andar","Marchar","Correr","Ver" 	,"Observar" ,"Mirar" ,"Utilizar" ,"Comunicarse" ,"Grabar","Dormir","Despertar","Sacar","Unir","Ligar","Saltar","Cantar" ,"Probar" ,"Gustar","Leer" ,"Escuchar" ,"Nadar" ,
"Limpiar" ,"Practicar","Levantarse"	,"Darse la vuelta","Girar"	,"Vestir","Vivir","Morir" ,"Entregar","Enviar" ,"Atacar","Herir","Apaciguar","Firmar","Emborracharse" ,"Acoger" ,"Admitir" 	,"Solicitar" ,"Reservar" ,
"Comprar" ,"Ganar" ,"Compartir" ,"Salvar","Ayudar" ,"Guardar","Reafirmar" ,"Asentir" ,"Negar","Subir","Bajar" ,"Estrenar" ,"Manchar" ,"Mojar" ,"Secar" ,"Reproducir" ,"Alojarse" ,"aceptar","agregar","admirar","admitir",
"aconsejar","Afrontar","permitirse","estar","Acordar","alertar","permitir","entretener","analizar","anunciar","molestar","contestar","pedir","disculpar","aparecer","aplaudir","apreciar","aprobar","discutir","arreglar",
"arrestar","llegar","preguntar","adjuntar","atacar","intentar","asistir","atraer","evitar","apoyar","hornear","balancear","prohibir","bañarse","rogar","comportarse","pertenecer","bendecir","cegar","parpadear","enrojecer",
"hervir","reservar","aburrir","Pedir","prestar","rebotar","frenar","respirar","cepillar","quemar","enterrar","llamar","calcular","acampar","cuidar","causar","desafiar","cambiar","cargar","cazar","engañar","verificar","alegrar",
"mascar","reclamar","aplaudir","limpiar","aclarar","cerrar","cobrar","coleccionar","peinar","comparar","competir","quejarse","completar","concentrarse","concernir","confesar","confundir","conectar","considerer","consistir",
"contener","continuar","copiar","corregir","toser","contar","cubrir","rajar","embestir","atropellar","arrastrarse","cruzar","aplastar","gritar","llorar","curar","rizar","curvar","pasear","dañar","bailar","engañar","decidir",
"decorar","demorar","deleitar","repartir","depender","describir","merecer","destruir","detectar","descubrir","doblar","seguir","continuar","engañar","forzar","formar","fundar","enmarcar","asustar","freír","recoger","reunir",
"saludar","graduarse","graduar","engrasar","gruñir","adivinar","guiar","martillar","pasar","entregar","colgar","suceder","dañar","odiar","encabezar","calentar","ayudar","cazar","esperar","abrazar","apurarse","ganar",
"educar","avergonzar","emplear","vaciar","alentar","finalizar","disfrutar","ingresar","entretener","huir","enfrentar","decolorarse","fracasar","imaginar","desear","atar","abrochar","enviar","temer","vayan","buscar",
"archivar","llenar","filmar","disparar","despedir","encajar","quedar","reparar","brillar","centellear","flotar","inundarse","fluir","circular","florecer","interesar","interferir","interrumpir"
,"inventar","invitar","irritar","encarcelar","unir","juntar","bromear","juzgar","saltar","patear","matar","besar","arrodillarse","tejer","golpear","anudar","etiquetar","aterrizar","durar","reírse",
"lanzar","nivelar","lamer","mentir","iluminar","alivianar","gustar","administrar","marchar","marcar","casarse","haciendo","juegar","unir","medir","derretirse","memorizar","remendar","ordeñar","perder","extrañar",
"mezclar","mover","mudarse","multiplicar","asesinar","clavar","nombrar","necesitar","advertir","fijar","fijarse","darse","numerar","obedecer","objetar","observar","obtener","ofender","ofrecer","abrir","ordenar","pedir",
"inundar","adeudar","empaquetar","pintar","estacionar","pasar","aprobar","pegar","acariciar","detenerse","pedalear","pelar","echando","ojear","ejecutando","actuando","llamar","llamando","recoger","levantar","planear",
"planificar","plantar","ubicar","colocar","tocar","complacer","conectar","señalar","lustrar","poseer","enviar","derramar","practicar","rezar","preceder","oren","orar","preferir","preparar","presentar","regalar",
"presionar","apretar","fingir","impedir","imprimir","programar","prometer","proteger","proveer","tirar","bombear","castigar","empujar","hacer","llover","levantar","alcanzar","darse","recibir","reconocer","grabar",
"reducir","reflejar","rechazar","lamentarse","relajarse","soltar","confiar","permanecer","recordar","acordarse","eliminar","alquilar","reparar","repetir","reemplazar","responder","informar","reproducer","solicitar",
"rescatar","jubilarse","regresar","rimar","enjuagar","arriesgar","robar","remar","frotar","arruinar","regir","dominar","despedir","navegar","satisfacer","salvar","ahorrar","guardar","gritar","atornillar","sellar",
"buscar","separar","servir","establecer","compartir","afeitarse","proteger","resguardar","comprar","suspirar","firmar","hacer","pecar","esquiar","saltearse","deslizarse","disminuir","oler","sonreír","fumar","estornudar",
"roncar","nevar","empapar","sonar","deletrear","derramar","malcriar","estropear","vaporizar","arrancar","comenzar","quedarse","permanecer","pararse","detenerse","almacenar","estirar","estudiar","tener","sufrir","sugerir",
"proveer","apoyar","suponer","sorprender","rodear","sospechar","colgar","cambiar","enchufar","conversar","saborear","tomar","chinchar","llamar","tentar","comprobar","agradecer","tildar","marcar","atar","dar","proponer",
"tocar","remolcar","comerciar","negociar","entrenar","transportar","viajar","temblar","confiar","tratar","intentar","volver","girar","doblar","escribir","unificar","usar","desaparecer","visitar","esperar","caminar",
"querer","advertir","lavar","gastar","desperdiciar","vigilar","pesar","agradecer","susurrar","silbar","limpiar","secar","desear","imaginarse","preguntarse","trabajar","preocuparse","bostezar","gritar","ceder","acercar"]
@app.route('/Verbo')
def clasificacion_De_Verbo():
    for subdir, dirs, files in os.walk(directory):
        bibTXT = open(os.path.join(subdir, "ReinaValera1960.txt"), 'r')
        leeBiblia = bibTXT.read().__str__()

    InterVerbTxt = re.findall(r"(?=(" + '|'.join(pronombresComunes) + r"))", leeBiblia)
    for word in InterVerbTxt:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()
    for words in frequency_list:
        print(words, frequency[words])

    return "El detalle de la cantidad de verbos en todo el texto se ensena en consola"

sustantivosComunes = []
@app.route('/Sustantivo')
def clasificacion_De_Sustantivo():
 return "El detalle de la cantidad de sustantivos en todo el texto se ensena en consola"


if __name__ == '__main__':
    app.run(port=5000, debug=True)