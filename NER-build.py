from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import csv


def ret_loc_ner(tweet):
    st = StanfordNERTagger('stanford_ner/english.all.3class.distsim.crf.ser.gz',
					   'stanford_ner/stanford-ner.jar',
					   encoding='utf-8')

    tokenized_text = word_tokenize(tweet)
    classified_text = dict(st.tag(tokenized_text))

    list_of_locations = []
    for word, entity in classified_text.items():
        if entity == "LOCATION":
            list_of_locations.append(word)

    return list_of_locations

    # print(classified_text)

def get_loc_from_tweets():
    with open('Data/geocode_csv.csv', encoding='utf8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        with open('Data/ner_output_final.csv', "w") as csv_file:
            for row in reader:
                    writer = csv.writer(csv_file, delimiter="|")
                    writer.writerow(ret_loc_ner(row[0]))
                    csv_file.flush()

                # print(ret_loc_ner(row[0]))


get_loc_from_tweets()