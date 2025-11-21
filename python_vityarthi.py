#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Samarth
#
# Created:     14-11-2025
# Copyright:   (c) Samarth 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

def predict_single():
    print("\n--- Single Patient Disease Prediction ---")

    temp = float(input("Enter temperature (°C): "))
    cough = input("Cough (yes/no): ").lower()
    runny = input("Runny nose (yes/no): ").lower()
    fatigue = input("Fatigue (yes/no): ").lower()

    if temp >= 38 and cough == "yes" and fatigue == "yes":
        print("→ Possible Disease: Fever or Flu")
    elif cough == "yes" and runny == "yes":
        print("→ Possible Disease: Common Cold")
    elif fatigue == "yes" and temp < 38:
        print("→ Possible Condition: Weakness")
    else:
        print("→ No major symptoms detected.")

def predict_multiple():
    print("\n=== Multiple Patient Checking Mode ===")

    while True:
        name = input("\nEnter patient name (or type 'stop' to exit): ")

        if name.lower() == "stop":
            print("Exiting multiple patient mode...")
            break

        temp = float(input("Temperature: "))
        cough = input("Cough (yes/no): ").lower()
        runny = input("Runny nose (yes/no): ").lower()

        if temp > 38 and cough == "yes":
            print(f"{name} may have Fever.")
        elif cough == "yes" and runny == "yes":
            print(f"{name} may have Cold.")
        else:
            print(f"No major symptoms detected for {name}.")


def dictionary_predict():
    print("\n=== Dictionary-Based Prediction ===")

    diseases = {
        "Fever": ["high temperature", "fatigue"],
        "Cold": ["cough", "runny nose"],
        "Flu": ["fever", "cough", "weakness"]
    }

    sym1 = input("Enter symptom 1: ").lower()
    sym2 = input("Enter symptom 2: ").lower()

    matched = []

    for disease, symptoms in diseases.items():
        if sym1 in symptoms or sym2 in symptoms:
            matched.append(disease)

    if matched:
        print("Possible diseases:", matched)
    else:
        print("No disease matched these symptoms.")


def show_about():
    print("\n--- ABOUT THIS PROGRAM ---")
    print("This is a basic rule-based disease prediction system built using pure Python.")
    print("Features:")
    print(" - Single patient prediction")
    print(" - Multiple patient checking")
    print(" - Dictionary-based disease matching")
    print("This project is designed for first-year engineering students.")

def main():
    while True:
        print("\n====================================")
        print("        DISEASE PREDICTION SYSTEM")
        print("====================================")
        print("1. Predict Disease (Single Patient)")
        print("2. Predict Disease (Multiple Patients)")
        print("3. Dictionary-Based Prediction")
        print("4. About Program")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            predict_single()
        elif choice == "2":
            predict_multiple()
        elif choice == "3":
            dictionary_predict()
        elif choice == "4":
            show_about()
        elif choice == "5":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Try again.")

main()




