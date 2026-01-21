def main():
    age = input("What is your age?\n")  
    x = int(age)
    if x < 18:
        print("You are a child")
    else:
        print("You are an adult")


main()