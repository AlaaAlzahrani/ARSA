import os
from pathlib import Path
from ARSA.camel_tools.utils.charmap import CharMapper
from ARSA.camel_parser.src.classes import TextParams
from ARSA.camel_parser.src.conll_output import print_to_conll, save_to_file, text_tuples_to_string
from ARSA.camel_parser.src.data_preparation import parse_text
from ARSA.camel_parser.src.initialize_disambiguator.disambiguator_interface import get_disambiguator
from ARSA.camel_parser.src.utils.model_downloader import get_model_name
from docopt import docopt
from pandas import read_csv
from transformers.utils import logging

logging.set_verbosity_error()


def parsing_texts (files, parse_model, tagset, temp_dir):
  
    root_dir = Path(__file__).parent
    model_path = root_dir/"models"
    
    # camel_tools import used to clean text
    arclean = CharMapper.builtin_mapper("arclean")

    #
    ### Get clitic features
    #
    clitic_feats_df = read_csv(root_dir / 'data/clitic_feats.csv')
    clitic_feats_df = clitic_feats_df.astype(str).astype(object) # so ints read are treated as string objects
    

    #
    ### Set up parsing model 
    # (download defaults models, and get correct model name from the models directory)
    #
    model_name = get_model_name(parse_model, model_path=model_path)
    
    disambiguator = get_disambiguator("bert", "r13")
    
    #
    ### main code ###
    #

    parsed_files = []  # list to store paths of parsed files

    for text_file in files:
        print(f'processing {text_file}')
        lines = []
        with open(text_file, 'r') as f:
            lines = [line for line in f.readlines() if line.strip()]
            
        file_type_params = TextParams(lines, model_path/model_name, arclean, disambiguator, clitic_feats_df, tagset, "")
        parsed_text_tuples = parse_text("text", file_type_params)

        parsed_file_path = Path(temp_dir) / Path(text_file).name
        save_to_file(text_tuples_to_string(parsed_text_tuples, sentences=lines), parsed_file_path)

        parsed_files.append(parsed_file_path)  # append the path of the parsed file to the list

    return parsed_files  # return the list of parsed file paths

if __name__ == '__main__':
  parsing_texts(['/content/segmented/par101.txt', '/content/segmented/par101_copy.txt'], 'catib', 'catib6', '/content/parsed_files')