import random

from dvclive import Live

live = Live(save_dvc_exp=True)
for i in range(10):
    live.log_metric("train/metric", random.random())
    live.log_metric("test/metric", random.random())
    live.next_step()
live.end()
