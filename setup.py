#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LimiX: Unleashing Structured-Data Modeling Capability for Generalist Intelligence

A foundation model for tabular data that handles classification, regression,
missing-value imputation, and more under one unified framework.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

# Core dependencies (excluding flash-attention which needs special handling)
install_requires = [
    'torch==2.7.1',
    'torchvision==0.22.1',
    'torchaudio==2.7.1',
    'tqdm==4.67.3',
    'pandas==2.3.3',
    'scipy==1.17.1',
    'scikit-learn==1.7.2',
    'kditransform==1.2.0',
    'einops==0.8.2',
    'numpy',
    'huggingface-hub',
]

# Optional dependencies for advanced features
extras_require = {
    'retrieval': ['optuna'],
    'dev': [
        'pytest',
        'black',
        'flake8',
        'mypy',
    ],
    'docs': [
        'sphinx',
        'sphinx-rtd-theme',
    ],
}

# All optional dependencies
extras_require['all'] = list(set(sum(extras_require.values(), [])))

setup(
    name='limix',
    version='1.0.0',
    author='LimiX Team',
    author_email='',
    description='A foundation model for tabular data with unified learning capabilities',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/limix-ldm/LimiX',
    packages=find_packages(exclude=['examples', 'doc', 'benchmark_list']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.11,<3.12',
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    zip_safe=False,
    keywords='machine-learning deep-learning tabular-data transformer foundation-model',
    project_urls={
        'Documentation': 'https://www.limix.ai/doc/',
        'Source': 'https://github.com/limix-ldm/LimiX',
        'Tracker': 'https://github.com/limix-ldm/LimiX/issues',
    },
)
