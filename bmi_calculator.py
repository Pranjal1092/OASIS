import argparse

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

def main():
    parser = argparse.ArgumentParser(description='Calculate your BMI (Body Mass Index).')
    
    parser.add_argument('-w', '--weight', type=float, help='Weight in kilograms')
    parser.add_argument('-t', '--height', type=float, help='Height in meters')
    
    args = parser.parse_args()
    
    if args.weight is None:
        args.weight = float(input('Enter your weight in kilograms: '))
    if args.height is None:
        args.height = float(input('Enter your height in meters: '))
    
    bmi = calculate_bmi(args.weight, args.height)
    category = classify_bmi(bmi)
    
    print(f'Your BMI is: {bmi:.2f}')
    print(f'BMI Category: {category}')

if __name__ == '__main__':
    main()
