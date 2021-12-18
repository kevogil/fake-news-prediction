# Fake News Prediction

## Dataset
The dataset used to train our machine learning model was obtained from Kaggle, consisting of news articles and posted between 2015-2018.

Two sets of data were provided, one consisting of all fake news, and another of all real news.
The overall format and columns were the same across both datasets.

The data consisted of the following fields:<br>
`title` `text` `subject` `date`

<a href="https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset">Link to dataset</a>


## Data Cleaning
The following data cleaning steps were taken:
1. Replace any empty strings with NaN
2. Add a binary column to each dataset, identifying the news articles as either being fake or real (0 = fake, 1 = real)
3. Append datasets into one dataframe
4. Create a new column called `combined_text` that concatenates the `title` and `text` columns
5. Pre-processing:
    - Cleaned text data from `combined_text` using regex (regular expressions)
    - Tokenized the text (splitting a sentence into individual words)
    - Lemmatized each word (removing inflections and grouping words by their lemma)
