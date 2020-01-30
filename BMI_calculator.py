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
        print("Please input the height")
        height = input("Input the height:")

        return weight_unit,weight,height_unit,height

def verify(weight_unit,weight,height_unit,height):
    if weight_unit == 'kg':
        if height_unit == 'm':
            result,BMI_value = BMI_calculate(weight,height)
        elif height_unit == 'meters':
            result,BMI_value = BMI_calculate(weight,height)
        elif height_unit == 'inches':
            height = float(height)
            height = 0.0254*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'cm':
            height = float(height)
            height = 0.01*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'centimeters':
            height = float(height)
            height = 0.01*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'feet':
            height = float(height)
            height = 0.3048*height
            result ,BMI_value=BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    elif weight_unit == 'kilograms':
        if height_unit == 'm':
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'meters':
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'inches':
            height = float(height)
            height = 0.0254*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'cm':
            height = float(height)
            height = 0.01*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'centimeter':
            height = float(height)
            height = 0.01*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'feet':
            height = float(height)
            height = 0.3048*height
            result,BMI_value =BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    elif weight_unit == 'lbs':
        weight = float(weight)
        weight = 0.45359237*weight
        if height_unit == 'm':
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'meters':
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'inches':
            height = float(height)
            height = 0.0254*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'cm':
            height = float(height)
            height = 0.01*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'centimeter':
            height = float(height)
            height = 0.01*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'feet':
            height = float(height)
            height = 0.3048*height
            result,BMI_value =BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    elif weight_unit == 'pounds':
        weight = float(weight)
        weight = 0.45359237*weight
        if height_unit == 'm':
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'meters':
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'inches':
            height = float(height)
            height = 0.0254*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'cm':
            height = float(height)
            height = 0.01*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'centimeter':
            height = float(height)
            height = 0.01*height
            result,BMI_value =BMI_calculate(weight,height)
        elif height_unit == 'feet':
            height = float(height)
            height = 0.3048*height
            result,BMI_value =BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")
            result = -1
            BMI_value = -1
    else:
        print("Please input 'kg' or 'kilograms' or 'lbs' or 'pounds' these exact words")
        result = -1
        BMI_value = -1
    return result,BMI_value


def BMI_calculate(weight,height):
    weight = float(weight)
    height = float(height)
    BMI = weight/(height**2)
    if BMI<18.5:
        return "Underweight",BMI
    elif 18.5<=BMI<25:
        return "Normal weight",BMI
    elif 25<=BMI<30:
        return "Overweight",BMI
    else:
        return "Obese",BMI

def print_the_result(result,BMI_value):
    if result == -1:
        print("Please input the unit again")
    else:
        print("The BMI of this person is {}".format(round(BMI_value,3)))
        print("The health level of this person is {}".format(result))


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
            result,BMI_value = verify(weight_unit,weight,height_unit,height)
            print_the_result(result,BMI_value)

if __name__=="__main__":
    interface()
