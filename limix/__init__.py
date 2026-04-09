"""
LimiX: Unleashing Structured-Data Modeling Capability for Generalist Intelligence

A foundation model for tabular data that handles classification, regression,
missing-value imputation, feature selection, sample selection, and causal inference
under one unified framework.

For more information, visit: https://www.limix.ai/doc/
"""

__version__ = '1.0.0'

from limix.inference.predictor import LimiXPredictor

__all__ = [
    'LimiXPredictor',
    '__version__',
]
