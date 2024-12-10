import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python setupday.py <day_number>")
        return

    dayNum = sys.argv[1]
    folder_name = f"day{dayNum}"

    # Check if the folder already exists
    if os.path.exists(folder_name):
        print(f"Error: Folder '{folder_name}' already exists.")
        return
    else:
        os.makedirs(folder_name)

        with open(os.path.join(folder_name, f"{folder_name}.txt"), 'w') as txt_file:
            txt_file.write("")  # Empty .txt file
        with open(os.path.join(folder_name, f"{folder_name}sample.txt"), 'w') as txt_file_sample:
            txt_file_sample.write("")  # Empty .txt file

        with open(os.path.join(folder_name, f"{folder_name}p1.py"), 'w') as p1_py_file:
            p1_py_file.write("")  # Empty .py file
        with open(os.path.join(folder_name, f"{folder_name}p2.py"), 'w') as p2_py_file:
            p2_py_file.write("")  # Empty .py file

        print(f"Folder '{folder_name}' created successfully.")


if __name__ == "__main__":
    main()
