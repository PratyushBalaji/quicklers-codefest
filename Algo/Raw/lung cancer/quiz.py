from short import *

questions = ["Do you smoke?",'Do you have yellow fingers?','Do you suffer from anxiety?','Are you facing peer pressure in social environments?','Do you have any chronic diseases?','Do you frequently feel fatigued?','Do you have allergies?','Do you suffer from wheezing?','Do you drink alcohol?','Do you often have unprovoked coughs?','Do you have shortness of breath?','Do you have trouble swallowing?','Do you have chest pain?']
arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x = input('are you male?')
if x[0].lower() == 'y':
    arr[0] += 1

x = int(input('how old are you?'))
arr[1] == x

for i in range(len(questions)):
    x = input(questions[i]+' : ')
    if x[0].lower() == 'y':
        arr[i+2] += 1
    else:
        continue

num = pred(arr)
if num[0] == 1:
    print("you might have cancer")
else:
    print("you probably dont have cancer")



# GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,
# WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN