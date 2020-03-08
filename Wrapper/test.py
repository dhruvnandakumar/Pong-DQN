import torch
import math

a = torch.ones((2, 2), requires_grad=True)

b = a + 5
c = b.mean()
print(b , c)

print(a.grad)

c.backward()

print(a.grad)