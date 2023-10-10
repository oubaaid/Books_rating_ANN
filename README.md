# Books_rating_ANN

I have started the porject with data analysis. Eliminating bad lines with bad seperations included. 
Will not present a big threat because of the small number of lines droped (4 lines).

I have noticed that books having avg_ratings below 2.4 had very little to no reviews at all. So we are not taking them into consideration.
Audio-Books with pages lower than 30 mainly were found to have incorrect number of pages. They are going to be eliminated for giving incorrect input about pages.

Low number of pages was also related mainly to guide-books, children books, etc.. They are not going to be eliminated. High number of pages reaching up to 6576, were 
mainly boxes of multiple books/novels, except some J.K.K books of harry potter which are known to be voluminous or medicinal / pharmeuctical books. So we are keeping them.

Audio-Books with pages lower than 30 mainly were found to have incorrect number of pages. They are going to be eliminated for giving incorrect input about pages.
Low number of pages was also related mainly to guide-books, children books, etc.. They are not going to be eliminated.

books with high ratings_count are in english, and it is true they are the most famous ones.
It is strange to find books with average_rating, but have 0 ratings_count in the other hand. We are going to eliminate them
Also books with low ratings rate are irrelevant to our data and model as well. eliminating them.

The books above 20k text_reviews_count are specials book, however being this uniquene may be irrelevant to our data and can cause confusion to our model. We will eliminate
them. We can eliminate all the other points above the 662 count mark and consider them as outliers. However this can be relevant information to our model as these points have
a progressive pattern.

Seeing that publisher column contains 1491 distinct values, best way to transform it is through Label encoding method. Where each publisher will be assigned to an int64.

language code has the same issue issue, string values are going to be tranformed to int values representing each language.
We are using an encoder for the language and publisher encoding values.

For the publication_date column, we will divide the column into 3 seperate columns, as follow : Month, Day and Year
We convert the 'publication_date' column to datetime with 'coerce' for handling invalid dates

We were wondering about keeping the column "publisher" or not, if it has an actual relevance in terms of data or not.
We can also suppose that in real life some publishers can put work more than others or even have a bigger ability to distribute a book.

Concerning data standarzation and normalization :
Normalization is used when the data doesn't have Gaussian distribution whereas Standardization is used on data having Gaussian distribution. Normalization scales in a
range of [0,1] or [-1,1]. Standardization is not bounded by range. Normalization is highly affected by outliers.
In Normalisation, the change in values is that they are at a standard scale without distorting the differences in the values. Whereas, Standardisation assumes that the
dataset is in Gaussian distribution and measures the variable at different scales, making all the variables equally contribute to the analysis.

avg_ratings which is our target column is normaly distributed, which is a good sign.

I have split our data to data and target (x and y), then split our data randomly to test and train blocks, with a test size of 20% of the total dataset.

I have also noticed some nan rows are causing nan loss function and 0 accuracy metric after final standarzation
We perform a row dropping action to eliminate these nan values in both train and test data

For model training, I started with Classic AdaBoost model, then simple linear regression, moving to Randomforest.
We went for an Artificial Neural Neutwork with 1 input layer, 2 hiden layers and 1 output layer.
Initializing network and adding the first fully-connected layer having 7 neurons for 7 inputs, choosing relu first for being a suitable rectifier activation function,
and for it's simplicty + ability to overcome limitations

I have chosen to go with ANN model, due to the good score it gave us compared to other models. It is also important to have a model that is capable of understanding hiden parameters in the data, and deal with enormous amount of data in the long run.
Also, Neural Networks are cool !

I used Recall for the ANN model, because it shows whether an ML model can find all objects of the target class. Also, Recall is a metric that quantifies the number of correct positive predictions made out of
all positive predictions that could have been made. Unlike precision that only comments on the correct positive predictions out of all positive predictions,
recall provides an indication of missed positive predictions.

This is our model's architecture :
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense (Dense)               (None, 8)                 72        
                                                                 
 dense_1 (Dense)             (None, 5)                 45        
                                                                 
 dense_2 (Dense)             (None, 1)                 6         
                                                                 
=================================================================
Total params: 123 (492.00 Byte)
Trainable params: 123 (492.00 Byte)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________

Finally to deploy our model using spark library. Type "python app.py" in your terminal pointing straight to the path of your app.py file
