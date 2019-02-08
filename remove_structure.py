import re, sys

def split_corpus_into_sentences(corpus):
    with open(corpus, "r") as f:
        text = f.read()
        sentences = text.split("\n\n")
    return sentences

def destroy(sentence):
    POS_tagged = r"(\([^()]*\))"
    destroyed_sentence = " ".join(re.findall(POS_tagged, sentence))
    return destroyed_sentence

def create_POS_tagged_corpus(corpus, output):
    sents = split_corpus_into_sentences(corpus)
    destroyed_sents = [destroy(sent) for sent in sents]
    with open(output, "w") as f:
        for sent in destroyed_sents:
            f.write(sent)
            f.write("\n\n")

if __name__ == '__main__':

    corpus = "sample_corpus.txt"
    output = "sample_output.txt"

    create_POS_tagged_corpus(corpus, output)
