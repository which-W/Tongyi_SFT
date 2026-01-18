from peft import AutoPeftModelForCausalLM
from modelscope import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer
from modelscope import snapshot_download
import os


class SFT_EVA:
    def __init__(self):
        # 指定模型保存到当前目录下的 qwen_model 文件夹
        self.cache_dir = os.path.abspath("./models")
        self.model_dir = snapshot_download(
            "qwen/Qwen-1_8B-Chat-Int4", cache_dir=self.cache_dir
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_dir, trust_remote_code=True
        )
        self.model = AutoPeftModelForCausalLM.from_pretrained(
            "output_qwen",  # path to the output directory
            device_map="auto",
            trust_remote_code=True,
        ).eval()

    def eva_all(self):
        self.model.generation_config.top_p = 0  # 只选择概率最高的token

        prompt_template = """
            给定一句话：“%s”，请你按步骤要求工作。

            步骤1：识别这句话中的所需要要求的诗歌信息
            步骤2：根据问题提示生成对应的诗歌内容

            请问，这首诗歌是：
        """
        Q_list = [
            "写一首关于春天的诗",
            "能为我写一首爱情诗吗？",
            "请写一首描写乡村夜晚的七言绝句",
            "我想听一首关于友情的现代诗",
            "写一首关于秋天落叶的五言律诗",
            "你能创作一首城市夜景的诗吗？",
            "请为我和我的爱人写一首结婚纪念日的诗",
            "写一首关于大海和孤独的自由诗",
            "能写一首关于童年回忆的诗吗？",
        ]
        for Q in Q_list:
            prompt = prompt_template % (Q,)
            A, hist = self.model.chat(self.tokenizer, prompt, history=None)
            print("Q:%s\nA:%s\n" % (Q, A))

    def eav_one(self,que):
        self.model.generation_config.top_p = 0  # 只选择概率最高的token

        prompt_template = """
            给定一句话：“%s”，请你按步骤要求工作。

            步骤1：识别这句话中的所需要要求的诗歌信息
            步骤2：根据问题提示生成对应的诗歌内容

            请问，这首诗歌是：
        """
        prompt = prompt_template % (que,)
        A, hist = self.model.chat(self.tokenizer, prompt, history=None)
        print(f"{A}")

if __name__ == "__main__":
    eval = SFT_EVA()
    eval.eva_all()
    
