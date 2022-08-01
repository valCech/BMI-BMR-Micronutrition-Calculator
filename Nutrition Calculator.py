
#BMI, BMR & Micronutrition calculation
#Base_input
print("Welcome to Val's Micronutrition Calculator")
input("Press enter to start")
height = float(input("What is your height in centimetres?\n"))
weight = float(input("What is your weight in kg?\n"))
age = float(input('What is your age?\n'))
gender = input('If you are man type m otherwise type w\n').upper()
name = str(input('What is your name?\n')).capitalize()
#BMI_(Body Mass Index)
BMI = weight / ((height/100)**2)
BMI1 = round(BMI, 1)
print(f"Your BMI is {BMI1}")
if BMI1 <= 18.5:
    print("Underweight\nEat something you skinny addvert on hunger!")
elif BMI1 <= 24.9:
    print("Normal\nTime to shape it up.")
elif BMI1 <= 29.9:
    print("Overweight\nYou need to follow this diet!")
elif BMI1 <= 34.9:
    print("Obese\nDiet should be your second name from now on!")
else:
    print("System overload!!!\nSelf destruction 3, 2, 1......")
input("Press enter for your micronutrition plan!\n")
#BMR_calculation_(Basal Metabolic Rate)
diet_calories_m = str(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age) *1.55)
diet_calories_w = str(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age) *1.55)
#Macronutrients_man
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
#macronutrients_woman
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
  print("Here we go " + name + ',' +'\nYour daily calorie intake should be ' + diet_calories_m + 'cal\n'
       'You need to lower your overall intake calories by 300cal\n' 
       "But don't worry, I have done it for you :)\n")
  print('Here is your daily micronutrient ratio:\n' + 'Protein:' + protein_m + 'g\n'
       'Carbohydrates: ' + carbs_m + 'g\n'
       'Fat: ' + fat_m + 'g')
elif gender == "W":
  print('Hallo ' + name +',\nYour daily calorie intake should be ' + diet_calories_w + 'cal\n'
       'You also need to lower your overall intake calories by 250cal\n' 
       "But don't worry, I have done it for you :)\n")
  print('Here is your daily micronutrient ratio:\n' + 'Protein:' + protein_w + 'g\n'
        'Carbohydrates: ' + carbs_w + 'g\n'
        'Fat: ' + fat_w + 'g')
else:
      print("Too heavy fingers or never typed before? Try it again and focus!")
input('Made with love by Val')

