```python
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class GPT4:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

    def generate_response(self, input_text):
        inputs = self.tokenizer.encode(input_text, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

gpt4 = GPT4()

def handleEmail(email):
    email_content = email['content']
    response = gpt4.generate_response(email_content)
    return response

def scheduleTask(task):
    task_description = task['description']
    response = gpt4.generate_response(task_description)
    return response
```