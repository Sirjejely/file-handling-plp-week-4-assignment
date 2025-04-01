def read_and_modify_file():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the filename to read: ")
        
        # Open the file for reading
        with open(input_filename, 'r') as file:
            content = file.readlines()
        
        # count the number of words in the file
        file = open("input.txt", "r")
        data = file.read()
        words = data.split()
        count = len(words)
        print("Number of words in the file:", count)
        
        # Modify the content (example: convert to uppercase)
        modified_content = [line.upper() for line in content]
                
        # Define the output filename
        output_filename = "modified_" + input_filename
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.writelines(modified_content)
            file.write("\nNumber of words in the file: " + str(count))

        
        print(f"File successfully modified and saved as {output_filename}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please enter a valid filename.")
    except IOError:
        print("Error: Unable to read the file. Please check file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
