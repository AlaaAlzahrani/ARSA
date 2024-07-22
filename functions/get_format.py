import os
import pandas as pd
from pathlib import Path
from functions.general_utils import create_temp_directory, create_subfolder

def format_and_save_text(file_paths, temp_dir):
    
    formatted_files = []
    common_subfolder = create_subfolder(temp_dir, "formatted_files")

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # create a dataframe from the text file
        df = pd.DataFrame({'TextColumn': lines})
        df = df[df['TextColumn'].str[0].str.isnumeric()]

        # split the text column into multiple columns
        split_columns = df['TextColumn'].str.extractall('(\S+)').unstack()
        num_cols = split_columns.shape[1]
        column_names = [f'C{i+1}' for i in range(num_cols)]
        df[column_names] = split_columns
        
        # drop the text column and any columns with all missing values
        df = df.drop(columns=['TextColumn'])
        df = df.loc[:, (df != '_').any()]

    # rename columns to have more informative names
        df.rename(columns={'C1': 'sent_elements',
                       'C2': 'actual_token',
                       'C3': 'lemma_token',
                       'C4': 'pos',
                       'C6': 'pos_ud',
                       'C7': 'dep_relation',
                       'C8': 'dep_type'}, inplace=True)

        # add 'root' info to the dep_type column
        if 'dep_type' in df.columns:
            df['dep_type'] = df['dep_type'].replace('---', 'ROOT')

        # add a column to identify the sentence number
        df['sent_num'] = df['sent_elements'].eq('1').cumsum()
        df = pd.concat([df['sent_num'], df.drop('sent_num', axis=1)], axis=1)

        # prepare the data for shifting
        df['pos'] = df['pos'].replace('_', pd.NA).astype('string')
        df = df.replace('_', '')

        # shift mislocated values to the right starting from a speific column
        if df['pos'].isna().any():
            mislocated_values = df.loc[:, 'pos'].isna()
            df.loc[mislocated_values, 'pos':] = df.loc[mislocated_values, 'pos':].shift(1, axis=1)
            df = df.drop(columns=['C5', 'C10']) # drop unwanted columns

        # save the formatted file
        file_stem = os.path.splitext(Path(file_path).name)[0]
        
        # use a unique file name within the common subfolder
        output_file_path = os.path.join(common_subfolder, f"{file_stem}.csv")
        df.to_csv(output_file_path, index=False)
        print(f'Formatted file created at: {output_file_path}')
        
        formatted_files.append(output_file_path)

    return formatted_files


def formatting(input_file_paths, temp_dir):
    
    formatted_files = format_and_save_text(input_file_paths, temp_dir)
    return formatted_files

if __name__ == '__main__':
    formatting()

