import torch
import matplotlib.pyplot as plt

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using device:", device)

size = 256

x = torch.arange(size, device=device)
y = torch.arange(size, device=device)

print("x shape:", x.shape)
print("y shape:", y.shape)

Y, X = torch.meshgrid(y, x, indexing="ij")

print("X shape:", X.shape)
print("Y shape:", Y.shape)

difference = Y - X

triangle_mask = X <= Y

and_result = torch.bitwise_and(X, difference)

sierpinski = triangle_mask & (and_result == 0)

plt.imshow(sierpinski.cpu().numpy(), cmap="gray")
plt.axis("off")
plt.show()