import torch
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(512 * 512 * 4, 128),
            nn.ReLU(),
            nn.Linear(128, 512 * 512 * 3),
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x).view(-1, 3, 512, 512)

class ConditionalGAN:
    def __init__(self):
        self.generator = Generator()

    def generate(self, foreground, alpha):
        input_tensor = torch.cat([torch.tensor(foreground), torch.tensor(alpha[:, :, None])], dim=2).view(1, -1)
        return self.generator(input_tensor).detach().numpy()
