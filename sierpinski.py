import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

size = 256

x = torch.arange(size, device=device)
y = torch.arange(size, device=device)

print("x shape:", x.shape)
print("y shape:", y.shape)