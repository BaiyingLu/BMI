# To calculate the BMI of a person
def unit_select_and_input():
    while True:
        print("Please input the calculation unit")
        print("Please input the weight unit first")
        print("Input 'kg(kilograms)' or 'lbs(pounds)'")
        weight_unit = input("Input the weight unit:")
        print("The weight unit you input is {}".format(weight_unit))
        print("Please input the weight")
        weight = input("Input the weight:")


        print("Next, please input the height unit")
        print("Input 'm(meters)' or 'inches' or 'cm'")
        height_unit = input("Input the height unit:")
        print("The height unit you input is {}".format(height_unit))
        print("Please input the weight")
        height = input("Input the height:")

        return weight_unit,weight,height_unit,height



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
            weight_unit,weight,height_unit,height = unit_select_and_input()
            print(weight_unit,weight,height_unit,height)


if __name__=="__main__":
    interface()
