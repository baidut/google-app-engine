from ..label import IqaLabel

'''
Download the datasets
=====================

https://live.ece.utexas.edu/research/ChallengeDB/

.
├── !data/
│   ├── CLIVE/
│        ├── labels.csv
│        ├── Image/
│        │    ├── trainingImages/
│        │    ├── 3.bmp

'''

class CLIVE(IqaLabel):
    path = '!data/CLIVE'
    img_raw_size = [500, 500]
    img_tfm_size = 500
    folder = 'Images'
