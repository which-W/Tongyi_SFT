from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer
from modelscope import snapshot_download
import os

class Down_Load():
    def __init__(self):
        self.cache_dir = os.path.abspath("./models")
        self.model_dir = snapshot_download("qwen/Qwen-1_8B-Chat-Int4", cache_dir=self.cache_dir)
        

if __name__ == '__main__':
    Down_Load()