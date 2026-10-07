age = "19"
print(age)


convocation_list = ["Davido", "Burna", "Rema", "Baddo"]

def avg(a, b):
    print((a + b) /2)
    
def average(a, b):
    print("calculating......")
    return (a + b) /2
    
print(avg(10, 20))
print(average(20, 30))

final_score = (average(20, 90) * 2) - average(10, 20)
print(final_score)

def greet(alias):
    print("congratulation to you, my dear" + alias)
    
    
for name in convocation_list:
    greet(name)
    greet(name)
    greet(name)
    print("moving to the next great artist")
    
    
time = 10
if time <= 9:
    print("eat bread")
elif time >= 12 and time <= 15:
    print("jollof")
elif time >= 19 and time <= 22:
    print("groceries and floating barries")
else:
    print("starving and fasting")
    
    
    
    
food = input("Enter a food you like (q to quit):")

while not food == "q":
    print(f"you like {food}")
        
    food = input("Enter another food you like (q to quit):")

print("bye")




num = int(input("Enter a # between 1 - 10:"))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10:"))
    
print(f'your number is {num}')



scores = [8, 90, 60, 73, 28, 73, 94, 95, 82, 48, 92, 39, 48, 29, 38, 40, 39,39, 54, 59]
for score in scores:
    # print(score)
    
        

    if score >=70 and score <95:
     print(f'{score} - A')
    if score >=60 and score <70:
       print(f'{score} - B')
    if score >=50 and score <60:
      print(f'{score} - c')
    if score >=45 and score <50:
     print(f'{score} - D')
    if score >=40 and score <44:
        print(f'{score} - E')
    if score >=8 and score <39:
       print(f'{score} - F')


input("what is your problem joshua?")
joshua = input("continue")
print(joshua)

