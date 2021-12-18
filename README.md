# Fake News Prediction

## Dataset
The dataset used to train our machine learning model was obtained from Kaggle, consisting of news articles and posted between 2015-2018.
Two sets of data were used, one consisting of all fake news, and another of all real news.
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


## Visualizations

### Confusion Matrix
Logistic Regression was used to train our machine learning model.
The training data yielded in an accuracy score of 99.5%.
The testing data yielded in an accuracy score of 99.1%.
<p align="center">
  <img src="https://github.com/kevogil/fake-news-prediction/blob/720e122b2b890e01137c301a6a5413f69c2e6dd9/static/images/conf_matrix.png">
</p>

## Bar Chart
Our dataset could be classified into three main topics - Politics, World News, and U.S. News.
A majority of our training data consisted of news topics related to politics.
Understanding this, the confidence of the model returning an accurate prediction on non-political news is not great.
<p align="center">
  <img src="https://github.com/kevogil/fake-news-prediction/blob/720e122b2b890e01137c301a6a5413f69c2e6dd9/static/images/bar_chart.png">
</p>