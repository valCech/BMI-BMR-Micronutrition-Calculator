vlastimil
#8827

LorDury — Today at 10:04
print("Welcome to BMI app that will help you to calculate your BMI index. Let's begin!")
height = float(input("What is your height in meters? "))
weight = float(input("what is your weight in kg? "))
BMI = weight / height**2
BMI1 = "{:.2f}".format(BMI)

Expand
BMI_index.py
1 KB
print("Hello, and welcome to this roller coaster app. You must be over 87cm high to pass through the gate.")
Height = int(input("What is your height in cm?\n"))
bill = 0

if Height >= 87:
    print("Enjoy your ride on our roller coaster :)")
Expand
Horska_draha.py
1 KB
print("This app is to help you to split your bill for hospitality.\n")
bill = int(input("How much is your restaurant bill?\n"))
percent = int(input("How much percent would you like to tip them?\n"))
people = int(input("How many people share the bill?\n"))
calctip = bill * (percent * 0.01)
fairshare = (calctip + bill) / people
Expand
Kalkukalacka.py
1 KB
userage = int(input("How old are you?\n"))
maxage = int(90)
years = int(maxage) - int(userage)
days = 365 * int(maxage) - 365 * int(userage)
hours = int(days) * 24
print(f"rest of your estimated life is {years} years \n or {days} days \n or {hours} hours.")
Expand
maxage90.py
1 KB
Tohle jsem nejak udelal zatim. Ale na tu hru chci pouzit ten druhej koncept
Roller coaster
S funkci IF, elif, else
vlastimil — Today at 10:07
a jak vyzkousis jestli to funguje?
LorDury — Today at 10:07
Pak do toho dat nejakjy random generatory, jako treba hazeni kostkou nebo vypocet nejake sance etc a pribeh mutanta muze zacit.
LorDury — 28/07/2022
bud v nejakym tom kodovaci nebo primo v pythonu, ale to by v kodu na konci muselo by napsano print("any key to continue")
Da se tu nejak sdilet obrazovka ?D
vlastimil — Today at 10:09
ja kdyz delam js tak to napijim na html code k tomu vytvoreny a muzu rovnou videt jak to pracuje.
nejak podobne to musi jit i s pythonem. nekam integrovat i videt jak to slape
LorDury — 28/07/2022
jde, ve VS code
a enbo v pycharm
nevim jak v IDLE
muzu ti zavolat?
vlastimil — Today at 10:11
kde muzes dat hodnoty do variables? treba u toho restaurant billu
volej
LorDury
 started a call that lasted an hour.
 — 28/07/2022
vlastimil — 28/07/2022
type()
typeOf()
len
lentgth
length
Clyde
BOT
 — 28/07/2022
It appears you've been by yourself in this call for more than five minutes. The bandwidth patrol has asked me to disconnect you to save bandwidth. That stuff doesn't grow on trees!
Only you can see this • Dismiss message
LorDury — 28/07/2022
print("Welcome to BMI app that will help you to calculate your BMI index. Let's begin!")
height = float(input("What is your height in meters? "))
weight = float(input("what is your weight in kg? "))
BMI = weight / height**2
BMI1 = round(BMI, 1)
print(f"Your BMI is {BMI1}")
if BMI1 <= 18.5:
    print("Underweight\nEat something you skinny addvert on hunger!")
elif BMI1 <= 24.9:
    print("Normal\nFinaly someone normal.")
elif BMI1 <= 29.9:
    print("Overweight\nSlow down that workout on your beerceps!")
elif BMI1 <= 34.9:
    print("Obese\nYou are fat bitch!")
else:
    print("System overload!!!\nSelf destruction 3, 2, 1......")
