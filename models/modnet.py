import torch
import torch.nn as nn
import torch.nn.functional as F

class MODNet(nn.Module):
    def __init__(self):
        super(MODNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)  # Downsample
        )

        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(128, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 1, kernel_size=3, stride=1, padding=1),
            nn.Sigmoid()  # Output alpha mask
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded  # Alpha matte output

if __name__ == "__main__":
    model = MODNet()
    sample_input = torch.randn(1, 3, 512, 512)  # (Batch, Channels, Height, Width)
    output = model(sample_input)
    print("Output Shape:", output.shape)  # Expected: (1, 1, 512, 512)
