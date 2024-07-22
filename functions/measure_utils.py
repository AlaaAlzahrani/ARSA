import os


### helper functions ###

def get_file_name(path):
    file_name = os.path.basename(path).split('.')[0]
    return file_name


def get_total_sentences(df):
    return df['sent_num'].nunique()


### syntactic complexity functions ###
# measure 1
def get_total_word_count(df):
    return df[df['pos'] != 'PNX']['lemma_token'].count()


# measure 2
def get_total_verb_count(df):
    return (df['pos'].astype(str).apply(lambda x: 'VRB' in x)).sum(skipna=True)


# measure 3
def get_total_passive_verb_count(df):
    return (df['pos'].astype(str).apply(lambda x: 'PASS' in x)).sum(skipna=True)


# measure 4
def get_total_kana_sisters_verb_count(df):

    # specify values to check for (11 verbs)
    kana_sisters_list = ["كان", "أمسى", "أصبح", "أضحى", "بات", "صار", "ظل", "فتئ", "برح", "زال", "دام"]

    # condition 1
    kana_mask = df['lemma_token'].isin(kana_sisters_list) & (df['pos'] == "VRB")
    
    # condition 2 (to check that the sentence is nominal)
    following_mask = (df['pos'].shift(-1) != 'VRB') & (df['pos'].shift(-2) != 'VRB')
    
    # Combine conditions
    final_condition = kana_mask & following_mask
    
    # Calculate count
    total_kana_sisters_verb = final_condition.sum()
    
    return total_kana_sisters_verb


# measure 5
def get_total_object_count(df):
    return ((df['dep_type'].apply(lambda x: 'OBJ' in x)).sum())


# measure 6
def get_total_relative_clauses(df):

    # specify values to check for (12 items)
    rel_clause_list = ['الذي', 'اللذان', 'اللذين', 'الذين', 'التي', 'اللتين', 'اللتان', 'اللواتي', 'اللائي', 'ذو', 'ذات', 'ذوات']

    # condition
    rel_condition = df['lemma_token'].isin(rel_clause_list) & (df['dep_type'] == 'MOD')

    # calculate count
    total_rel = rel_condition.sum()
    return total_rel


# measure 7
def get_total_adjuncts(df):

    # specify values to check for 
    adjunct_list = ['أينما', 'حيث', 'حيثما', 'عندما', 'حين', 'كلما', 'لما', 'بينما', 'لأن', 'إذ', 'إذا', 'حتى', 'كي', 'لولا', 'إذا', 'إن', 'لو', 'رغم', 'إلا']
    pos_ud_values = ['SCONJ', 'NOUN', 'ADP', 'PROPN']

    # set condition 1: if token is in adjunct list AND has one of the required pos_ud values
    adj_condition1 = df['lemma_token'].isin(adjunct_list) & df['pos_ud'].str.contains('|'.join(pos_ud_values))

    # set condition 2: if two specific subsequent tokens (token 1 and 2) constitute one adjunct, count as 1 instance
    adj_condition2 = (df['lemma_token'] == 'ل+') & (df['lemma_token'].shift(-1) == 'أن')

     # calculate count
    total_adjuncts = (adj_condition1 | adj_condition2).sum()

    return total_adjuncts


# measure 8
def get_total_conjunctions(df):

    # specify values to check for 
    conj_list = ['ثم', 'أو', 'أم', 'لكن', 'و+', 'ف+']

    # condition
    conj_condition = df['lemma_token'].isin(conj_list) & (df['pos_ud'].str.contains('ud=CCONJ'))

    # calculate count
    total_conj = conj_condition.sum()

    return total_conj


# measure 9
def get_total_idafa_count(df):
    return ((df['dep_type'] == 'IDF') & (~df['pos_ud'].str.contains('ud=PRON'))).sum()


# measure 10
def get_total_nominalization_count(df):

    # conditions
    nominalization_conditions = (
        ~((df['pos_ud'].str.contains("ud=NOUN")) & (df['pos_ud'].shift(-1).str.contains("ud=NOUN"))) &
        ~df['dep_type'].str.contains("MOD") &
        df['pos_ud'].str.contains("ud=NOUN") &
        df['pos_ud'].str.contains("num=s") &
        df['pos_ud'].str.contains("rat=i") &
        (df['lemma_token'].apply(len) >= 5)
    )

    # calculate count
    total_nominalizations = nominalization_conditions.sum()

    return total_nominalizations


