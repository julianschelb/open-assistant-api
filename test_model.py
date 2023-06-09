from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoTokenizer, AutoModelForCausalLM, AutoModelWithLMHead, AutoModel

# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2LMHeadModel.from_pretrained('gpt2')

tokenizer = AutoTokenizer.from_pretrained(
    'OpenAssistant/oasst-sft-1-pythia-12b')
model = AutoModelForCausalLM.from_pretrained(
    'OpenAssistant/oasst-sft-1-pythia-12b', trust_remote_code=True)

request = {"prompt": "<|prompter|>Who was Albert Einstein?<|endoftext|><|assistant|>"}

input_sequence = tokenizer(
    request.get("prompt"), return_tensors="pt"
)

print(input_sequence)


output = model.generate(**input_sequence, max_new_tokens=500, typical_p=0.2, 
                        temperature=0.6, pad_token_id=tokenizer.eos_token_id,
                        num_beams=5, num_return_sequences=5)
print(output)
response = tokenizer.batch_decode(output, skip_special_tokens=False)
print(response)