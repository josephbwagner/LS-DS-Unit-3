#!/usr/bin/env python
"""
lambdata - a collection of Data Science helper functions
"""

import numpy as np
import pandas as pd
from . import example_module

Y = example_module.increment(example_module.x)
TEST = pd.DataFrame(np.ones(10))
