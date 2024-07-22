import re
import nltk
nltk.download('punkt')
from pathlib import Path
import os
from functions.general_utils import create_subfolder

# Helper function
def segment_and_save_text(input_data, temp_dir):
   
    with open(input_data, 'r', encoding="utf-8") as f:
        text = f.read()
        # modify the text
        text = re.sub("؟", "?", text)  # Replace any ؟ with ?
        # replace words that were difficult to parse by camel parser
        text = re.sub(r"\bولكي\b", "و لكي", text)
        text = re.sub(r"\bحينما\b", "حين ما", text)

        sentences = nltk.sent_tokenize(text)

    common_subfolder = create_subfolder(temp_dir, "segmented_files")

    file_stem = os.path.splitext(Path(input_data).name)[0]
    output_file_path = os.path.join(common_subfolder, f"{file_stem}.txt")

    with open(output_file_path, 'w', encoding="utf-8") as f:
        f.write('\n'.join(sentences))

    print(f'Segmented file created at: {output_file_path}')
    return output_file_path

# Main function
def segmenting(input_folder, temp_dir):
    segmented_files = []
    input_folder_path = Path(input_folder)

    for input_file in input_folder_path.glob("*.txt"):
        print(f'Processing {input_file.name}')
        segmented_file = segment_and_save_text(input_file, temp_dir)
        segmented_files.append(segmented_file)

    return segmented_files

if __name__ == '__main__':
    segmenting('input_folder', 'temp_dir')