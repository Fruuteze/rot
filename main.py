#input()
name = input ("Введите имя: ")
print(f"Привет ,{name}!")

#input() > int
age_str = input ("Введите ваш возраст:")
age = int(age_str)

print(age)
print(age_str)

#input() > float
weight = float(input("Укажите рост (см)"))

t(weight)
t(type(weight))

#input() > bool
input:bool(1)
output: True

input:bool(0)
output:False

input:bool(True)
output:True

input:bool([1, 2, 3])
output:True

input:bool([])
output:False

#input() > str
str(object='')
str(object=b'', encoding='utf-8', errors='strict')

#input() > complex

c = complex(1, 1) print(c)

c = complex(1.5, -2.1) print(c)

c = complex(0xF) # hexadecimal print(c)

c = complex(0b1010, -1) # binary print(c)