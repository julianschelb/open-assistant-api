from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained('OpenAssistant/oasst-sft-1-pythia-12b')
model = AutoModelForCausalLM.from_pretrained('OpenAssistant/oasst-sft-1-pythia-12b').eval()

#from transformers import GPT2Tokenizer, #GPT2LMHeadModel
#tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
#model = GPT2LMHeadModel.from_pretrained('gpt2')
