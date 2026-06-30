try:
    # Ask the user for the file name
    file_name = input("Enter the file name (with .txt): ")

    # Open the file in read mode
    with open(file_name, "r") as file:
        content = file.read()

    print("\nCurrent File Content:")
    print("-" * 40)
    print(content)
    print("-" * 40)

    # Ask the user which word to replace
    old_word = input("\nEnter the word to find: ")
    new_word = input("Enter the replacement word: ")

    # Check if the word exists
    if old_word in content:

        # Replace the word
        updated_content = content.replace(old_word, new_word)

        # Save the updated content back to the file
        with open(file_name, "w") as file:
            file.write(updated_content)

        print("\nWord replaced successfully!")

        print("\nUpdated File Content:")
        print("-" * 40)
        print(updated_content)
        print("-" * 40)

    else:
        print("\nThe word was not found in the file.")

except FileNotFoundError:
    print("\nError: File not found.")

except PermissionError:
    print("\nError: Permission denied.")

except Exception as e:
    print("\nAn unexpected error occurred.")
    print(e)