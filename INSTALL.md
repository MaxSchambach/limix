# LimiX Installation Guide

## Installation via pip

### Standard Installation

```bash
pip install limix
```

### Installation with Flash Attention (Linux only)

For optimal performance on Linux with CUDA 12.x, install flash-attention:

```bash
# For Python 3.11
pip install https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.0.post2/flash_attn-2.8.0.post2+cu12torch2.7cxx11abiTRUE-cp311-cp311-linux_x86_64.whl

# Then install limix
pip install limix
```

**Note**: Flash attention is a pre-compiled wheel for Linux only. On macOS or Windows, the package will work without it but may have reduced performance.

### Development Installation

If you want to install from source for development:

```bash
git clone https://github.com/limix-ldm/LimiX.git
cd LimiX
pip install -e .
```

### Installation with Optional Dependencies

```bash
# For retrieval optimization features
pip install limix[retrieval]

# For development tools
pip install limix[dev]

# Install everything
pip install limix[all]
```

## Usage

After installation, you can import LimiX in your Python code:

```python
from limix import LimiXPredictor
import torch

# Create predictor
clf = LimiXPredictor(
    device=torch.device('cuda'),
    model_path='path/to/model.ckpt',
    inference_config='config/cls_default_retrieval.json'
)

# Make predictions
prediction = clf.predict(X_train, y_train, X_test)
```

## Requirements

- Python >= 3.11, < 3.12
- PyTorch 2.7.1
- CUDA-compatible GPU (recommended for inference)

For more detailed usage examples, see the [main README](README.md) or [documentation](https://www.limix.ai/doc/).
