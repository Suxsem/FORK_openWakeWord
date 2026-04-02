import platform
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Build extras_requires based on platform
def build_additional_requires():
    if platform.system() == "Windows" and platform.machine() == "x86_64":
        additional_requires = [
            'PyAudioWPatch'
        ]
    else:
        additional_requires = []

    return additional_requires

setuptools.setup(
    name="openwakeword",
    version="0.6.1", # Incrementata versione per distinguere il fork
    install_requires=[
        'onnxruntime>=1.14.0',
        'ai-edge-litert>=2.0.2; platform_system == "Linux" or platform_system == "Darwin"',
        'speexdsp-ns>=0.1.2; platform_system == "Linux"',
        'tqdm>=4.0',
        'scipy>=1.10.0', # Necessario per Python 3.12+
        'scikit-learn>=1.2.0',
        'requests>=2.0',
    ],
    extras_require={
        'test': [
            'pytest>=7.2.0',
            'pytest-cov>=2.10.1',
            'flake8>=5.0',
            'mock>=5.1',
        ],
        'full': [
            'mutagen>=1.46.0',
            'torch>=2.0.0', 
            'torchaudio>=2.0.0',
            'torchinfo>=1.8.0',
            'torchmetrics>=0.11.4',
            'speechbrain>=1.0.0', # Versione stabile 2025/2026
            'audiomentations>=0.30.0',
            'torch-audiomentations>=0.11.0',
            'acoustics>=0.2.6',
            'pyyaml>=6.0',
            'onnx>=1.16.0',
            'onnx2tf>=1.20.0', # Sostituisce onnx-tf per conversioni moderne
            'onnxsim>=0.4.0',
            'pronouncing>=0.2.0',
            'datasets>=2.14.4',
            'deep-phonemizer>=0.0.19'
        ]
    },
    author="David Scripka (Fork by Suxsem)",
    description="An open-source audio wake word detection framework updated for modern Python environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Suxsem/FORK_openWakeWord",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
)