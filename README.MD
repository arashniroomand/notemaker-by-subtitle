# Subtitle to Markdown Converter

This script processes .en.srt subtitle files and  write a complete not from subtitle like we already do in our classes using Google Generative AI and converts them into Markdown format. 
# Sample of Output

![photo](img\sample.png)
## Features

- Mounts Google Drive to access subtitle files in a Colab environment.
- Processes subtitle files and converts them into structured Markdown format.
- Utilizes the gemini-pro model from Google Generative AI.
- Saves the converted Markdown files to a specified directory.

## Prerequisites

- Google Colab account (for running in the cloud)
- Google Drive access (if running in Colab)
- API key for Google Generative AI

## Setup

1. Clone or Copy the Script:
   - Copy the script to your Google Colab environment or local machine.

2. API Key:
   - Obtain an API key for Google Generative AI and replace YOUR_API_KEY in the script with your actual key.

3. Folder Paths:
   - Set FOLDER_PATH to the directory containing your .en.srt files.
   - Set MD_FILES_PATH to the directory where you want to save the .md files.

## Usage

### In Google Colab

1. Mount Google Drive:
   - Use the drive.mount('/content/drive') function to access your Google Drive files.

2. Configure API:
   - Call configure_genai(API_KEY) to set up the Generative AI with your API key.

3. Run the Script:
   - Execute the main() function to process files and generate Markdown content.

### On Your Local System

1. Remove Google Drive Dependencies:
   - Remove or comment out the from google.colab import drive and drive.mount() lines.

2. Set Local Paths:
   - Update FOLDER_PATH and MD_FILES_PATH to point to local directories.

3. Run Locally:
   - Execute the script using a Python environment that supports the google.generativeai library.

## Code Explanation

- `mount_drive`: Mounts Google Drive in Colab. Remove or modify this for local use.
- `process_files`: Identifies and processes subtitle files in the specified folder.
- `process_file`: Reads a subtitle file, uses AI to generate content, and saves it as Markdown.
- `main`: The entry point for executing the script.

## Notes

- The script is optimized for use with Google Colab but can be adapted for local environments.

