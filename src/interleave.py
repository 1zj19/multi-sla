import zipfile
import os

def process_zip_file():

    zip_file_path = input("Enter the full path to the zip file: ")
    if not os.path.exists(zip_file_path):
        print(f"Error: The file '{zip_file_path}' does not exist.")
        return
    if not os.path.isfile(zip_file_path):
        print(f"Error: The path '{zip_file_path}' is not a file.")
        return

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            print(f"\nReal .png files in '{zip_file_path}':")
            real_pngs = [
                name for name in zf.namelist()
                if name.endswith('.png') and '/._' not in name and not name.startswith('__MACOSX')
            ]

            if not real_pngs:
                print("No valid .png files found.")
                return

            for name in real_pngs:
                print(name)

    except zipfile.BadZipFile:
        print(f"Error: '{zip_file_path}' is not a valid zip file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_zip_file()