import torch

# create a tensor with empty values
x = torch.empty(2, 2, 2, 2)

# create a tensor with random values
x_rand = torch.rand(2, 3)

# print(x + x_rand)

# create a tensor with zeros
x_zeros = torch.zeros(1, dtype=torch.float8_e5m2)
# print(x_zeros)

# check a tensor size
# print(x_rand.size())

# create a tensor from a list
x_list = torch.tensor([1, 2.5, 3])
# print(x_list)

# How to convert / reshape a tensor
x_reshape = torch.rand(4, 4)
y = x_reshape.view(-1, 2, 2, 2)
print(x_reshape)
print(y, y.size())

# numpy cannot handle gpu tensors