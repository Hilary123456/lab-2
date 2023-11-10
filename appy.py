import csv
import random
import xml.dom.minidom as minidom

# 1. Записи, у которых поле «Название» длиннее 30 символов.

with open('books-en.csv', 'r') as file:
    data = csv.reader(file, delimiter=';')
    for data in list(data):
        if len(data[1]) > 30:
            print(data[1])

# 2. Поиск книг по автору
flag = 0
search = input('search authors: ')

price_limit = 149.99

with open('books-en.csv', 'r') as file:
    data = csv.reader(file, delimiter=';')

    for row in data:
        Price_tag = row[6]
        try: 
            if float(Price_tag) > price_limit:
                author_column = row[2].lower()
                search_file = author_column.find(search.lower())
                if search_file != -1:
                    print(row[2])
                    flag = 1
        except ValueError:
            continue 
if flag == 0:
    print('Nothing found!')

# 3. Библиографическая ссылка Генератор
with open('books-en.csv', 'r') as books_data:
    data = list(csv.reader(books_data, delimiter=';'))

random_entries = random.sample(data[1:], 20)

references = []
for i, entry in enumerate(random_entries, start=1):
    author = entry[2]
    title = entry[1]
    year = entry[3]
    reference = f"{author}. {title} - {year}"
    references.append(reference)

with open('bibliography_file.txt', 'w') as outfile:
    for i, reference in enumerate(references, start=1):
        outfile.write(f"{i}. {reference}\n")

print("Bibliographic referencesnsaved to 'bibliography_file.txt'.")



# 4. «Средний показатель Value»
xml_doc = minidom.parse('currency.xml')
valute_elements = xml_doc.getElementsByTagName('Valute')
total_value = 0
count = 0

for valute in valute_elements:
    value_text = valute.getElementsByTagName('Value')[0].firstChild.data
    value = float(value_text.replace(',', '.'))
    total_value += value
    count += 1
average_value = total_value / count

print("Средний показатель Value:", average_value)



# 5. Все теги без повторов
with open('currency.xml', 'r') as currency_file:
    file = currency_file.read()
    dom = minidom.parseString(file)

    elements = dom.getElementsByTagName('*')
    unique_tags = set()
    for element in elements:
        unique_tags.add(element.tagName)
    for tag in unique_tags:
        print(tag)

# 6. Все издательства без повторов
unique_publishers = set()
with open('books-en.csv', 'r') as books_data:
    data = list(csv.reader(books_data, delimiter=';'))
    for row in data:
        publishers = row[4]
        publisher_list = publishers.split(',')
        for publisher in publisher_list:
            unique_publishers.add(publisher.strip())
for publisher in unique_publishers:
    print(publisher)

# 7. 20 лучших книг
books = []
with open('books-en.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    next(reader)
    for row in reader:
        books.append(row)
sorted_books = sorted(books, key=lambda x: int(x['Downloads']), reverse=True)

top_20_books = sorted_books[:20]
for book in top_20_books:
    print(book)
