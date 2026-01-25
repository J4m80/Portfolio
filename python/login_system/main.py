import reg
import log

def main():
    while True:
        print("\nWelcome!")
        print("Choose an action:")
        print("1 - Register")
        print("2 - Login")
        print("3 - Exit")

        choice = input("Enter the number: ")

        if choice == "1":
            reg.run()
        elif choice == "2":
            log.run()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")
