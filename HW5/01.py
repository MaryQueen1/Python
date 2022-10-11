# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

path = r'C:\Users\DRUNK_ELEPHANT\Desktop\Queen\Getting to know Python\HW5\old_text.txt'
path2 = r'C:\Users\DRUNK_ELEPHANT\Desktop\Queen\Getting to know Python\HW5\new_text.txt'

with open(path, 'r') as data:
    old_text = data.read()
    redact = old_text.split(' ')

with open(path2, 'w') as data2:
    words = [word for word in redact if not 'a' in word and not 'b' in word and not 'c' in word]
    new_text = ' '.join(words)
    data2.writelines(new_text)

print('Новый текст записался в файл new_text')

# РќРµ СѓРјРµР» СЏ РїСЂРёС‚РІРѕСЂСЏС‚СЊСЃСЏ, РќР° СЃРІСЏС‚РѕРіРѕ РїРѕС…РѕРґРёС‚СЊ
# Подскажите, пожалуйста, что это?
# Было на выводе в консоли, когда текст был на русском,
# и я выводила его отредактированный вариант в терминал
# (из-за этого пришлось прописать решение для английского текста)