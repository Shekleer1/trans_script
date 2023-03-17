from googletrans import Translator


translator=Translator()


with open(file='C:\\Users\\Shekleer\\Desktop\\вспомогательный софт и эмуляторы)\\Anki\\TXT_from.txt', mode='r') as file1:

    text=file1.read()
    newList=[]
    processed_text = text.replace('\n',' ')
    processed_text = processed_text.replace('-',' ')
    processed_text = processed_text.replace('das', ' ')
    processed_text = processed_text.replace('die', ' ')
    processed_text = processed_text.replace('der', ' ')
    processed_text = processed_text.replace('ist', ' ')
    processed_text = processed_text.replace('"', ' ')
    processed_text = processed_text.replace('/',' ').split(sep=' ')
    for word in processed_text:
        try:
            if word[-1] == '\n':
                newList.append(word[:-1])
            elif word[-1] == ',':
                newList.append(word[:-1])
            elif word[-1] == '/':
                newList.append(word[:-1])
            elif word[-1] == '.':
                newList.append(word[:-1])
            else:
                newList.append(word)
        except IndexError:
            pass

with open(file='C:\\Users\\Shekleer\\Desktop\\вспомогательный софт и эмуляторы)\\Anki\\TXT_in.txt', mode='w') as file2:
    for each in newList:
        translation = translator.translate(each, dest='ru')
        file2.write(f"{each} --- {translation.text}\n")












