def modify_file(input_filename, output_filename):
    """
    Reads a file, modifies each line, and writes the modified lines to a new file.

    Args:
        input_filename (str): The name of the file to read.
        output_filename (str): The name of the file to write to.
    """
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                # Modify the line here (example: add " [MODIFIED]" to each line)
                modified_line = line.strip() + " [MODIFIED]\n"
                outfile.write(modified_line)
        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The input file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}' or write to '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "_main_":
    while True:
        input_file = input("Enter the name of the file to read: ")
        try:
            with open(input_file, 'r') as f:
                print(f"File '{input_file}' found and is readable.")
                break  # Exit the loop if the file is successfully opened
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied to read '{input_file}'. Please check file permissions and try again.")
        except Exception as e:
            print(f"An unexpected error occurred while trying to open '{input_file}': {e}. Please try again.")

    output_file = input("Enter the name for the new output file: ")
    modify_file(input_file, output_file)

    print("\n--- Outcomes Achieved! 🎉 ---")
    print("You are now skilled in:")
    print("- Reading data from files in Python.")
    print("- Writing modified data to new files.")
    print("- Implementing error handling for file operations (FileNotFoundError, PermissionError, etc.).")
    print("- Building more robust and user-friendly applications by handling potential file-related issues.")