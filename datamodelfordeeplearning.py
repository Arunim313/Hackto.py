from keras.datasets import mnist

data = mnist.load_data( )

((X_train, y_train), (X_test, y_test)) = data

X_train = X_train.reshape((X_train.shape[0],  28*28)).astype('float32')
X_test = X_test.reshape((X_test.shape[0],  28*28)).astype('float32')
X_train = X_train / 255
X_test = X_test / 255
from keras.utils import np_utils

print(y_test.shape)

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

num_classes = y_test.shape[1]
print(y_test.shape)

from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(32,  input_dim = 28*28,  activation = 'relu'))
model.add(Dense(64,  activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))
model.compile( loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'] )
model.summary( )
model.fit(X_train, y_train, epochs=10, batch_size=100)
scores = model.evaluate(X_test, y_test)
print(scores)
