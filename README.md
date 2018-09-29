# A Survey on the relevance between the location-information in twitter description and tagged location
A project that was developed to find the relevence between the location information in the description of the tweets and the tagged location and classify them as Perfect Match, Partial Match, Regional Match and No Match.

| Twitter Description  | Tagged Location | Match |
| ------------- | ------------- | ------------- |
| I am in New York  | New York  | Perfect Match  |
| Obama gave a speech in Chicago  and Milwaukee | Chicago  | Partial Match  |
| I was in Austin  | Texas  | Regional Match  |
| I am travelling to Seattle  | Vancouver  | No Match  |

# Criteria
Perfect Match - If the location information in the twitter description and the tagged location are the same \
Partial Match - If one of the locations in the twitter description matches the tagged location \
Regional Match - If the location in the twitter description is a part of the tagged loation and viceversa (a city in a state) \
No Match - If the location in the twitter description and the tagged location are different

# Requirements
* Python 3.6.3
* tweepy
* nltk
* pygeocoder
* matplotlib
* Pycharm or suitable IDE

# Data Set
Twitter data set of the months of October 2016 and November 2016
