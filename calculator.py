done = "yes"
a = eval(input("Enter a: "))

while done != "no":
    b = eval(input("Enter b: "))
    c = input("Enter operator (+, -, *, /): ")

    if c == '+':
        a = a + b
    elif c == '-':
        a = a - b
    elif c == '*':
        a = a * b
    elif c == '/':
        if b == 0:
            print("Zero division error!")
            continue
        else:
            a = a / b
    else:
        print("Invalid operator!")
        continue

    done = input("Do you want to continue (yes/no): ")

print("Result:", a)
