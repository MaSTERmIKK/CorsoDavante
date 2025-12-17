# Importiamo le librerie principali
import torch
import torch.nn as nn
import torch.optim as optim

# 1. Creazione di tensori
# Tensore di numeri casuali (3 righe, 4 colonne)
x = torch.rand(3, 4)  # Tensore casuale
y = torch.ones(3, 4)  # Tensore pieno di 1
z = torch.zeros(3, 4)  # Tensore pieno di 0

# Operazioni sui tensori
result = x + y  # Somma di tensori
result = result * 2  # Moltiplicazione scalare

# 2. Autograd: Calcolo automatico dei gradienti
# Creiamo un tensore con `requires_grad=True` per tracciare le operazioni
a = torch.tensor([2.0, 3.0], requires_grad=True)
b = a**2 + 3 * a + 1  # Funzione su cui calcoleremo il gradiente
b.sum().backward()  # Calcolo del gradiente

# I gradienti sono ora memorizzati in `a.grad`
print(a.grad)  # Output: tensor([7., 9.])

# 3. Definizione di un modello semplice
# Costruiamo un modello feed-forward con PyTorch
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(2, 1)  # Layer lineare con 2 input e 1 output

    def forward(self, x):
        return self.linear(x)

model = SimpleModel()

# 4. Definizione della funzione di perdita e dell'ottimizzatore
criterion = nn.MSELoss()  # Funzione di perdita MSE (Mean Squared Error)
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Ottimizzatore SGD con learning rate 0.01

# 5. Addestramento del modello
# Simuliamo un dataset di input e target
inputs = torch.tensor([[1.0, 2.0], [2.0, 3.0]], requires_grad=True)
targets = torch.tensor([[5.0], [8.0]])

# Loop di addestramento
for epoch in range(100):  # Eseguiamo 100 epoch
    # Forward pass: calcolo delle predizioni
    outputs = model(inputs)

    # Calcolo della perdita
    loss = criterion(outputs, targets)

    # Resettiamo i gradienti accumulati
    optimizer.zero_grad()

    # Backward pass: calcolo del gradiente
    loss.backward()

    # Aggiornamento dei pesi
    optimizer.step()

    # Output del progresso
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

# 6. Valutazione del modello
with torch.no_grad():  # Disabilitiamo il calcolo del gradiente per la valutazione
    test_input = torch.tensor([[3.0, 4.0]])
    prediction = model(test_input)
    print(f'Prediction: {prediction}')
