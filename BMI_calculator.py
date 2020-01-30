# To calculate the BMI of a person in different unit
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
        print("Input 'm(meters)' or 'inches' or 'cm(centimeters)' or 'feet'")
        height_unit = input("Input the height unit:")
        print("The height unit you input is {}".format(height_unit))
        print("Please input the weight")
        height = input("Input the height:")

        return weight_unit,weight,height_unit,height

def verify(weight_unit,weight,height_unit,height):
    if weight_unit == 'kg':
        if height_unit == 'm':
            BMI_calculate(weight,height)
        if height_unit == 'meters':
            BMI_calculate(weight,height)
        if height_unit == 'inches':
            height = 0.0254*height
            BMI_calculate(weight,height)
        if height_unit == 'cm':
            height = 0.01*height
            BMI_calculate(weight,height)
        if height_unit == 'centimeters':
            height = 0.01*height
            BMI_calculate(weight,height)
        if height_unit == 'feet':
            height = 0.3048*height
            BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    if weight_unit == 'kilograms':
        if height_unit == 'm':
            BMI_calculate(weight,height)
        if height_unit == 'meters':
            BMI_calculate(weight,height)
        if height_unit == 'inches':
            height = 0.0254*height
            BMI_calculate(weight,height)
        if height_unit == 'cm':
            height = 0.01*height
            BMI_calculate(weight,height)
        if height_unit == 'centimeter':
            height = 0.01*height
            BMI_calculate(weight,height)
        if height_unit == 'feet':
            height = 0.3048*height
            BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    if weight_unit == 'lbs':
        weight = 0.45359237*weight
        if height_unit == 'm':
            BMI_calculate(weight,height)
        if height_unit == 'meters':
            BMI_calculate(weight,height)
        if height_unit == 'inches':
            height = 0.0254*height
            BMI_calculate(weight,height)
        if height_unit == 'cm':
            height = 0.01*height
            BMI_calculate(weight,height)
        if height_unit == 'centimeter':
            height = 0.01*height
            BMI_calculate(weight,height)
        if height_unit == 'feet':
            height = 0.3048*height
            BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    if weight_unit == 'pounds':
        weight = 0.45359237*weight
        if height_unit == 'm':
            BMI_calculate(weight,height)
        if height_unit == 'meters':
            BMI_calculate(weight,height)
        if height_unit == 'inches':
            height = 0.0254*height
            BMI_calculate(weight,height)
        if height_unit == 'cm':
            height = 0.01*height
            BMI_calculate(weight,height)
        if height_unit == 'centimeter':
            height = 0.01*height
            BMI_calculate(weight,height)
        if height_unit == 'feet':
            height = 0.3048*height
            BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")
    else:
        print("Please input 'kg' or 'kilograms' or 'lbs' or 'pounds' these exact words")


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
            verify(weight_unit,weight,height_unit,height)


if __name__=="__main__":
    interface()
