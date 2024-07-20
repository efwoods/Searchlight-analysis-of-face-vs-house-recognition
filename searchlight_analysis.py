"""This module is used to perform searchlight analysis."""

# Load the Haxby dataset

import pandas as pd
from nilearn import datasets
from nilearn.image import get_data, load_img, new_img_like


def load_haxby_dataset():
    """This function loads the haxby dataset.

    Returns:

        fmri_filename: Functional nifti images (4D)
        labels: labels fro the nifit image
        y: Target labels
        y: run labels
    """

    haxby_dataset = datasets.fetch_haxby()

    # print basic information on the dataset
    print(f'Anatomical nifti image (3D) is located at: {haxby_dataset.mask}')
    print(f'Functional nifti images (4D) is located at: {haxby_dataset.func[0]}')

    fmri_filename = haxby_dataset.func[0]
    labels = pd.read_csv(haxby_dataset.session_target[0], sep=' ')
    y = labels['labels']
    run = labels['chunks']

    return fmri_filename, labels, y, run

if __name__ == '__main__':
    fmri_filename, labels, y, run = load_haxby_dataset()
