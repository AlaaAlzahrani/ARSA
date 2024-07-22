from functions.measure_utils import get_file_name
import pandas as pd
from pathlib import Path
from io import StringIO # to make a string into a df
import os
from functions.calc_measures import (
    # count measures
    get_word_count, get_verb_count,
    get_object_count, get_sentence_count,

    # complexity measures
    words_per_sentence, verbs_per_sentence,
    passive_verbs_per_sentence, kana_sisters_verb_per_sentence,
    relative_clauses_per_sentence, adjuncts_per_sentence, 
    conjunctions_per_sentence, objects_per_sentence, 
    idafa_per_sentence, nominalization_per_sentence, 
    )

def get_measures(df, filename):
    word_count = get_word_count(df)
    verb_count = get_verb_count(df)
    object_count = get_object_count(df)
    sentence_count = get_sentence_count(df)

    word_ratio = words_per_sentence(df)
    verb_ratio = verbs_per_sentence(df)
    passive_verb_ratio = passive_verbs_per_sentence(df)
    kana_sisters_verb_ratio = kana_sisters_verb_per_sentence(df)
    object_ratio = objects_per_sentence(df)
    rel_ratio = relative_clauses_per_sentence(df)
    adjunct_ratio = adjuncts_per_sentence(df)
    conjunction_ratio = conjunctions_per_sentence(df)
    idafa_ratio = idafa_per_sentence(df)        
    nominalization_ratio = nominalization_per_sentence(df)
    
    result_dict = {
        'File': 'NA',
        'number_of_words_in_text': word_count,
        'number_of_verbs_in_text': verb_count,
        'number_of_objects_in_text': object_count,
        'number_of_sentences_in_text': sentence_count,
        'number_of_words_per_sentence': word_ratio,
        'number_of_verbs_per_sentence': verb_ratio,
        'number_of_passive_verbs_per_sentence': passive_verb_ratio,
        'number_of_kana_sisters_verbs_per_sentence': kana_sisters_verb_ratio,
        'number_of_objects_per_sentence': object_ratio,
        'number_of_relative_clauses_per_sentence': rel_ratio,
        'number_of_adjuncts_per_sentence': adjunct_ratio,
        'number_of_coordinates_per_sentence': conjunction_ratio,
        'number_of_idafa_per_sentence': idafa_ratio,
        'number_of_nominalizations_per_sentence': nominalization_ratio
    }
    
    return result_dict

def measures(input_files, output_folder):

    complexity_results = []  # initiate a list

    output_folder_path = Path(output_folder)
    os.makedirs(output_folder_path, exist_ok=True)

    for input_file_path in input_files:
        input_file = Path(input_file_path)
        print(f'Processing {input_file.name}')

        # Read the CSV file
        df = pd.read_csv(input_file)

        # get and attach name info
        file_name = get_file_name(input_file_path)

        # append results to the list
        result_dict = get_measures(df, file_name)
        complexity_results.append(result_dict)
        result_dict['File'] = file_name

    # create a df from list -> string to csv
    result_df = pd.DataFrame(complexity_results)
    csv_string = result_df.to_csv(index=False)
    results_file = StringIO(csv_string)

    # Check if the DataFrame is not empty before attempting to read
    if not result_df.empty:
        csv_file = pd.read_csv(results_file)

        # Save the concatenated CSV file
        final_output_csv = output_folder_path / "final_output.csv"
        csv_file.to_csv(final_output_csv, index=False)

        return final_output_csv
    

if __name__ == '__main__':
    measures()