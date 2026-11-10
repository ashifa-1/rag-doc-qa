from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class AnswerGenerator:
    def __init__(self, model_name="google/flan-t5-base", max_new_tokens=256):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name, local_files_only=True)
        except Exception:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.max_new_tokens = max_new_tokens

    def generate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
        outputs = self.model.generate(**inputs, max_new_tokens=self.max_new_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

