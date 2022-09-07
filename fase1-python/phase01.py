#name Rodrigo Tadeu Alves de Moura
#RM RM97330

#Cap 07 - Advanced algorithm and flowchart concepts for logic in decision making

year = float(input("Time as a smoker...."))
price = float(input("Value of cigarette pack...."))
quantity = float(input("number of cigarettes per day...."))

value = (((year * 365) * price) * quantity)

if value <= 20000:
     print("With the value of {}, you could buy a bike vruummm".format(value))
elif value <= 20000 and value <= 50000:
     print("With the value of {}, you could buy a beautiful motorcycle".format(value))
else:
     print("With the value of {}, you could buy a nice car".format(value))

