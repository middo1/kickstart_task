import requests
import json

r = requests.get("https://opentdb.com/api.php?amount=10&category=19&difficulty=medium&type=multiple")

quest = json.loads(r.text)

q = quest["results"]
no = len(q)
x = 0
score = 0

while x < no:
    print(q[no - (no-x)]["question"])
    print(q[no - (no-x)]["correct_answer"])
    for y in q[no - (no-x)]["incorrect_answers"]:
        print(y)
    user_ans = input("Enter your answer: ")
    if user_ans == q[no - (no-x)]["correct_answer"]:
        print("correct")
        score += 1
    else:
        print("wrong")

    re = input("do you want to continue playing: ")
    if re == "no":
        print("Your score is " ,score)
        break
    else:
        x += 1
        continue


