
def input_grades():
    try:
        with open("grades.txt", "a") as file:
            while True:
                subject = input("Enter subject name (or 'done' to finish): ")

                if subject.lower() == "done":
                    break

                try:
                    grade = float(input("Enter grade (0-100): "))

                    if grade < 0 or grade > 100:
                        print("Please enter a grade between 0 and 100.")
                        continue

                    file.write(f"{subject},{grade}\n")
                    print("Grade saved successfully!")

                except ValueError:
                    print("Invalid input. Please enter a numeric grade.")

    except OSError as error:
        print("File error:", error)


def calculate_average():
    try:
        grades = []

        with open("grades.txt", "r") as file:
            for line in file:
                try:
                    subject, grade = line.strip().split(",")
                    grades.append(float(grade))
                except ValueError:
                    print("Skipping invalid grade record.")

        if len(grades) == 0:
            print("No grades found.")
            return None

        average = sum(grades) / len(grades)
        print("Your average grade is:", round(average, 2))
        return average

    except FileNotFoundError:
        print("No grade file found. Please enter grades first.")
        return None

    except OSError as error:
        print("File error:", error)
        return None


def main():
    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Enter subject grades")
        print("2. Calculate average grade")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            input_grades()
        elif choice == "2":
            calculate_average()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    return


if __name__ == "__main__":
    main()