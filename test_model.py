from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoTokenizer, AutoModelForCausalLM, AutoModelWithLMHead

# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2LMHeadModel.from_pretrained('gpt2')

tokenizer = AutoTokenizer.from_pretrained(
    'OpenAssistant/falcon-7b-sft-mix-2000')
model = AutoModelWithLMHead.from_pretrained(
    'OpenAssistant/falcon-7b-sft-mix-2000', trust_remote_code=True)

request = {"prompt": "Once upon a time"}

input_sequence = tokenizer(
    request.get("prompt"), return_tensors="pt"
)

print(input_sequence)


# Pass input sequence as list into the model
outputs = model.generate(
    **input_sequence,
    num_beams=5,
    num_return_sequences=5,
    # prefix_allowed_tokens_fn=lambda batch_id, sent: trie.get(sent.tolist()),
)

print(outputs)
# Decode model output to obtain entity candidates
response = tokenizer.batch_decode(outputs, skip_special_tokens=True)
# result = jsonable_encoder(EntityDisambiguated(candidates=candidates))

print(response)
