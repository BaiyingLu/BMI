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
            result = BMI_calculate(weight,height)
        elif height_unit == 'meters':
            result = BMI_calculate(weight,height)
        elif height_unit == 'inches':
            height = 0.0254*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'cm':
            height = 0.01*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'centimeters':
            height = 0.01*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'feet':
            height = 0.3048*height
            result =BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    elif weight_unit == 'kilograms':
        if height_unit == 'm':
            result =BMI_calculate(weight,height)
        elif height_unit == 'meters':
            result =BMI_calculate(weight,height)
        elif height_unit == 'inches':
            height = 0.0254*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'cm':
            height = 0.01*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'centimeter':
            height = 0.01*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'feet':
            height = 0.3048*height
            result =BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    elif weight_unit == 'lbs':
        weight = 0.45359237*weight
        if height_unit == 'm':
            result =BMI_calculate(weight,height)
        elif height_unit == 'meters':
            result =BMI_calculate(weight,height)
        elif height_unit == 'inches':
            height = 0.0254*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'cm':
            height = 0.01*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'centimeter':
            height = 0.01*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'feet':
            height = 0.3048*height
            result =BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")

    elif weight_unit == 'pounds':
        weight = 0.45359237*weight
        if height_unit == 'm':
            result =BMI_calculate(weight,height)
        elif height_unit == 'meters':
            result =BMI_calculate(weight,height)
        elif height_unit == 'inches':
            height = 0.0254*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'cm':
            height = 0.01*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'centimeter':
            height = 0.01*height
            result =BMI_calculate(weight,height)
        elif height_unit == 'feet':
            height = 0.3048*height
            result =BMI_calculate(weight,height)
        else:
            print("Please input 'm' or 'meters' or 'inches' or 'cm' or 'centimeters' or 'feet' these exact words")
    else:
        print("Please input 'kg' or 'kilograms' or 'lbs' or 'pounds' these exact words")
    return result


def BMI_calculate(weight,height):
    weight = float(weight)
    height = float(height)
    BMI = weight/(height**2)
    if BMI<18.5:
        return "Underweight"
    elif 18.5<=BMI<25:
        return "Normal weight"
    elif 25<=LDL_level<30:
        return "Overweight"
    else:
        return "Obese"

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
            result = verify(weight_unit,weight,height_unit,height)
            print(result)

if __name__=="__main__":
    interface()
