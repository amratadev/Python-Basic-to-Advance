import random 
print("Welcome to the head-tail Game..!!")

round=5
user_head=0
computer_head=0

for toss in range(1,round+1):
    print(f"\n Toss:{toss}")

    user_result=random.choice(["head","tail"])
    print("User:",user_result)

    computer_result=random.choice(["head","tail"])
    print("Computer:",computer_result)

    if user_result=="head":
        user_head+=1
    if computer_result=="head":
        computer_head+=1

# ✅ Final winner check loop नंतर
if user_head>computer_head:
       print("User WINS the Game!")
elif computer_head>user_head:
       print("Computer WINS the Game!")
else:
       print("Match DRAW!")