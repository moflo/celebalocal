# TFDS Manual Loading of Celeb A dataset

Workaround for failing TFDS loading of public dataset, Celeb A

## Usage

You can use this from with Colab using the following methods:

```
!pip install git+https://github.com/moflo/celebalocal.git
!pip install tfds_nightly

import tensorflow as tf
tf.__version__  # should be 2.7.0

import tensorflow_datasets as tfds
import celebalocal
ds = tfds.load('celebalocal', split='train')
```
