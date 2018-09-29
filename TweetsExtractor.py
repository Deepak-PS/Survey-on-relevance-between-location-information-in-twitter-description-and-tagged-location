import csv
import os
from datetime import datetime
import bz2
import re
import simplejson as json
from nltk import word_tokenize

bz2FilePath = '10'
CSVfields = ['text', 'location']
geocounter = 0
totalcounter = 0


def reading(filepath):
    starttime = datetime.now()
    with open('finaltweets_new.csv', 'w', newline='', encoding='utf-8') as csvfile:  ## open the CSV new file
        tweetwriter = csv.DictWriter(csvfile, delimiter=',', fieldnames=CSVfields)  ## initialize the CSV
        tweetwriter.writeheader()  ## write the header of CSV

        for root, dirs, files in os.walk(filepath):  ## read the folder
            for name in files:  ## read the file
                print("PATHHH---------", os.path.join(root, name).capitalize())
                filename = os.path.join(root, name)  ## save the path of the file

                with bz2.BZ2File(filename, 'r') as f:  ## read the BZ file in the path
                    for line in f:  ## read each line
                        tweet = json.loads(line)  ## parse the json
                        try:
                            if tweet['created_at']:
                                if tweet['lang'] == 'en':
                                    tweetbody = getLocAndText(tweet)
                                    if tweetbody:
                                        writeCSV(tweetbody, tweetwriter)
                                        # tweetwriter.writerow(tweetbody)

                        except Exception as e:
                            continue
    endtime = datetime.now()
    print("Geo", geocounter)
    print("Total", totalcounter)
    print("processing time -->", starttime - endtime)


def writeCSV(tbody, writer):
    writer.writerow(tbody)


def getLocAndText(tweet):
    global geocounter
    global totalcounter

    totalcounter = totalcounter + 1
    if tweet['coordinates'] != None:
        geocounter = geocounter + 1
        csvObj = {
            'text': tweet['user']['description'],
            'location': tweet['coordinates']['coordinates']
        }
        return csvObj


reading(bz2FilePath)