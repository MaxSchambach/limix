# Package Restructuring Summary

This document summarizes the changes made to make LimiX pip-installable.

## Changes Made

### 1. Package Structure
Moved core code modules into a `limix/` package directory:
- `model/` → `limix/model/`
- `inference/` → `limix/inference/`
- `utils/` → `limix/utils/`
- `retrieval_extension/` → `limix/retrieval_extension/`

### 2. Files Created

#### `setup.py`
- Standard Python package setup file
- Includes all dependencies specified for Python 3.11
- Supports optional dependencies via extras_require:
  - `retrieval`: Optuna for hyperparameter search
  - `dev`: Development tools (pytest, black, flake8, mypy)
  - `docs`: Documentation tools (sphinx)
  - `all`: All optional dependencies

#### `pyproject.toml`
- Modern Python packaging configuration (PEP 517/518)
- Contains same metadata as setup.py in declarative format

#### `MANIFEST.in`
- Specifies which non-Python files to include in the distribution
- Includes config files, documentation, README, and LICENSE

#### `limix/__init__.py`
- Main package entry point
- Exports `LimiXPredictor` class for easy importing
- Defines package version

#### Package `__init__.py` files
- `limix/inference/__init__.py`
- `limix/model/__init__.py`
- `limix/utils/__init__.py` (already existed)
- `limix/retrieval_extension/__init__.py`
- `limix/retrieval_extension/retrieval_search_space/__init__.py`

#### `INSTALL.md`
- Installation instructions for end users

### 3. Import Statement Updates

Updated all relative imports to absolute imports with `limix.` prefix:

**Files Updated:**
- `limix/inference/predictor.py`
- `limix/inference/inference_method.py`
- `limix/inference/preprocess.py`
- `limix/model/encoders.py`
- `limix/model/transformer.py`
- `limix/utils/loading.py`
- `limix/retrieval_extension/retrieval_search_space/inference_search.py`
- `inference_classifier.py` (top-level script)
- `inference_regression.py` (top-level script)
- `examples/demo_classification.py`
- `examples/demo_regression.py`
- `examples/demo_missing_value_imputation.py`

**Example change:**
```python
# Before
from inference.predictor import LimiXPredictor
from utils.loading import load_model

# After
from limix.inference.predictor import LimiXPredictor
from limix.utils.loading import load_model
```

## Installation Instructions

### For End Users

```bash
# Basic installation
pip install limix

# With flash-attention (Linux + CUDA only)
pip install https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.0.post2/flash_attn-2.8.0.post2+cu12torch2.7cxx11abiTRUE-cp311-cp311-linux_x86_64.whl
pip install limix

# With optional dependencies
pip install limix[retrieval]  # Adds optuna
pip install limix[all]         # All optional deps
```

### For Development

```bash
git clone https://github.com/limix-ldm/LimiX.git
cd LimiX
pip install -e .                # Editable install
pip install -e .[dev]          # With dev tools
```

## Usage After Installation

```python
# Simple import
from limix import LimiXPredictor

# Or explicit
from limix.inference.predictor import LimiXPredictor
```

## Files That Remain at Root Level

These files intentionally remain at the repository root:
- `inference_classifier.py` - Example inference script
- `inference_regression.py` - Example inference script
- `examples/` - Example scripts directory
- `config/` - Configuration files (included in package via MANIFEST.in)
- `doc/` - Documentation and images
- `benchmark_list/` - Benchmark data (excluded from package)

## Dependencies

All dependencies are specified with exact versions as requested:
- torch==2.7.1
- torchvision==0.22.1
- torchaudio==2.7.1
- tqdm==4.67.3
- pandas==3.0.2
- scipy==1.17.1
- scikit-learn==1.7.2
- kditransform==1.2.0
- numpy (version flexible)
- huggingface-hub (version flexible)

**Note on flash-attention:**
The flash-attention wheel is NOT included in install_requires because:
1. It's Linux-only
2. It's CUDA-specific
3. Users need to select the correct pre-built wheel for their system

Users should install it separately before installing limix if they want optimal performance.

## Testing the Package

To test the package structure locally before publishing:

```bash
# Build the package
python setup.py sdist bdist_wheel

# Install locally
pip install dist/limix-1.0.0-py3-none-any.whl

# Test import
python -c "from limix import LimiXPredictor; print('Success!')"
```

## Publishing to PyPI

When ready to publish:

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Upload to Test PyPI first
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# If test passes, upload to PyPI
twine upload dist/*
```

## Backward Compatibility

The top-level scripts (`inference_classifier.py`, `inference_regression.py`) and examples still work because:
1. They use the updated import statements (`from limix.inference.predictor import ...`)
2. The `sys.path` manipulation in examples ensures the package can be found

This means existing workflows and documentation remain valid.
