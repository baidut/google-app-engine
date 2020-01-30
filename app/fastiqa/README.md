# Why FastIQA?

* easy to get started for [FastAI](https://github.com/fastai/fastai) users.
* training and validating an IQA model in a few lines of code

```python
%matplotlib inline
from fastiqa.basics import *

label = CLIVE                           # LIVE Challenge Database
arch = BodyHeadModel(backbone=resnet18) 
learn = IqaLearner.from_cls(label, arch)
learn.fit(10)                           # training for 10 epochs
learn.valid(on=[KonIQ, FLIVE])          # valid on other databases 
```

