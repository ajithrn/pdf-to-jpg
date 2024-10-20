import os
import sys
import shutil
from pdf2image import convert_from_path
from PIL import Image

def check_poppler():
    return shutil.which('pdftoppm') is not None

def get_user_input():
    print("Choose an option for output filenames:")
    print("1. Append text")
    print("2. Prepend text")
    print("3. No additional text (default)")
    
    choice = input("Enter your choice (1/2/3): ").strip() or '3'
    
    if choice in ['1', '2']:
        text = input("Enter the text to add: ")
        return ('append' if choice == '1' else 'prepend'), text
    return 'no', ''

def convert_pdfs_to_jpgs(folder_path):

    action, text = get_user_input()

    try:
        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                base_name = filename.replace(' ', '-').rsplit('.', 1)[0]
                
                try:
                    pages = convert_from_path(os.path.join(folder_path, filename))
                    
                    for i, page in enumerate(pages):
                        if action == 'append':
                            jpg_filename = f"{base_name}-page{i+1}-{text}.jpg"
                        elif action == 'prepend':
                            jpg_filename = f"{text}-{base_name}-page{i+1}.jpg"
                        else:
                            jpg_filename = f"{base_name}-page{i+1}.jpg"
                        
                        page.save(os.path.join(folder_path, jpg_filename), 'JPEG')
                    
                    print(f"Converted {filename} to JPG(s)")
                except Exception as e:
                    print(f"Error converting {filename}: {str(e)}", file=sys.stderr)

        print("All PDFs have been processed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    folder_path = '.'  # Current directory, change if needed
    convert_pdfs_to_jpgs(folder_path)
