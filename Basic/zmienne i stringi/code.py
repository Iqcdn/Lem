#1&2
#lubie placki

#3
#wyświetl tekst "John Cleese"
print("John Cleese")

#4
#wyswietl tekst "Monty Python's Flying Circus"
print("Monty Python\'s Flying Circus")

#5
#wyswietl wartość wyrażenia 1 + 2 + 3
print(1+2+3)

#6
#wyświetl pole powierzchni prostokąta o wymiarach 17 na 23
print(17*23)

#7
print(2.34*14)

#8
#wyświetl komunikat zgodny z trescią zadania
print("Koszt jednej parówki to:", 4.50/6.0, "PLN")

#9
#wyświetl komunikat zgodny z trescią zadania
print("Każde dziecko otrzyma",round(133/16),"parówek")

#10
#wyświetl komunikat zgodny z trescią zadania
print("Dla nauczyciela zostało",133%16 ,"parówek")

#11
price = 0.75
print("Parówka kosztuje:", price ,"PLN")
del price

#12
students = 16
print ("Na pikniku było", students, "uczniów")
del students

#13
text = "ave caesar!"
print(text.upper())
del text

#14
text = "MORITURI TE SALUTANT"
print(text.lower())
del text

#15
quote = "two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
print(quote.capitalize())
del quote

#16
some_title = "monty python's flying circus"
print(some_title.title())
del some_title

#17
some_text = "Mmmmm, xxx, yummy xxx, I love xxx!"
print (some_text.replace("xxx", "sausages"))
del some_text

#18
quote = "The hardest thing in the world to understand is the Income Tax."
print(quote.swapcase())
del quote

#19
quote = "     just a flesh wound.\n"
print(quote.strip())
del quote

#20
text1 = "monty"
text2 = "python"
print(text1+text2)
del text1, text2

#21
first_name = "clint"
last_name = "eastwood"
print(first_name.capitalize()+", "+last_name.capitalize())
del first_name, last_name

#22
text1 = "Ole! "
print(text1*10)
del text1

#23
nr1 = 123
nr2 = 456
nr3 = 789
print(nr1, nr2, nr3, sep = ".")
del nr1, nr2, nr3

#24
print("Black", end=" * ")
print("Knight")

#25
actor1 = "clint eastwood"
actor2 = "bee vang"
actor3 = "scott eastwood"
print("Gran Torino cast: ", end="")
print(actor1.title(), actor2.title(), actor3.title(), end=".", sep=", ")
del actor1, actor2, actor3