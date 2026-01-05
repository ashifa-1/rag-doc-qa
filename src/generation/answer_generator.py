from transformers import pipeline

class AnswerGenerator:
    def __init__(self, model_name="google/flan-t5-base"):
        self.generator = pipeline(
            "text2text-generation",
            model=model_name,
            max_length=700
        )

    def generate(self, prompt):
        response = self.generator(prompt)
        return response[0]["generated_text"]
