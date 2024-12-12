import re
import csv # Модуль csv предоставляет функционал для работы с CSV-файлами.
           # Он позволяет читать и записывать данные в формате CSV.
import urllib.request # Модуль urllib.request предоставляет функциональность для открытия URL-адресов и обработки
                     # HTTP-запросов. Он позволяет получать содержимое веб-страниц, отправлять данные на серверы и
                     # выполнять другие действия, связанные с HTTP.


url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
response = urllib.request.urlopen(url)
html_content = response.read().decode()
#print(html_content)
pattern = r"(?:-link\">)(?P<name>[^<]+)(?:[^o]*[^l]*.*\n *)(?P<address>[^\n]+)(?:\s*.*>\s*.*>\s*.*>\s*<d[^>]*>\s*.*\s*.*>(?P<phone>[^<]+).*>\s*</dl>)?(?:\s*<.*>\s*<.*\s*<.*>(?P<workhours>[^<]+)</dd>)?"

match = re.findall(pattern, html_content)
# Запись полученных данных в csv-файл
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Адрес', 'Телефон', 'Рабочие часы'])

    for i in match:
        writer.writerow(i)

# 4. Вывод информации по именованным группам:

matches = re.finditer(pattern, html_content)

for match in matches:
    print("Название:", match.group('name'))
    print("Адрес:", match.group('address'))
    print("Телефон:", match.group('phone'))
    print("Рабочие часы:", match.group('workhours'))
    print("\n")

if not re.search(pattern, html_content):
    print("No match found.")

# В этой версии кода `re.finditer` используется для поиска итераций,
# затем цикл `for` выводит содержимое каждой группы для каждого вхождения.
# Если соответствие не найдено, выводится сообщение "No match found.".