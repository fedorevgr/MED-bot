import speech_recognition as sr
import re
from fuzzywuzzy import fuzz

r = sr.Recognizer()
with sr.AudioFile("C:\ST\ecord.wav") as source:  # Microphone
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="ru-RU")
    except:
        print("Извините я не понял что вы сказали")

symptomps = ['зуд', 'кожная сыпь', 'узловые кожные высыпания', 'постоянное чихание', 'озноб', 'боль в суставах',
             'боль в животе', 'кислотность', 'язвы на языке', 'атрофия мышц', 'рвота', 'жжение при мочеиспускании',
             'мажущие выделения при мочеиспускании', 'утомляемость', 'увеличение веса', 'тревога',
             'холодные руки и ноги',
             'перепады настроения', 'потеря веса', 'беспокойство', 'вялость', 'комочки в горле',
             'нерегулярный уровень сахара',
             'кашель', 'высокая температура', 'запавшие глаза', 'одышка', 'потливость', 'обезвоживание',
             'расстройство желудка',
             'головная боль', 'желтоватая кожа', 'темная моча', 'тошнота', 'потеря аппетита', 'боль за глазами',
             'боль в спине',
             'запор', 'боль в животе', 'диарея', 'легкая лихорадка', 'желтая моча', 'пожелтение глаз',
             'острая печеночная недостаточность', 'много жидкости',
             'вздутие живота', 'увеличение лимфатических узлов', 'недомогание', 'нечеткое и искаженное зрение',
             'мокрота', 'раздражение горла', 'покраснение глаз',
             'синусовое давление', 'насморк', 'заложенность носа', 'боль в груди', 'слабость в конечностях',
             'учащенное сердцебиение', 'боль при дефекации',
             'боль в анальной области', 'кровавый стул', 'раздражение в анусе', 'боль в шее', 'головокружение',
             'судороги', 'кровоподтеки', 'ожирение', 'опухшие ноги',
             'опухшие кровеносные сосуды', 'одутловатое лицо и глаза', 'увеличенная щитовидная железа',
             'ломкость ногтей', 'опухшие конечности', 'чрезмерный голод',
             'внебрачные контакты', 'сухость и покалывание губ', 'невнятная речь', 'боль в коленях',
             'боль в тазобедренных суставах', 'мышечная слабость',
             'ригидность затылочных мышц', 'припухлость суставов', 'скованность движений', 'вращательные движения',
             'потеря равновесия', 'неустойчивость',
             'слабость с одной стороны тела', 'потеря обоняния', 'дискомфорт в мочевом пузыре', 'неприятный запах мочи',
             'постоянное ощущение мочи', 'отхождение газов',
             'внутренний зуд', 'токсический вид', 'депрессия', 'раздражительность', 'мышечная боль',
             'измененная чувствительность', 'красные пятна на теле', 'боль в животе',
             'аномальные менструации', 'дисхромия', 'пятна', 'слезотечение', 'повышенный аппетит', 'полиурия',
             'анамнез', 'слизистая мокрота', 'ржавая мокрота',
             'отсутствие концентрации внимания', 'нарушения зрения', 'переливание крови',
             'получение нестерильных инъекций', 'кома', 'желудочное кровотечение', 'вздутие живота',
             'употребление алкоголя в анамнезе', 'обезвоживание', 'кровь в мокроте', 'выступающие вены на икрах',
             'учащенное сердцебиение', 'болезненная ходьба', 'гнойные прыщи',
             'угри', 'судороги', 'шелушение кожи', 'серебристый налет', 'небольшие вмятины на ногтях',
             'воспаленные ногти', 'волдыри', 'красные раны вокруг носа', 'желтая корка']


def to_normal_text(text):
    return re.findall(r'[^\w\s]+|\w+', text)


def find_same_words(text, symptomps):
    patient_symptoms = []
    for symptom in symptomps:
        for word in text:
            if fuzz.ratio(symptom, word) > 70:
                patient_symptoms.append(symptom)
    return patient_symptoms


text = to_normal_text(text)
print(text)
print(find_same_words(text, symptomps))
