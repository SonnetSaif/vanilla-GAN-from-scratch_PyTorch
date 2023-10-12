# Vanilla GAN Implementation

This repository contains an implementation of the Generative Adversarial Network (GAN) based on the original paper [Generative Adversarial Networks by Ian Goodfellow et al.](https://arxiv.org/abs/1406.2661)

The code is written in PyTorch and aims to generate realistic images using a GAN architecture.

## Table of Contents

- [Vanilla GAN Implementation](#vanilla-gan-implementation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Results](#results)
  - [Contributing](#contributing)
  - [License](#license)
  - [Citation](#citation)

## Introduction

The Generative Adversarial Network (GAN) is a deep learning architecture that consists of two neural networks, a generator and a discriminator, which are trained simultaneously through adversarial training. The generator tries to create data that is indistinguishable from real data, while the discriminator tries to differentiate between real and generated data.

This implementation closely follows the original GAN paper, though some minor changes have been made. 
<!-- providing a solid foundation for understanding and experimenting with GANs. -->

## Getting Started

### Prerequisites

- Python (>=3.6)
- PyTorch (>=1.7.1)
- Other dependencies can be installed using the provided `requirements.txt` file.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/SonnetSaif/vanilla-GAN-from-scratch_PyTorch.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage
- Just simply execute the **vanilla_GAN_PyTorch.ipynb** cell by cell in Google Colab/Jupyter Notebook


## Dataset

This project utilizes the MNIST dataset, a widely used benchmark dataset for handwritten digit recognition. MNIST contains a training set of 60,000 grayscale images of handwritten digits (0 through 9) and a test set of 10,000 images. Each image is 28x28 pixels.

### Source

The dataset is available directly through the torchvision library in PyTorch. Also, available at [huggingface](https://huggingface.co/datasets/mnist).


## Results


## Contributing
If you'd like to contribute or have any suggestions for this project, feel free to open an issue or create a pull request. Contributions are welcome!


## License
This project is licensed under the MIT License.


## Citation
If you use this code in your research, please cite the original GAN paper:
```bash
@article{goodfellow2014generative,
  title={Generative adversarial nets},
  author={Goodfellow, Ian and Pouget-Abadie, Jean and Mirza, Mehdi and Xu, Bing and Warde-Farley, David and Ozair, Sherjil and Courville, Aaron and Bengio, Yoshua},
  journal={Advances in neural information processing systems},
  volume={27},
  year={2014}
}
```
