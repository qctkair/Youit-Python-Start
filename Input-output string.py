# str - строки
string1 = str()  # string1 = ""
string2 = "it is string"  # 'it is string'
string3 = string2
print(string1, f"({type(string1)}),", string2, f"({type(string2)}),", string3, f"({type(string3)})")

print('it is "comfortable"')
# print("it is "comfortable"") нельзя так
# print('it is 'comfortable'') тоже нельзя так

bigString = """it is a big,
very big
string""" # или в одинарных ковычках ('''something''')
print(bigString)

string4 = string2 + string3  # склеивает строки string1 и string2, в прямом смысле складываем
print(string4)

# а что если мы хотим число преобразовать в строку?
integer = 873
string5 = str(integer)  # что-то напоминает...
integer = int(string5)
print(string5, integer)

# в Python (и не только в нем) существуют специальные символы - '\n' (перевод строки), '\t' (табуляция = 4 пробела)
print("it is first line\n\tit is second line")


# как отличить специальный символ от части строки?
# - с помощью дублирования обратной косой черты '\\'
print("\\n")
# - с помощью так называемых raw strings (сырые строки)
print(r"\n")
# на самом деле кавычки, которые ограничивают строку, - тоже специальные символы (они же нужны, чтобы интерпретатор понял, где начинается строка, а где заканчивается)
# значит мы можем их также использовать с помощью '\\'!
print("\"smth important\"")
# а вот с помощью raw strings нельзя :(
# print(r"smth "very" important") - нельзя. не сработает.

# все это называется экранированием - способ предотвращения интерпретации специальных символов в строках


# по умолчанию print(), разделяет элементы вывода пробелами
print("it is string", 57)

# но мы можем сами выбрать, чем хотим разделять с помощью метода sep (separator)
print("it is string", 57, sep=", ")
print("it is string", 57, sep="\n")
print("it is string", 57, sep="\t")
print("it is string", 57, sep=" ")  # default

# а закнчивается print(), по умолчанию, переводом строки
print("it is first line")
print("it is second line")

# это тоже мы можем настраивать под себя с помощью метода end
print("it is first line", end=" ")
print("it is first line too", end="\n")  # по умолчанию
print("it is second line")


# кстати строки можно использовать как комментарии. мы их никуда не сохраняем (на самом деле "под капотом" строка создается, и так как мы ее не используем, удаляется - временная переменная)
"comment"
"""it is a big,
   very
   big comment"""