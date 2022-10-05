import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import *
from fastapi import UploadFile
from models import EpubInfo
import base64

download('stopwords')

stop_words = stopwords.words('spanish')
newStopWordsES = ["0","1","2","3","4","5","6","7","8","9","_","a","actualmente","acuerdo","adelante","ademas","además","adrede","afirmó","agregó","ahi","ahora","ahí","al","algo","alguna","algunas","alguno","algunos","algún","alli","allí","alrededor","ambos","ampleamos","antano","antaño","ante","anterior","antes", "año", "años","apenas","aproximadamente","aquel","aquella","aquellas","aquello","aquellos","aqui","aquél","aquélla","aquéllas","aquéllos","aquí","arriba","arribaabajo","aseguró","asi","así","atras","aun","aunque","ayer","añadió","aún","b","bajo","bastante","bien","breve","buen","buena","buenas","bueno","buenos","c","cada","casi","cerca","cierta","ciertas","cierto","ciertos","cinco","claro","comentó","como","con","conmigo","conocer","conseguimos","conseguir","considera","consideró","consigo","consigue","consiguen","consigues","contigo","contra","cosas","creo","cual","cuales","cualquier","cuando","cuanta","cuantas","cuanto","cuantos","cuatro","cuenta","cuál","cuáles","cuándo","cuánta","cuántas","cuánto","cuántos","cómo","d","da","dado","dan","dar","de","debajo","debe","deben","debido","decir","dejó","del","delante","demasiado","demás","dentro","deprisa","desde","despacio","despues","después","detras","detrás","dia","dias","dice","dicen","dicho","dieron","diferente","diferentes","dijeron","dijo","dio","donde","dos","durante","día","días","dónde","e","ejemplo","el","ella","ellas","ello","ellos","embargo","empleais","emplean","emplear","empleas","empleo","en","encima","encuentra","enfrente","enseguida","entonces","entre","era","erais","eramos","eran","eras","eres","es","esa","esas","ese","eso","esos","esta","estaba","estabais","estaban","estabas","estad","estada","estadas","estado","estados","estais","estamos","estan","estando","estar","estaremos","estará","estarán","estarás","estaré","estaréis","estaría","estaríais","estaríamos","estarían","estarías","estas","este","estemos","esto","estos","estoy","estuve","estuviera","estuvierais","estuvieran","estuvieras","estuvieron","estuviese","estuvieseis","estuviesen","estuvieses","estuvimos","estuviste","estuvisteis","estuviéramos","estuviésemos","estuvo","está","estábamos","estáis","están","estás","esté","estéis","estén","estés","ex","excepto","existe","existen","explicó","expresó","f","fin","final","fue","fuera","fuerais","fueran","fueras","fueron","fuese","fueseis","fuesen","fueses","fui","fuimos","fuiste","fuisteis","fuéramos","fuésemos","g","general","gran","grandes","gueno","h","ha","haber","habia","habida","habidas","habido","habidos","habiendo","habla","hablan","habremos","habrá","habrán","habrás","habré","habréis","habría","habríais","habríamos","habrían","habrías","habéis","había","habíais","habíamos","habían","habías","hace","haceis","hacemos","hacen","hacer","hacerlo","haces","hacia","haciendo","hago","han","has","hasta","hay","haya","hayamos","hayan","hayas","hayáis","he","hecho","hemos","hicieron","hizo","horas","hoy","hube","hubiera","hubierais","hubieran","hubieras","hubieron","hubiese","hubieseis","hubiesen","hubieses","hubimos","hubiste","hubisteis","hubiéramos","hubiésemos","hubo","i","igual","incluso","indicó","informo","informó","intenta","intentais","intentamos","intentan","intentar","intentas","intento","ir","j","junto","k","l","la","lado","largo","las","le","lejos","les","llegó","lleva","llevar","lo","los","luego","lugar","m","mal","manera","manifestó","mas","mayor","me","mediante","medio","mejor","mencionó","menos","menudo","mi","mia","mias","mientras","mio","mios","mis","misma","mismas","mismo","mismos","modo","momento","mucha","muchas","mucho","muchos","muy","más","mí","mía","mías","mío","míos","n","nada","nadie","ni","ninguna","ningunas","ninguno","ningunos","ningún","no","nos","nosotras","nosotros","nuestra","nuestras","nuestro","nuestros","nueva","nuevas","nuevo","nuevos","nunca","o","ocho","os","otra","otras","otro","otros","p","pais","para","parece","parte","partir","pasada","pasado","paìs","peor","pero","pesar","poca","pocas","poco","pocos","podeis","podemos","poder","podria","podriais","podriamos","podrian","podrias","podrá","podrán","podría","podrían","poner","por","por qué","porque","posible","primer","primera","primero","primeros","principalmente","pronto","propia","propias","propio","propios","proximo","próximo","próximos","pudo","pueda","puede","pueden","puedo","pues","q","qeu","que","quedó","queremos","quien","quienes","quiere","quiza","quizas","quizá","quizás","quién","quiénes","qué","r","raras","realizado","realizar","realizó","repente","respecto","s","sabe","sabeis","sabemos","saben","saber","sabes","sal","salvo","se","sea","seamos","sean","seas","segun","segunda","segundo","según","seis","ser","sera","seremos","será","serán","serás","seré","seréis","sería","seríais","seríamos","serían","serías","seáis","señaló","si","sido","siempre","siendo","siete","sigue","siguiente","sin","sino","sobre","sois","sola","solamente","solas","solo","solos","somos","son","soy","soyos","su","supuesto","sus","suya","suyas","suyo","suyos","sé","sí","sólo","t","tal","tambien","también","tampoco","tan","tanto","tarde","te","temprano","tendremos","tendrá","tendrán","tendrás","tendré","tendréis","tendría","tendríais","tendríamos","tendrían","tendrías","tened","teneis","tenemos","tener","tenga","tengamos","tengan","tengas","tengo","tengáis","tenida","tenidas","tenido","tenidos","teniendo","tenéis","tenía","teníais","teníamos","tenían","tenías","tercera","ti","tiempo","tiene","tienen","tienes","toda","todas","todavia","todavía","todo","todos","total","trabaja","trabajais","trabajamos","trabajan","trabajar","trabajas","trabajo","tras","trata","través","tres","tu","tus","tuve","tuviera","tuvierais","tuvieran","tuvieras","tuvieron","tuviese","tuvieseis","tuviesen","tuvieses","tuvimos","tuviste","tuvisteis","tuviéramos","tuviésemos","tuvo","tuya","tuyas","tuyo","tuyos","tú","u","ultimo","un","una","unas","uno","unos","usa","usais","usamos","usan","usar","usas","uso","usted","ustedes","v","va","vais","valor","vamos","van","varias","varios","vaya","veces","ver","verdad","verdadera","verdadero","vez","vosotras","vosotros","voy","vuestra","vuestras","vuestro","vuestros","w","x","y","ya","yo","z","él","éramos","ésa","ésas","ése","ésos","ésta","éstas","éste","éstos","última","últimas","último","últimos"]
stop_words.extend(newStopWordsES)

