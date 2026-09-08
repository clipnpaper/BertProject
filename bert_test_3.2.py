from transformers import BertModel, BertTokenizer
import torch

# 1. 모델 및 토크나이저 로드
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = "Last Christmas, I give you my heart."

# 2. 토큰 분절(Tokenize) 및 수동 패딩 / 어텐션 마스크 실습
tokens = tokenizer.tokenize(sentence)
print("--- 분절된 토큰 ---")
print(tokens)

tokens = ['[CLS]'] + tokens + ['[SEP]']
print("\n--- [CLS] 와 [SEP] 추가 후 토큰 ---")
print(tokens)

tokens = tokens + ['[PAD]'] *2
print("\n--- [PAD] 추가 후 토큰 ---")
print(tokens)

attention_mask = [1 if i != '[PAD]' else 0 for i in tokens]
print("\n--- 어텐션 마스크 (1: 실제 토큰, 0: 패딩 토큰) ---")
print(attention_mask)

token_ids = tokenizer.convert_tokens_to_ids(tokens)
print("\n--- 토큰 ID 변환 ---")
print(token_ids)

token_ids = torch.tensor(token_ids).unsqueeze(0)
attention_mask = torch.tensor(attention_mask).unsqueeze(0)

outputs = model(token_ids, attention_mask=attention_mask)
hidden_rep = outputs.last_hidden_state
cls_head = outputs.pooler_output

print("\n--- hidden_rep (모든 토큰의 표현 벡터) ---")
print(hidden_rep.shape)

print("\n--- cls_head ([CLS] 토큰의 표현 벡터) ---")
print(cls_head.shape)


# 3. 표준 토큰화 방식 (PyTorch 텐서 형태로 반환)
inputs = tokenizer(sentence, return_tensors='pt')
print("\n--- ######토크나이저 결과 (인코딩) ###############---")
print(inputs)

print("\n--- input_ids ---")
print(inputs['input_ids'])
