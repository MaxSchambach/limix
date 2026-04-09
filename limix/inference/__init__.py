"""Inference module for LimiX predictor and inference methods."""

from limix.inference.predictor import LimiXPredictor
from limix.inference.inference_method import InferenceAttentionMap, InferenceResultWithRetrieval

__all__ = [
    'LimiXPredictor',
    'InferenceAttentionMap',
    'InferenceResultWithRetrieval',
]
