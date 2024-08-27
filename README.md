# Image Converter Script

This script allows you to convert all image files in a specified directory to a desired format, supporting common image formats like `.jpg`, `.png`, `.gif`, etc. The converted images are saved in an `export` folder within the specified directory. The script prompts you to enter a new directory and image extension after each conversion cycle, allowing you to process multiple directories and formats in one run.

## Prerequisites

Ensure you have Python 3.x installed on your system.

## Installation

1. Clone this repository or download the script files.
2. Navigate to the project directory.
3. Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script using the following command:

    ```bash
    python script_name.py
    ```

    Replace `script_name.py` with the actual name of the script file.

2. When prompted, enter the path to the directory containing the images you wish to convert.

3. Specify the target image format (e.g., `jpg`, `png`) when prompted.

4. The script will process the images and save the converted files in an `export` folder within the specified directory.

5. After the conversion is complete, you can enter another directory and format or type `exit` to stop the script.

## Example

```bash
Supported formats: jpg, jpeg, png, gif, bmp, tiff, svg
Enter the directory path: /path/to/your/images
Enter the desired image extension (e.g., jpg, jpeg, png, gif, bmp, tiff, svg): jpg
Type 'exit' to stop or press Enter to process another directory: 
```
