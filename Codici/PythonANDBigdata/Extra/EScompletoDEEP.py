import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist

# 1. Caricamento e preparazione dei dati
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalizzazione

# 2. Definizione del modello
model = Sequential([
    Flatten(input_shape=(28, 28)),             # Appiattimento dell'immagine
    Dense(128, activation='relu'),            # Livello nascosto
    Dense(10, activation='softmax')           # Livello di output
])

# 3. Compilazione e addestramento
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)

# 4. Valutazione del modello
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"Accuratezza sul set di test: {test_accuracy * 100:.2f}%")
