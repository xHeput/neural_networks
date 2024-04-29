import torch
from torch import nn
from torch.utils.data import DataLoader  # do danych
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler  # do skalownia



class Dane(torch.utils.data.Dataset):
  def __init__(self, x, y, scale = True):
    if not torch.is_tensor(x) and not torch.is_tensor(y):
      if scale:
        x = StandardScaler().fit_transform(x)
      self.x = torch.from_numpy(x)
      self.y = torch.from_numpy(y)
  # check len of dataset
  def __len__(self):
    return len(self.x)
  # takes sample from indices dataset
  def __getitem__(self, i):
    return self.x[i], self.y[i]

class MLP(nn.Module):
  def __init__(self):
    super(MLP, self).__init__()
    # layers structure
    self.layers = nn.Sequential(nn.Linear(13, 50),
                                nn.ReLU(),
                                nn.Linear(50, 25),
                                nn.ReLU(),
                                nn.Linear(25, 1))
  def forward(self, x):
    return self.layers(x)


boston = fetch_openml(name = 'boston', version = 1)
x = boston.data
y = boston.target
y = y.to_numpy()
dane = Dane(x, y)

mdl = MLP()
loss = nn.MSELoss()
n = 10  # num of epochs
opt = torch.optim.Adam(mdl.parameters(), lr = 0.01)

train = torch.utils.data.DataLoader(dane, batch_size = 10, shuffle = True)

for epoch in range (0, n):
  print("Epoka ", epoch + 1)
  for i, data in enumerate(train, 0):
    input, output = data
    input = input.float()
    output = output.float()

    opt.zero_grad()
    calc_output = mdl(input)
    waste = loss(calc_output, output)
    waste.backward()
    opt.step()
