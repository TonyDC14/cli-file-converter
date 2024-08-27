import os
from PIL import Image

def create_export_folder(directory):
    export_path = os.path.join(directory, 'export')
    if not os.path.exists(export_path):
        os.makedirs(export_path)
    return export_path

def get_image_extensions():
    return ('.jfif', '.png', '.gif', '.bmp', '.tiff', '.svg', '.jpeg', '.jpg')

def get_supported_formats():
    return ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg']

def convert_image(img_path, output_path, target_extension):
    img = Image.open(img_path)
    img = img.convert('RGB') if img.mode == 'RGBA' else img
    format_mapping = {'jpg': 'JPEG', 'jpeg': 'JPEG', 'png': 'PNG', 'gif': 'GIF',
                      'bmp': 'BMP', 'tiff': 'TIFF', 'svg': 'SVG'}
    img_format = format_mapping.get(target_extension.lower(), target_extension.upper())
    img.save(output_path, img_format)
    print(f"Converted: {img_path} -> {output_path}")

def process_directory(directory, target_extension, export_path):
    image_extensions = get_image_extensions()
    for root, _, files in os.walk(directory):
        if 'export' in root:
            continue
        for file in files:
            process_file(root, file, export_path, image_extensions, target_extension)

def process_file(root, file, export_path, image_extensions, target_extension):
    if file.lower().endswith(image_extensions):
        img_path = os.path.join(root, file)
        output_file_name = os.path.splitext(file)[0] + f'.{target_extension}'
        output_path = os.path.join(export_path, output_file_name)
        convert_image(img_path, output_path, target_extension)

def run_conversion_loop():
    supported_formats = get_supported_formats()
    
    while True:
        print("Supported formats: " + ", ".join(supported_formats))
        directory = input("Enter the directory path: ").strip()
        target_extension = input(f"Enter the desired image extension (e.g., {', '.join(supported_formats)}): ").strip()
        
        if target_extension.lower() not in supported_formats:
            print(f"Error: Unsupported format '{target_extension}'. Please choose from the supported formats.")
        else:
            export_path = create_export_folder(directory)
            process_directory(directory, target_extension, export_path)
        
        if input("Type 'exit' to stop or press Enter to process another directory: ").strip().lower() == 'exit':
            break

if __name__ == "__main__":
    run_conversion_loop()

