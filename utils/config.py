# -*- coding: utf-8 -*-

# @Author  : xmh
# @Time    : 2021/1/22 14:25
# @File    : config.py

"""
file description:：

"""
class GPT2Config():
    def __init__(self,
                 vocab_size_or_config_json_file=50257,
                 n_ctx = 1024,  # 表示每次最多取n_ctx个token, 即window size
                 n_position = 1024,
                 n_head = 12,
                 layer_norm_epsilon=1e-5
                 ):
        self.vocab_size_or_config_json_file = vocab_size_or_config_json_file
        self.n_ctx = n_ctx
        self.n_position = n_position
        self.n_head = n_head
        self.layer_norm_epsilon = layer_norm_epsilon