def clearText(text):
    # word_tokens = word_tokenize(unidecode.unidecode(text.lower())) 
    word_tokens = word_tokenize(text.lower()) 
    word_tokens = [w for w in word_tokens if w.isalpha() or w.isnumeric()]
    word_tokens = [w for w in word_tokens if not w.lower() in stop_words]
    # word_tokens = [PorterStemmer().stem(w) for w in word_tokens]
    
    return word_tokens

def readEpub(file: UploadFile) -> epub.EpubBook: 
    contents = file.file.read() 
    with open(file.filename, 'wb') as f:
        f.write(contents)
        f.close()        
    book = epub.read_epub(file.filename)
    os.remove(file.filename)
    
    return book

def chapter_to_str(book):
    text = ''
    
    for chapter in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
        text+=(' '.join([para.get_text() for para in soup.find_all('p')]))    
    
    return text

def most_common(tokens, number = 23):
    fdist = FreqDist(tokens)
    
    return fdist.most_common(number)

def word_most_common(book, number):
    text = chapter_to_str(book)
    word_tokens = clearText(text) 

    return most_common(word_tokens, number)

def bigrams_most_common(book, number):
    text = chapter_to_str(book)
    word_tokens = clearText(text) 
    bgs = bigrams(word_tokens)
    
    return most_common(bgs, number)

def tigrams_most_common(book, number):
    text = chapter_to_str(book)
    word_tokens = clearText(text) 
    tbgs = trigrams(word_tokens)
    
    return most_common(tbgs, number)

def info(book: epub.EpubBook):
    image = None
    
    for item in book.get_items_of_type(ebooklib.ITEM_IMAGE):
        if item.get_name() == 'Images/cover.jpg':
            # image = io.BytesIO(item.get_content())
            # Image.open(io.BytesIO(image.get_content())).show()
            image = base64.b64encode(item.get_content()).decode()

    title = book.get_metadata('DC', 'title')[0][0] if len(book.get_metadata('DC', 'title')) > 0 else None
    creator = book.get_metadata('DC', 'creator')[0][0] if len(book.get_metadata('DC', 'creator')) > 0 else None
    identifier = book.get_metadata('DC', 'identifier')[0][0] if len(book.get_metadata('DC', 'identifier')) > 0 else None
    contributor = book.get_metadata('DC', 'contributor')[0][0] if len(book.get_metadata('DC', 'contributor')) > 0 else None
    rights = book.get_metadata('DC', 'rights')[0][0] if len(book.get_metadata('DC', 'rights')) > 0 else None
    coverage = book.get_metadata('DC', 'coverage')[0][0] if len(book.get_metadata('DC', 'coverage')) > 0 else None
    date = book.get_metadata('DC', 'date')[0][0] if len(book.get_metadata('DC', 'date')) > 0 else None
    description = book.get_metadata('DC', 'description')[0][0] if len(book.get_metadata('DC', 'description')) > 0 else None
    
    return EpubInfo(title, creator, identifier, contributor, rights, coverage, date, description, image)