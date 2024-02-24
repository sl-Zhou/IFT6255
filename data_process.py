import os
import gzip
import shutil

# Function to extract all .gz files in a directory
def extract_all_gz(directory, output_directory):
    # Create the extracted files directory if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.endswith('.gz'):
            # The path to the current .gz file
            file_path = os.path.join(directory, filename)
            # The output path for the extracted content
            output_file_path = os.path.join(output_directory, filename[:-3])  # Remove the .gz extension
            # Extract the .gz file
            with gzip.open(file_path, 'rb') as f_in:
                with open(output_file_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            print(f'Extracted: {filename}')


gz_files_directory = 'AP'

extracted_files_directory = 'Data'

# Call the function to extract all .gz files
extract_all_gz(gz_files_directory, extracted_files_directory)