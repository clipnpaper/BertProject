from transformers import BertModel, BertTokenizer
import torch

model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = "I love Paris"

# 1. 표준 토큰화 방식 ([CLS], [SEP], Attention Mask가 자동 추가됨)
inputs = tokenizer(sentence, return_tensors='pt')
print(inputs)
# 출력: {'input_ids': tensor([[ 101, 1045, 2293, 3000,  102]]), 'token_type_ids': ..., 'attention_mask': ...}

# 2. 토큰 문자열 확인이 필요한 경우
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
print(tokens)
# 출력: ['[CLS]', 'i', 'love', 'paris', '[SEP]']