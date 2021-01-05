# Online Test !
# 1. Collect personal details from user
# a] Which data structure should be used ? - Arrays/Lists
# b] How to store ? - students = [[name, rollno, marks]]
# Initialisation
import time


user_record = []
questions = [
    ["question 1", "A"],
    ["question 2", "B"],
    ["question 3", "C"],
    ["question 4", "D"],
    ["question 5", "C"]
]

questn_number = 1
total_marks = 0
flag = 0
time_flag = 0
condition = "no"


while condition == "no":
    print('''
        Options :
        1. Previous Student Records
        2. Give a test
        ''')

    option = int(input("Choose your option : "))

    if (option == 1):
        print(f'Student Record : {user_record}')
        print("Do you want to exit ? Yes/No")
        condition = input()
        condition = condition.lower()
    else:

        name = input("Enter name : ")
        roll_no = int(input("Enter Roll Number : "))

        # Set current Time
        time_after = time.time() + 30

        for i in range(0, len(questions)):

            for j in range(0, len(questions[i])-1):
                print(f' {questn_number}] {questions[i][j]} ? ')
                print("   1] A  2] B  3] C  4] D")

                # Collect options from user !
                answer = input("Your Answer : ")

                # Check whether time is left or not !
                current_time = time.time()

                if (time_after - current_time <= 0):
                    time_flag = 1
                    break

                # Verify if the option is correct or not !
                if(answer.upper() == questions[i][1]):
                    print(
                        f"Correct - Time Left {int(time_after - current_time)} secs")
                    total_marks = total_marks + 1
                elif answer.lower() == "exit":
                    flag = 1
                else:
                    print(
                        f" Wrong - Time Left {int(time_after - current_time)} secs ")

                questn_number = questn_number + 1

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
        print(f' {name} you got {total_marks} marks !') if (
            total_marks > 1) else print(f' {name} you got {total_marks} mark !')

        # Reset total_marks !
        total_marks = 0

        # Final exit dialog box !
        print("Do you want to exit ? Yes/No")
        condition = input()
        condition = condition.lower()
