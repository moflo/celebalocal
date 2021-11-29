import tensorflow_datasets as tfds
import os
import random

_DESCRIPTION = "celeblocal data loader"
_CITATION = "TFDS Celeb_A"


class Celebalocal(tfds.core.GeneratorBasedBuilder):
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(256, 256, 3)),
            'label': tfds.features.ClassLabel(names=['no', 'yes']),
        }),
        supervised_keys=('image', 'label'),  # Set to `None` to disable
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    path = dl_manager.download_and_extract('https://s3.amazonaws.com/pytorch-tutorial-assets/img_align_celeba.zip')
    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    for f in path.glob('img_align_celeba/*.jpg'):
      image_id = os.path.basename(f).split('.')[0]
      key = random.getrandbits(256)
      record =  {
          'image': f,
          'label': 'yes',
      }
      yield key, record
