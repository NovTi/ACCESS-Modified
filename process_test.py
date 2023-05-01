import pdb
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def clause_dependency_ratio(complex_sentence, simple_sentence):
    comp_clauses = nltk.sent_tokenize(complex_sentence)
    simple_clauses = nltk.sent_tokenize(simple_sentence)

    comp_dependent_clauses = []
    simple_dependent_clauses = []
    for clause in comp_clauses:
        words = nltk.word_tokenize(clause)
        tags = nltk.pos_tag(words)
        for i in range(len(tags)):
            if tags[i][1] == 'IN':
                dependent_clause = ' '.join(words[i+1:])
                comp_dependent_clauses.append(dependent_clause)

    for clause in simple_clauses:
        words = nltk.word_tokenize(clause)
        tags = nltk.pos_tag(words)
        for i in range(len(tags)):
            if tags[i][1] == 'IN':
                dependent_clause = ' '.join(words[i+1:])
                simple_dependent_clauses.append(dependent_clause)
                
    if(len(comp_dependent_clauses) > 0 and len(simple_dependent_clauses) > 0):
        return int(len(comp_dependent_clauses)/len(simple_dependent_clauses))
    elif(len(comp_dependent_clauses) > 0):
        return len(comp_dependent_clauses)
    else:
        return int(1.0)

def pos_compression_ratio(complex_sentence, simple_sentence):

    comp_words = nltk.word_tokenize(complex_sentence)
    simple_words = nltk.word_tokenize(simple_sentence)
    comp_tags = nltk.pos_tag(comp_words)
    comp_distinct_tags = set(tag[1] for tag in comp_tags)
    simple_tags = nltk.pos_tag(simple_words)
    simple_distinct_tags = set(tag[1] for tag in simple_tags)

    return int(len(comp_distinct_tags)/len(simple_distinct_tags))

if __name__ == '__main__':
    compx = 'The Empire of Nicaea succeeded in capturing Constantinople and the rest of the Latin Empire , thus re-establishing the Byzantine Empire .'
    simple = 'The Byzantine Empire came back when the Empire of Nicaea captured Constantinople and the Latin Empire .'
    r1 = clause_dependency_ratio(compx, simple)
    r2 = pos_compression_ratio(compx, simple)
    pdb.set_trace()
