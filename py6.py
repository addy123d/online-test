arr = [1, 1, 2, 2, 3, 3, 3, 3]
counter = 1

if len(arr) == 1:
    print(f'Number occuring more than 25% is {arr[0]}')
else:
    for index in range(1, len(arr)):
        # print(arr[index])

        # Check repetition !
        if arr[index-1] == arr[index]:
            counter = counter + 1
        # print(f'Number is {arr[index]} and it is repeating {counter} times')

        # Check whether number is repeating more than 25% or not !
            if counter >= len(arr)*0.25:
                print(
                    f'Length of array is {len(arr)} and 25% is {len(arr)*0.25}')
                print("hit !")
                print(f'Number occuring more than 25% is {arr[index]}')
                break

        else:
            counter = 1
