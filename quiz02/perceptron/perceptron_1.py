import torch
import torch.nn as nn
import torch.optim as optim

class Perceptron(nn.Module):
    def __init__(self, input_size):
        super(Perceptron, self).__init__()
        self.linear = nn.Linear(input_size, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))
    
X = torch.tensor([[0., 0.], [0., 1.],[1., 0.],[1., 1.]])
y = torch.tensor([[0.], [1.], [1.], [0.]])

model = Perceptron(2)
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

epochs = 300
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

    if(epoch+1) % 50 == 0:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

with torch.no_grad():
    y_predicted = model(X)
    y_predicted_cls = y_predicted.round()
    accuracy = y_predicted_cls.eq(y).sum() / float(y.shape[0])
    print(f'Accuracy : {accuracy:.4f}')