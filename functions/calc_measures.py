
from ARSA.functions.measure_utils import (
    get_total_word_count, get_total_sentences, 
    get_total_verb_count, get_total_passive_verb_count, 
    get_total_kana_sisters_verb_count, get_total_object_count,
    get_total_relative_clauses, get_total_adjuncts, 
    get_total_conjunctions, get_total_idafa_count, 
    get_total_nominalization_count,
)


### count functions ###
def get_word_count(df):
    word_count = get_total_word_count(df)
    return word_count

def get_verb_count(df):
    verb_count = get_total_verb_count(df)
    return verb_count

def get_object_count(df):
    object_count = get_total_object_count(df)
    return object_count

def get_sentence_count(df):
    sentence_count = get_total_sentences(df)
    return sentence_count


### complexity measure functions ###

# measure 1:
def words_per_sentence(df):

    # calcuate counts
    total_word_count = get_total_word_count(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    word_ratio = total_word_count / total_sentences

    return word_ratio


# measure 2:
def verbs_per_sentence(df):

    # calcuate counts
    total_verb_count = get_total_verb_count(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    verb_ratio = total_verb_count / total_sentences

    return verb_ratio


# measure 3:
def passive_verbs_per_sentence(df):

    # calcuate counts
    total_passive_verb_count = get_total_passive_verb_count(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    passive_verb_ratio = total_passive_verb_count / total_sentences

    return passive_verb_ratio


# measure 4:
def kana_sisters_verb_per_sentence(df):

    # calcuate counts
    total_kana_sisters_verb_count = get_total_kana_sisters_verb_count(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    kana_sisters_ratio = total_kana_sisters_verb_count / total_sentences

    return kana_sisters_ratio


# measure 5:
def objects_per_sentence(df):

    # calcuate counts
    total_object_count = get_total_object_count(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    object_ratio = total_object_count / total_sentences

    return object_ratio


# measure 6:
def relative_clauses_per_sentence(df):

    # calcuate counts
    total_relative_clauses = get_total_relative_clauses(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    rel_ratio = total_relative_clauses / total_sentences

    return rel_ratio


# measure 7:
def adjuncts_per_sentence(df):

    # calcuate counts
    total_adjunct_count = get_total_adjuncts(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    adjunct_ratio = total_adjunct_count / total_sentences

    return adjunct_ratio


# measure 8:
def conjunctions_per_sentence(df):

    # calcuate counts
    total_conjunction_count = get_total_conjunctions(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    conjunction_ratio = total_conjunction_count / total_sentences

    return conjunction_ratio


# measure 9:
def idafa_per_sentence(df):

    # calcuate counts
    total_idafa_count = get_total_idafa_count(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    idafa_ratio = total_idafa_count / total_sentences

    return idafa_ratio


# measure 10:
def nominalization_per_sentence(df):

    # calcuate counts
    total_nominalization_count = get_total_nominalization_count(df)
    total_sentences = get_total_sentences(df)

    # calcuate ratio
    nominalization_ratio = total_nominalization_count / total_sentences

    return nominalization_ratio