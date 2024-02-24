import re

def parse_topics_to_tsv(text_data):
    # Split the text into individual topic sections
    topics = re.split(r'<top>', text_data)

    # Prepare the TSV content
    tsv_content = []

    for topic in topics:
        # Extract the number and title from each topic
        num_match = re.search(r'<num> Number:\s+(\d+)', topic)
        title_match = re.search(r'<title> Topic:\s+(.+?)\n', topic)

        # Check if both number and title are found
        if num_match and title_match:
            num = num_match.group(1).strip()
            title = title_match.group(1).strip()
            # Append to TSV content list as a tab-separated string
            tsv_content.append(f"{num}\t{title}")

    # Join all lines into a single string to represent the content of a TSV file
    tsv_result = "\n".join(tsv_content)
    return tsv_result

# File path
text_data_path = r"D:\IFT\ift6255\devoir1\AP_topics.1-150.txt"

# Read the file content
with open(text_data_path, 'r') as file:
    text_data = file.read()

# Process the text data to generate TSV content
tsv_output = parse_topics_to_tsv(text_data)

# Write the TSV content to a file
output_file_path = r'D:\IFT\ift6255\devoir1\tsv\query.tsv'
with open(output_file_path, 'w') as file:
    file.write(tsv_output)


