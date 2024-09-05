# Desktop Cleaner

A Python script designed to automatically sort and organize files from the "Downloads" folder into specific folders based on their type (e.g., images, audio, video). This script aims to declutter and manage files effectively on your PC.

## Features

- **Basic File Handling:** Identifies and moves files based on their type (e.g., `.png`, `.jpg`, `.mp3`, `.mp4`) to designated folders.
- **Categorization and Organization:** Automatically sorts files into specific folders (like "Images", "Audio", "Videos") based on their MIME types.
- **User Input and Flexibility:** Planned future feature to allow user-defined rules for file sorting.
- **Error Handling:** Planned improvement to handle errors gracefully during the file sorting process.
- **Graphical User Interface (GUI):** Optional enhancement to provide a user-friendly interface for the script.

## TODO

- Implement basic file handling to move files.
- Categorize and organize files based on their MIME types.
- Add user input functionality for customizable file sorting.
- Implement error handling for robust operation.
- (Optional) Develop a GUI for easy interaction.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Th30utcast/Desktop-Cleaner.git
   cd Desktop-Cleaner
   ```

2. **Install Required Libraries:**

   The script uses Python's standard libraries (`os`, `shutil`, `mimetypes`), so there are no additional dependencies.

3. **Run the Script:**

   ```bash
   python DeskCleaner.py
   ```

## Usage

- Place the script in a directory where you want to organize files or set the target directory in the script.
- Run the script from the command line or double-click it to execute.
- The script will sort files in the "Downloads" folder (default) into their respective categories (like "Images", "Audio", "Videos").

## Future Enhancements

- Improve file categorization and organization logic.
- Implement a graphical user interface (GUI) for ease of use.
- Add advanced error handling for better stability.
- Provide more flexible user input options for customized file sorting.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions and improvements.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.
