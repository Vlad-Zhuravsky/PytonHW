rus_dict = {"One": "Один", "Two": "Два", "Three": "Три"}
with open('ex4t.txt', 'w', encoding='utf-8') as f:
    with open ('ex4.txt', 'w', encoding='utf-8') as ft:
        f.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in ft]))