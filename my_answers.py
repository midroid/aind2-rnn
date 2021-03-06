import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = []
    y = []
    index = 0
    while index + window_size < len(series):
        X.append(series[index:index+window_size])
        y.append(series[index+window_size])
        index += 1
    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape=(window_size, 1)))
    model.add(Dense(1))
    model.summary()
    return model


### TODO: return the text input with only ascii lowercase and the punctuation given below included.
def cleaned_text(text):
    # punctuation = ['!', ',', '.', ':', ';', '?']
    import re
    import string

    LETTERS = string.ascii_letters
    PUNCTUATION = ',.\'!?;:'

    text = text.replace("'", "?")
    # find all unique characters in the text
    uniques = ''.join(set(text))

    # remove as many non-english characters and character sequences as you can 
    for char in uniques:
        if char not in LETTERS and char not in PUNCTUATION:
            text = text.replace(char, ' ')


    return text

### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text, window_size, step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []

    index = 0
    while index + window_size < len(text):
        inputs.append(text[index:index+window_size])
        outputs.append(text[index+window_size])
        index += step_size

    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size, num_chars):
    model = Sequential()
    # Layer 1, the LSTM module with 200 hidden units
    model.add(LSTM(200, input_shape=(window_size, num_chars)))
    # Layer 2, a fully-connected layer with softmax activation function
    model.add(Dense(num_chars, activation='softmax'))
    model.summary()
    return model
