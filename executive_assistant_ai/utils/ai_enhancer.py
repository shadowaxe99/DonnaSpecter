```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class AIEnhancer:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = keras.Sequential()
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))
        model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        return model

    def train_model(self, train_data, train_labels):
        self.model.fit(train_data, train_labels, epochs=10, batch_size=32)

    def enhance(self, data):
        prediction = self.model.predict(data)
        return prediction
```