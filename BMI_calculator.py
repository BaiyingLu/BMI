# To calculate the BMI of a person
def interface():
    while True:
        print("This is a BMI calculator")
        print("Please input option:")
        print("1 - Do analysis")
        print("9 - quit")
        choice = input('Enter you option:')
        if choice == '9':
            return
        elif choice == "1":
            pass


if __name__=="__main__":
    interface()
