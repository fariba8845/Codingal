def shutdown():
    user_input = input("Do you want to shut down? (Yes/No): ")

    if user_input == "Yes":
        print("Shutting down")
    elif user_input == "no":
        print("Aborting shut down.")
    else:
        print("Sorry.")

shutdown()
