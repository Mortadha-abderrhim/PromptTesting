


from unsloth import FastLanguageModel
import re
import torch



class ModelWrapper:

    def __init__(self, model_path="Mortadha/proxy_01"):
        self.model, self.tokenizer = FastLanguageModel.from_pretrained(
            model_path,
            max_seq_length = 16000,
            load_in_4bit = False, # Use 4bit to reduce memory use. False for 16bit LoRA.
            device_map = "balanced",
        )
        FastLanguageModel.for_inference(self.model)

    def generate(self, message,gen_args = {}):
        with torch.no_grad():
            messages = [
                {"role" : "user", "content" : message}
            ]
            tokenized = self.tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                return_tensors = "pt",
                #enable_thinking=False,
                return_dict=True,).to("cuda")
            output = self.model.generate(
            **tokenized,
            max_new_tokens = 512,
            **gen_args
            )[0]

            response = self.tokenizer.decode(
                output[len(tokenized["input_ids"][0]):],
                skip_special_tokens=True
            )

            # Remove common chat artifacts
            response = re.sub(r"<\|.*?\|>", "", response)
            response = re.sub(r"\[/?INST\]", "", response)
            response = re.sub(r"</s>", "", response)

            # Cle8an whitespace
            response = response.strip()
        return response
