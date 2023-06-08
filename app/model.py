# from transformers import AutoTokenizer, AutoModelForCausalLM
# import pickle

# tokenizer = AutoTokenizer.from_pretrained(
#    "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", add_prefix_space=True)
# model = AutoModelForCausalLM.from_pretrained(
#    "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5").eval()

from transformers import GPT2Tokenizer, GPT2LMHeadModel
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
