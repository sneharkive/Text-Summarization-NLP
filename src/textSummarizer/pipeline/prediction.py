# from textSummarizer.config.configuration import ConfigurationManager
# from transformers import AutoTokenizer
# from transformers import pipeline
# from transformers import PegasusForConditionalGeneration
#
#
# class PredictionPipeline:
#     def __init__(self):
#         self.config = ConfigurationManager().get_model_evaluation_config()
#
#     def predict(self, text):
#         tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
#         # gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
#         model = PegasusForConditionalGeneration.from_pretrained(
#             self.config.model_path
#         )
#
#         # pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
#         # pipe = pipeline("text-generation", model=self.config.model_path, tokenizer=tokenizer)
#         pipe = pipeline(
#             "summarization",
#             model=model,
#             tokenizer=tokenizer
#         )
#
#         print("Dialogue:")
#         print(text)
#
#         # output = pipe(text, **gen_kwargs)[0]["summary_text"]
#         output = pipe(
#             text,
#             max_new_tokens=80,
#             num_beams=8,
#             length_penalty=0.8,
#             do_sample=False
#         )[0]["summary_text"]
#
#         print("\nModel Summary:")
#         print(output)
#
#         return output


from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        # This will now download the tiny model from Hugging Face
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)

    def predict(self, text: str):
        # Remove the "summarize: " prefix for BART-based tiny models
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding="longest")

        summary_ids = self.model.generate(
            inputs["input_ids"],
            num_beams=4,
            max_new_tokens=50,
            early_stopping=True
        )

        output = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return output