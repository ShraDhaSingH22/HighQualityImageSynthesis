import torch
import torch.nn as nn

class SRGAN(nn.Module):
    def __init__(self):
        super(SRGAN, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 3, kernel_size=3, stride=1, padding=1)
        )

    def forward(self, x):
        return self.model(x)

    def enhance(self, image):
        image_tensor = torch.tensor(image).permute(2, 0, 1).unsqueeze(0).float() / 255.0  # Normalize
        with torch.no_grad():
            enhanced = self.forward(image_tensor)
        return (enhanced.squeeze(0).permute(1, 2, 0).numpy() * 255).astype("uint8")

if __name__ == "__main__":
    model = SRGAN()
    sample_input = torch.randn(1, 3, 512, 512)  # (Batch, Channels, Height, Width)
    output = model(sample_input)
    print("Output Shape:", output.shape)  # Expected: (1, 3, 512, 512)
