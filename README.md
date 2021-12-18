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
    - Removed stop words (commonly used words in the English language, i.e. "a", "the", "is", "are")
    - Tokenized the text (splitting a sentence into individual words)
    - Lemmatized each word (removing inflections and grouping words by their lemma)


## Modeling
<p align="center">
  <img src="https://github.com/kevogil/fake-news-prediction/blob/b81944321bf893a4a6958a64305c6cadd3220a99/static/images/ml_summary.png">
</p>


## Visualizations

### Confusion Matrix
Logistic Regression was used to train our machine learning model.
The training data yielded in an accuracy score of 99.5%.
The testing data yielded in an accuracy score of 99.1%.
<p align="center">
  <img src="https://github.com/kevogil/fake-news-prediction/blob/720e122b2b890e01137c301a6a5413f69c2e6dd9/static/images/conf_matrix.png">
</p>

### Bar Chart
Our dataset could be classified into three main topics - Politics, World News, and U.S. News.
A majority of our training data consisted of news topics related to politics.
Understanding this, the confidence of the model returning an accurate prediction on non-political news is not great.
<p align="center">
  <img src="https://github.com/kevogil/fake-news-prediction/blob/720e122b2b890e01137c301a6a5413f69c2e6dd9/static/images/bar_chart.png">
</p>

### Stacked Bar Chart
We were interested in looking at the top words that showed up in our dataset, as well as what the distribution of the words being found in fake and real news looked like.
The top words were mainly related to U.S. presidents, most notably Donald Trump.
Interestingly, news articles related to Obama and Clinton had a higher distribution of fake news compared to Donald Trump.
<p align="center">
  <img src="https://github.com/kevogil/fake-news-prediction/blob/720e122b2b890e01137c301a6a5413f69c2e6dd9/static/images/stacked_bar.png">
</p>

### Word Cloud
Our initial dataset consisted of 10,607,577 words across all of the news articles combined.
After pre-processing our data from removing stop words and lemmatization, our final dataset consisted of 214,805 unique words.
The following word cloud was a visual depiction of all of the unique words trained into our model, varying in size depending on the frequency they showed up across all trained news articles.
<p align="center">
  <img src="https://github.com/kevogil/fake-news-prediction/blob/720e122b2b890e01137c301a6a5413f69c2e6dd9/static/images/word_cloud.png", width="500", height="500">
</p>