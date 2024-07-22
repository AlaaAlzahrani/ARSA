# The Arabic Syntactic Analyzer (ARSA) 

## Overview 🔍

The Arabic Syntactic Analyzer (ARSA) is a Natural Language Processing (NLP) tool designed for the analysis of syntactic features in Arabic written texts. It employs the [camel_parser](https://github.com/CAMeL-Lab/camel_tools) library to identify and measure 13 distinct syntactic indices, comprising 9 syntactic complexity indices and 4 syntactic fluency indices. 

The ARSA tool can be applied to study the following topics:

- *Writing assessment*: evaluating syntactic features in Arabic compositions
- *Text readability*: determining the linguistic accessibility of Arabic texts
- *Second language acquisition*: analyzing syntactic development in Arabic learners' writing

## Key Features 

- **Comprehensive Analysis**: Evaluates 13 syntactic indices 
- **Dual Functionality**: Operates as both a local application and a cloud-based tool via Google Colab 
- **Batch Processing**: Capable of analyzing multiple text files simultaneously 
- **User-Friendly Interface**: Implemented as an interactive command-line interface (CLI) for ease of use 

## Installation and Setup 🛠️

1. **Clone this repository:**
```bash
git clone <REPOSITORY_URL>
```

2. **Install the required packages:**

```bash
cd ARSA_tool\camel_parser
pip install -r requirements.txt
python download_models.py
camel_data -i morphology-db-msa-s31
camel_data -i disambig-bert-unfactored-msa
```

```bash
cd ARSA_tool
pip install -r ARSA_requirements.txt
```

3. **Analyze your texts using the ARSA tool**

Run the following command:

```bash
python get_analysis.py
```

The command will prompt you to enter the input folder:

```bash
Please select the text file(s) folder: <write-the-input-folder-name-here>
```

The command will also prompt you to enter the output folder:

```bash
Please select the output folder: <write-the-output-folder-name-here>
```

## Example
```bash
python get_analysis.py
Please select the text file(s) folder: example/corpus
Please select the output folder: example/results
```

## Citation

If you use this tool, please cite the following papers to support the creators and encourage research on open-source Arabic processing tools:

```bibtex
@inproceedings{Elshabrawy:2023:camelparser,
    title = "{CamelParser2.0: A State-of-the-Art Dependency Parser for Arabic}",
    author = {Elshabrawy, Ahmed and AbuOdeh, Muhammed and Inoue, Go and Habash, Nizar},
    booktitle = {Proceedings of The First Arabic Natural Language Processing Conference (ArabicNLP 2023)},
    year = "2023"
}
```

```bibtex
@misc{Alzahrani:2024:ARSA,
    title = "{Arabic Syntactic Analyzer (ARSA): An Automated Tool for the Analysis of Arabic Written Texts}",
    author = {Alzahrani, Alaa and Alfaify, Adel},
    year = "2024",
    note = {Preprint}
}
```