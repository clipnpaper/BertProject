from transformers import BertModel, BertTokenizer
import torch

model = BertModel.from_pretrained('bert-base-uncased',
                                    output_hidden_states=True)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

sentence = "Oh I'm Drowing, it's raining all day. Breath"
tokens = tokenizer.tokenize(sentence)
tokens = ["[CLS]"] + tokens + ["[SEP]"]

print(f"\n--- 토큰 분절 결과: {tokens} ---")
print(f"\n--- 토큰 개수: {len(tokens)} ---")

tokens = tokens + ['[PAD]'] * 2
print(f"\n--- [PAD] 추가 후 토큰: {tokens} ---")

attention_mask = [1 if i != '[PAD]' else 0 for i in tokens]
print(f"\n--- 어텐션 마스크: {attention_mask} ---")
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(f"\n--- 토큰 ID 변환: {token_ids} ---")
token_ids = torch.tensor(token_ids).unsqueeze(0)
attention_mask = torch.tensor(attention_mask).unsqueeze(0)

outputs = model(token_ids, attention_mask=attention_mask)
last_hidden_state = outputs.last_hidden_state
pooler_output = outputs.pooler_output
hidden_states = outputs.hidden_states

print(f"\n--- last_hidden_state: {last_hidden_state.shape} ---")
print(f"\n--- pooler_output: {pooler_output.shape} ---")
print(f"\n--- hidden_states의 길이 : {len(hidden_states)} ---")








