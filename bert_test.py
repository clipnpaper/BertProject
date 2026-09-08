from transformers import BertModel, BertTokenizer
import torch

# 1. 모델 및 토크나이저 로드
model = BertModel.from_pretrained('bert-base-uncased')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = "Last Christmas, I give you my heart."

# 2. 토큰화 (PyTorch 텐서 형태로 반환)
inputs = tokenizer(sentence, return_tensors='pt')
print("--- 토크나이저 결과 (인코딩) ---")
print(inputs)

# 3. 토큰 문자열 확인
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
print("\n--- 분절된 토큰 목록 ---")
print(tokens)

# 4. BERT 모델 추론 및 출력 크기 확인
with torch.no_grad():
    outputs = model(**inputs)

last_hidden_state = outputs.last_hidden_state
print("\n--- 모델 출력 텐서 크기 (Batch Size, Sequence Length, Hidden Dimension) ---")
print("last_hidden_state shape:", last_hidden_state.shape)
# 출력 예시: torch.Size([1, 7, 768])
