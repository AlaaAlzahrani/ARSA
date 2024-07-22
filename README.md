---
title: "README file"
output:
  html_document:
    theme: simplex
    css: styles.css
---

# [The Arabic Syntactic Analyzer (ARSA)](https://github.com/AlaaAlzahrani/ARSA)


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Table of Contents
- [Overview](#overview)
- [Notable Features](#notable-features)
- [Installation and Setup for Windows users](#installation-and-setup-for-windows-users)
- [Installation and Setup for Mac/Linux Users](#installation-and-setup-for-maclinux-users)


## Overview 🔍

The Arabic Syntactic Analyzer (ARSA) is an open-source Natural Language Processing (NLP) tool designed for the analysis of syntactic features in Arabic written texts. It is based on python and employs the [camel_parser](https://github.com/CAMeL-Lab/camel_tools) library to identify and measure 13 distinct syntactic indices, comprising 9 syntactic complexity indices and 4 syntactic fluency indices. 

The ARSA tool can be applied to study the following topics:

- *Writing assessment*: evaluating syntactic features in Arabic compositions
- *Text readability*: investigating the linguistic accessibility of Arabic texts
- *Second language acquisition*: analyzing syntactic development in Arabic learners' writing

## Notable Features 

- **Automatic Analysis**: automatically evaluates 13 syntactic indices
- **Batch Processing**: capable of analyzing multiple text files simultaneously 
- **User-Friendly Interface**: implemented as an interactive command-line interface (CLI) for ease of use 
- **Dual Functionality**: operates as both a local application and a cloud-based tool via Google Colab 

## Installation and Setup for Windows users 🖥️

1. **Download the [ARSA_notebook.ipynb](https://github.com/AlaaAlzahrani/ARSA/blob/master/ARSA_notebook.ipynb) from this repository**

2. **Open [Google Colab](https://colab.research.google.com)**

3. **Upload the notebook:**
    - Go to '*File*' -> '*Upload notebook*'
    - Select the downloaded '*ARSA_notebook.ipynb*'

4. **Follow the step-by-step instructions within the notebook**


> *NOTE*: You can run the notebook on Mac and Linux devices. 


## Installation and Setup for Mac/Linux users 🐧🍎

1. **Clone this repository:**
```bash
git clone https://github.com/AlaaAlzahrani/ARSA.gitL
```

2. **Install the required packages:**

```bash
cd ARSA/camel_parser
pip install -r requirements.txt
python download_models.py
camel_data -i morphology-db-msa-s31
camel_data -i disambig-bert-unfactored-msa
```

```bash
cd ..
pip install -r ARSA_requirements.txt
```

```bash
pip install --upgrade huggingface_hub
pip install camel-tools
```

3. **Analyze your texts using the ARSA tool**

Run the following command:

```bash
cd path/to/ARSA/directory # change the working dircotry to the ARSA repository folder
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

4. Example
```bash
cd D:/my_projects/ARSA 
python get_analysis.py
Please select the text file(s) folder: example/corpus
Please select the output folder: example/results
```

> *NOTE*: This local installation method is currently unsupported on Windows because some dependencies of the camel parser library are incompatible with Windows.


## Citation

If you use this tool, please cite the following papers to support the authors and encourage the development of open-source Arabic language processing tools:

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


<style>
  blockquote { 
    background-color: #f0f8ff;
    border-left: 5px solid #87ceeb;
    margin: 1em 0;
    padding: 10px 20px;
    color: #333;
  }
</style>