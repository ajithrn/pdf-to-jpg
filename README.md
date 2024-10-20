# PDF to JPG Converter

This Python script converts PDF files in the current directory to JPG images. It's designed to process multiple PDF files, creating separate JPG images for each page of each PDF. The script also allows users to append or prepend custom text to the output filenames.

## Requirements

- Python 3.x
- pdf2image library
- Pillow library
- Poppler

## Installation

1. Ensure you have Python 3.x installed on your system.

2. Create and activate a virtual environment (recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Unix or MacOS
   venv\Scripts\activate.bat  # On Windows
   ```

3. Install the required Python libraries:
   ```
   pip install pdf2image Pillow
   ```

4. Install Poppler:
   - On macOS (using Homebrew):
     ```
     brew install poppler
     ```
   - On Ubuntu or Debian:
     ```
     sudo apt-get install poppler-utils
     ```
   - On Windows:
     Download and install from: http://blog.alivate.com.au/poppler-windows/

## Usage

1. Place the `pdf_to_jpg.py` script in the same directory as your PDF files.

2. Run the script:
   ```
   python pdf_to_jpg.py
   ```

3. The script will prompt you with numbered options for output filenames:
   1. Append text
   2. Prepend text
   3. No additional text (default)

4. Enter your choice (1, 2, or 3). If you choose 1 or 2, you'll be prompted to enter the text you want to add.

5. The script will process all PDF files in the current directory and create JPG images for each page.

## Output

- For each PDF file named `example.pdf`, the script will create images with the following naming conventions:
  - Default (Option 3): `PDF-example-page1.jpg`, `PDF-example-page2.jpg`, etc.
  - Appended (Option 1): `PDF-example-page1-YourText.jpg`, `PDF-example-page2-YourText.jpg`, etc.
  - Prepended (Option 2): `YourText-PDF-example-page1.jpg`, `YourText-PDF-example-page2.jpg`, etc.

## Troubleshooting

If you encounter an error message like "Unable to get page count. Is poppler installed and in PATH?", ensure that:

1. Poppler is correctly installed on your system.
2. The Poppler binaries are in your system's PATH.
3. You may need to restart your terminal or IDE after installing Poppler to update the PATH.

## Notes

- This script assumes all PDF files are in the same directory as the script.
- Large PDF files may take some time to process.
- Ensure you have sufficient disk space for the output JPG files.
- The appended or prepended text will be added to all output files in the session.
- If no choice is made, the script will default to option 3 (no additional text).

## Project Structure

- `pdf_to_jpg.py`: The main Python script for PDF to JPG conversion.
- `README.md`: This file, containing project documentation.
- `.gitignore`: Specifies intentionally untracked files to ignore in Git.
- `LICENSE`: Contains the MIT License text for this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
