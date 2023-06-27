from translate import Translator

translator = Translator(to_lang="es")  #Spanish

try:
    with open('./TranslateMe.txt', 'r') as myFile:
        text = myFile.read()
        translation = translator.translate(text)
        print(translation)

except FileNotFoundError as error:
    print(error.message)