input("Have a nice day!")
LorDury — 28/07/2022
print('''
               888                                          888    
                888                                          888    
                888                                          888    
 8888b. .d8888b 888888888d888 .d88b. 88888b.  8888b. 888  888888888 
    "88b88K     888   888P"  d88""88b888 "88b    "88b888  888888    
Expand
Game.py
10 KB
tak jsem udelal svoji prvni hru 😄
vlastimil — Today at 17:32
ja jsem dneska udelal vypocet micronutrition. jako zaklad jsem pouzil tvuj bmi. znalosti z js se mi tu hodili. Chce to uz jen doupravit vizualne, jako mezeri ci radky. Mrkni na to a navrhni upravy. prosim nesdilet, pouziju to na svoje portfolio
https://github.com/valCech/BMI-Micronutrition-Calculator 
LorDury — Today at 18:12
Dobry a hezky. Chce to debugovat
LorDury — Today at 18:28
Opravene posilam zpatky
#Diet & Micronutrition calculation
#Base_input
print("Welcome to Val's Micronutrition Calculator")
input("Press enter to start")
height = float(input("What is your height in centimetres?\n"))
weight = float(input("What is your weight in kg?\n"))
Expand
MicroBRONutri.py
3 KB
vlastimil
 started a call.
 — Today at 18:32
﻿
#Diet & Micronutrition calculation
#Base_input
print("Welcome to Val's Micronutrition Calculator")
input("Press enter to start")
height = float(input("What is your height in centimetres?\n"))
weight = float(input("What is your weight in kg?\n"))
age = float(input('What is your age?\n'))
gender = input('If you are man type m otherwise type w\n').upper()
name = str(input('What is your name?\n')).capitalize()
#BMI_calculation
diet_calories_m = str(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age) *1.55)
diet_calories_w = str(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age) *1.55)
#Micro_man
protein_m = float(diet_calories_m) * .5 / 4
protein_m = format(protein_m, ".2f")
protein_m = str(protein_m)
carbs_m = float(diet_calories_m) * .25 / 4
carbs_m = format(carbs_m, ".2f")
carbs_m = str(carbs_m)
fat_m = float(diet_calories_m) * .25 / 4
fat_m = format(fat_m, ".2f")
fat_m = str(fat_m)
diet_calories_m = float(diet_calories_m) - 300
diet_calories_m = format(diet_calories_m, ".2f")
diet_calories_m = str(diet_calories_m)
#macro_woman
protein_w = float(diet_calories_m) * .5 / 4
protein_w = format(protein_w, ".2f")
protein_w = str(protein_w)
carbs_w = float(diet_calories_m) * .25 / 4
carbs_w = format(carbs_w, ".2f")
carbs_w = str(carbs_w)
fat_w = float(diet_calories_m) * .25 / 4
fat_w = format(fat_w, ".2f")
fat_w = str(fat_w)
diet_calories_w = float(diet_calories_w) - 250
diet_calories_w = format(diet_calories_w, ".2f")
diet_calories_w = str(diet_calories_w)
#Gender_choice_and_results
if gender == "M":
  print("Hallo " + name + ',' +'\nYour daily calorie intake should be ' + diet_calories_m + 'cal\n'
       'You need to lower your overall intake calories by 300cal\n' 
       'But dont worry, I have already done it for you\n')
  print('Here is your micronutrient ratio:\n' + 'Protein:' + protein_m + 'g\n'
       'Carbohydrates: ' + carbs_m + 'g\n'
       'Fat: ' + fat_m + 'g')
elif gender == "W":
  print('Hallo ' + name +',\nYour daily calorie intake should be ' + diet_calories_w + 'cal\n'
       'You also need to lower your overall intake calories by 250cal\n' 
       'But dont worry, I have already done it for you\n')
  print('Your micronutrient ratio per day is:\n' + 'Protein:' + protein_w + 'g\n'
        'Carbohydrates: ' + carbs_w + 'g\n'
        'Fat: ' + fat_w + 'g')
else:
      print("Too heavy fingers or never typed before? Try it again and focus!")
input('Made with love by Val')
MicroBRONutri.py
3 KB
