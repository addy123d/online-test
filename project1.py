# Online Test !
# 1. Collect personal details from user
# a] Which data structure should be used ? - Arrays/Lists
# b] How to store ? - students = [[name, rollno, marks]]
# Initialisation
import time
import os

# For console color
os.system("cls")

print()
print("\033[36m Quiz Application By MANALI BHOSLE \033[00m")

for i in range(0, 50):
    print("\033[93m -\033[00m", end="")
print()


user_record = []
questions = [
    ["What did the Romans call Scotland?", "Caledonia"],
    ["Who was made Lord Mayor of London In 1397, 1398, 1406 And 1419?",
        "Richard (Dick) Whittington"],
    ["Who was the youngest British Prime Minister?",
        "William Pitt (The Younger)"],
    ["In which year was Joan of Arc burned at the stake?", "1431"],
    ["In which year did Britain originally join the EEC, now known as the European Union?",
        "1973"]
]

expected_answers = [
    ["Caledonia", "Augusta National", "Scot"],
    ["Catherine Parr", "Richard (Dick) Whittington", "Sir Walter Raleigh"],
    ["William Pitt (The Younger)", "Sir Walter Raleigh", "Mike Pence"],
    ["1350", "1401", "1431"],
    ["1901", "1973", "1937"],
]

questn_number = 1
total_marks = 0
flag = 0
time_flag = 0
condition = "no"


while condition == "no":
    print('''
        Options :
        1. EXIT
        2. Start Test
        ''')

    option = int(input("Choose your option : "))

    if (option == 1):
        # print(f'Student Record : {user_record}')
        # print("Do you want to exit ? Yes/No")
        # condition = input()
        # condition = condition.lower()
        condition = "yes"
    else:

        name = input("Enter name : ")
        roll_no = int(input("Enter Roll Number : "))

        # Set current Time
        time_after = time.time() + 30

        for i in range(0, len(questions)):

            for j in range(0, len(questions[i])-1):
                print(f' {questn_number}] {questions[i][j]} ? ')
                print(
                    f"   1] {expected_answers[i][0]}   2] {expected_answers[i][1]}  3] {expected_answers[i][2]} ")

                # Collect options from user !
                answer = input("Your Answer : ")

                # Initialise current time every time the question changes !
                current_time = time.time()

                # Check whether time is left or not !
                if (time_after - current_time <= 0):
                    time_flag = 1
                    break

                # Verify if the option is correct or not !
                if(expected_answers[i][int(answer)-1] == questions[i][1]):
                    print(
                        f"Correct - Time Left \033[33m {int(time_after - current_time)} \033[00m secs")
                    total_marks = total_marks + 1
                else:
                    print(
                        f" Wrong - Time Left \033[33m {int(time_after - current_time)} \033[00m secs ")

                questn_number = questn_number + 1
                print()
                for i in range(0, 50):
                    print("\033[93m -\033[00m", end="")
                print()
                print()

            # When user types exit
            if (flag == 1):
                break

            # When time's up
            if (time_flag == 1):
                print("Time's Up ! Test will be submitted automatically !")
                break

        # Store !
        user = [name, roll_no, total_marks]
        user_record.append(user)

        print(f'Students : {user_record}')

        # Final report Card !
        print(f''' Name - \033[36m {name} \033[00m
                   Roll Number - \033[36m {roll_no} \033[00m
                   Marks - \033[36m {total_marks} \033[00m''') if (
            total_marks > 1) else print(f''' \033[36m {name} \033[00m
                                             Roll Number - \033[36m {roll_no} \033[00m
                                             Marks - \033[36m {total_marks} \033[00m''')

        # Reset total_marks !
        total_marks = 0

        # Final exit dialog box !
        print("Do you want to exit ? Yes/No")
        condition = input()
        condition = condition.lower()

# Out of loop !
for i in range(0, 50):
    print("\033[93m -\033[00m", end="")
print()
