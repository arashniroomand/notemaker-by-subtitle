import os
import string
from google.colab import drive
import google.generativeai as genai

def mount_drive(drive_path='/content/drive'):
    """Mount Google Drive."""
    drive.mount(drive_path)

def process_files(folder_path, md_files_path, model):
    """Process files in the folder, transform them, and save the results."""
    for filename in os.listdir(folder_path):
        if filename.endswith('.en.srt'):
            process_file(folder_path, filename, md_files_path, model)

def process_file(folder_path, filename, md_files_path, model):
    """Process a single file, generate content, and save it in MD format."""
    filepath = os.path.join(folder_path, filename)

    with open(filepath, 'r') as f:
        texts = []
        for line in f:
            if line.strip() and '-->' not in line:
                texts.append(line)

    prompt = (
        "Read the below text and write it as a notebook. "
        "Extend it with additional knowledge and provide the text in MD format, "
        "including bold title and subtitle:\n\n" + "".join(texts)
    )

    response = model.generate_content(prompt)
    md_file_final = os.path.join(md_files_path, filename.replace('.en.srt', '.md'))

    with open(md_file_final, 'w') as md_file:
        md_file.write(response.text)

def main():
    """Main function to execute the script."""
    API_KEY = "YOUR_API_KEY"
    FOLDER_PATH = "ENTER_fOLDER_PATH"
    MD_FILES_PATH = "ENTER_MD_FILES_PATH"

    mount_drive()
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    process_files(FOLDER_PATH, MD_FILES_PATH, model)

if __name__ == "__main__":
    main()