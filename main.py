import torch

import train



# Declare Global Settings
root_dir = "dataset"
num_classes = 4
learning_rate = 1e-4
min_lr = 1e-7
patience = 10
batch_size = 8
epochs = 750
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Declare Interation Settings
interations = [
    {
        'save_dir': 'runs/v1',
        'size': (400, 400),
        'cfg': [8, 'M', 16, 16, 'M', 32, 32, 'M', 64, 64, 64, 'M', 128, 128, 128, 'M', 256, 256, 256, 'M'],
        'bn': True,
    }
]

if __name__ == "__main__":
    for data in interations:
        train.run(root_dir, data['size'], data['save_dir'], data['cfg'], data['bn'], batch_size, learning_rate, min_lr,
                  epochs, device, patience, num_classes)
