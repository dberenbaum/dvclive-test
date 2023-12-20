import random
import numpy as np

from dvclive import Live

with Live() as live:
    for i in range(20):
        live.log_metric("train/metric", random.random())
        live.log_metric("test/metric", random.random())
        img_numpy = np.random.randint(0, 254, (500, 500), dtype=np.uint8)
        live.log_image("numpy.png", img_numpy)
        live.next_step()
