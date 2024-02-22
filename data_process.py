import gzip
import os
import re
import json

# Function to decompress all .gz files in a directory
def decompress_gz_files(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith('.gz'):
            decompressed_filename = filename[:-3]
            with gzip.open(os.path.join(source_dir, filename), 'rb') as f_in:
                with open(os.path.join(target_dir, decompressed_filename), 'wb') as f_out:
                    f_out.write(f_in.read())
            yield decompressed_filename

# Function to parse a single document and convert it to a JSON object
def parse_document(doc_content):
    docno = re.search(r'<DOCNO>\s*(.*?)\s*</DOCNO>', doc_content)
    text = re.search(r'<TEXT>(.*?)</TEXT>', doc_content, re.DOTALL)
    
    document = {
        'id': docno.group(1).strip() if docno else None,
        'contents': text.group(1).strip() if text else None
    }
    return document

# Function to convert a single file to JSON and save it
def convert_file_to_json(file_path, json_dir):
    json_output_path = os.path.join(json_dir, os.path.basename(file_path) + '.json')
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        documents = []
        doc_content = []
        in_document = False
        for line in file:
            if '<DOC>' in line:
                in_document = True
                doc_content = []
            elif '</DOC>' in line:
                in_document = False
                doc_content.append(line)
                document = parse_document(''.join(doc_content))
                documents.append(document)
            elif in_document:
                doc_content.append(line)
                
    with open(json_output_path, 'w', encoding='ISO-8859-1') as json_file:
        json.dump(documents, json_file, ensure_ascii=False, indent=4)

# The script to process all .gz files in a directory
def process_gz_files_in_directory(source_dir, target_dir, json_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    if not os.path.exists(json_dir):
        os.makedirs(json_dir)
    
    decompressed_files = decompress_gz_files(source_dir, target_dir)
    
    for filename in decompressed_files:
        file_path = os.path.join(target_dir, filename)
        convert_file_to_json(file_path, json_dir)


source_dir = 'AP'
target_dir = 'Data'
json_dir = 'Data_json'

process_gz_files_in_directory(source_dir, target_dir, json_dir)
