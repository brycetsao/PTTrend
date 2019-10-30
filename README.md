# Introduction
This project uses scikit Bayesian algorithms to determine if a particular PTT article is politics-related.

We first use the Python Jieba library to separate Chinese words (斷詞) , and extract words as ***features*** for Bayesian algorithm. (Each word is a feature.)

Basically, with Bayesian algorithm, we can know that if a feature likely indicates the entire article (which contains a lot of features) is politics-related. For instance, a article containing the word "民進黨" is somewhat likely to be politics-related, even further, if the article also contains words like  "行政院", "立法院", "立委", "法條", it becomes highly likely that the article is politics-related.

We can know the degree of indication of each feature by extracting features and counting them in the training set. In the training set, there are lots of articles already labelled as politics-related or non politics-related. For example, in all politics-related articles in the training set, 90% of them contains "民進黨", then we know that "民進黨" is probably a political word, which means if an un-labelled article contains "民進黨", the article is likely to be politics related. But for words like "你們", it is likely that all articles, whether political or not, have about the same probablity of containing the word "你們", so it is a neutral word, we cannot infer from the word that if the article containing it is political.

# Demo
http://pttrend.nctu.me:3000

# Installation
On Ubuntu:

````
sudo apt install python3-pip python3-scipy python3-numpy
sudo pip3 install jieba sklearn

sudo pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp34-cp34m-linux_x86_64.whl
````

# Run
You can directly use our scraped PTT Gossiping articles, from `ptt.db`, if you would like to scrape the latest data, please run `parser.rb`.

Follow the steps to predict if a article is politics-related:

## Hand-pick the training set
In `ptt.db` we have already labelled a small part of articles as politics-related or non-politics-related, so you can skip this step, but if you would like to make a bigger training set, you can use the script `handpick_trainingset.py` to manually label them.

## Predict
Use `pttrend.py` to predict if you content is political. There are two ways to make predictions:

1. Use `-i` command line option to read content from stdin and make prediction, for example:
````
echo "民進黨" | python3 pttrend.py -i
````

2. Use `-p [id]` to read existing articles from the database and make prediction:
````
python3 pttrend.py -p 1000
````
