History_File = "history.txt"

def show_history():
    File = open(History_File,"r")
    lines = File.readlines()
    if len(lines) == 0:
        print("No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
    File.close()
    
def clear():
    File = open(History_File,"w")
    File.close()
    print("History cleared")

def save_history(equation,result):
    File = open(History_File,"a")
    File.write(f"{equation}={result}\n")
    File.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts)!=3:
        print("Invalid number. Use Format: number oparetor number")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1+num2
    elif op == "-":
        result = num1-num2
    elif op == "*":
        result = num1*num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1/num2
    else :
        print("Unsupported oparetor! Use only '+,-,*,/")

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_history(user_input,result)

def main():
    print("____SIMPLE CALCULATOR(type history,clear,exit)")
    while True:
        user_input = input("Enter Calculation (+,-,*,/) or command(history.clear,exit):")
        if user_input == "exit":
            print("Goodbye")
            break
        elif user_input== "history":
            show_history()
        elif user_input== "clear":
            clear()
        else :
            calculate(user_input)

main()








    

    



