import logging
logging.basicConfig(level=logging.INFO)
dzialanie = (input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:"))
a = float((input("Podaj składnik 1 ")))
b = float((input("Podaj składnik 2 ")))

wynik = 0
if dzialanie == "1":
        logging.info("Dodaję %f i %f" %(a,b))
        wynik = a + b
elif dzialanie == "2":
        logging.info("Odejmuję %f i %f" %(a,b))
        wynik = a - b
elif dzialanie == "3":
        logging.info("Mnożę %f i %f" %(a,b))
        wynik = a * b
else:
        logging.info("Dzielę %f i %f" %(a,b))
        wynik = a / b
        
print("wynik to %f" %(wynik))
