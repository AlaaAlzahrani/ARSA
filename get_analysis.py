from ARSA.functions.general_utils import create_temp_directory
from ARSA.functions.get_segment import segmenting
from ARSA.camel_parser.handle_multiple_texts import parsing_texts
from ARSA.functions.get_format import formatting
from ARSA.functions.get_measures import measures
from pathlib import Path
import shutil


#
## main function ##
#
def automatic_analyzer():

    # Create temporary directory
    temp_dir = create_temp_directory()

    # determine input and output 
    input_folder = input ('Please select the text file(s) folder:')
    output_folder = input ('Please select the output folder:')

    final_output_csv = None  # initialize to None
    output_path = None  # Initialize to None

    try:
        # use temporary directory for intermediate functions
        segmented_files = segmenting (input_folder, temp_dir)
        parsed_files = parsing_texts(segmented_files, 'catib', 'catib6', temp_dir)
        formatted_files = formatting(parsed_files, temp_dir)

        final_output_csv = measures(formatted_files, output_folder)


        if final_output_csv is not None:
            # Move the final result to the permanent output directory
            output_path = Path(output_folder) / "final_output.csv"
            shutil.move(final_output_csv, output_path)

    finally:
        shutil.rmtree(temp_dir)

    return output_path