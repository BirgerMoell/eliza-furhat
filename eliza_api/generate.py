import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

#tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

from transformers import GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

# add the EOS token as PAD token to avoid warnings
model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

# encode context the generation is conditioned on
input_ids = tokenizer.encode('It could be fun', return_tensors='tf')

# generate text until the output length (which includes the context length) reaches 50
# greedy_output = model.generate(input_ids, max_length=50)



# print("Output:\n" + 100 * '-')
# print(tokenizer.decode(greedy_output[0], skip_special_tokens=True))

# # activate beam search and early_stopping
# beam_output = model.generate(
#     input_ids, 
#     max_length=50, 
#     num_beams=5, 
#     no_repeat_ngram_size=2,
#     num_return_sequences=5,
#     early_stopping=True

# )

# print("Output:\n" + 100 * '-')
# print(tokenizer.decode(beam_output[0], skip_special_tokens=True))

# set seed to reproduce results. Feel free to change the seed though to get different results
tf.random.set_seed(0)

# activate sampling and deactivate top_k by setting top_k sampling to 0
# sample_output = model.generate(
#     input_ids, 
#     do_sample=True, 
#     max_length=50, 
#     top_k=0,
#     temperature=0.7
# )

# print("Output:\n" + 100 * '-')
# print(tokenizer.decode(sample_output[0], skip_special_tokens=True))

# set top_k to 50
# sample_output = model.generate(
#     input_ids, 
#     do_sample=True, 
#     max_length=50, 
#     top_k=50
# )

# print("Output:\n" + 100 * '-')
# print(tokenizer.decode(sample_output[0], skip_special_tokens=True))

# # set seed to reproduce results. Feel free to change the seed though to get different results
# tf.random.set_seed(0)

# deactivate top_k sampling and sample only from 92% most likely words
# sample_output = model.generate(
#     input_ids, 
#     do_sample=True, 
#     max_length=50, 
#     top_p=0.92, 
#     top_k=0
# )

# print("Output:\n" + 100 * '-')
# print(tokenizer.decode(sample_output[0], skip_special_tokens=True))

# # set seed to reproduce results. Feel free to change the seed though to get different results
# tf.random.set_seed(0)

# set top_k = 50 and set top_p = 0.95 and num_return_sequences = 3
# sample_outputs = model.generate(
#     input_ids,
#     do_sample=True, 
#     max_length=50, 
#     top_k=50, 
#     top_p=0.95, 
#     num_return_sequences=3
# )

# print("Output:\n" + 100 * '-')
# for i, sample_output in enumerate(sample_outputs):
#   print("{}: {}".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))


def gpt2generator(text):
    #text='\"'+text+'\"\n\"'
    #text = text + "?:"
    text = "-" + text + "?\n-:"
    print(text)
    input_ids = tokenizer.encode(text, return_tensors='tf')
    sample_outputs = model.generate(
    input_ids,
    do_sample=True, 
    max_length=30, 
    top_k=50, 
    top_p=0.95, 
    num_return_sequences=1
    )
    print("Output:\n" + 100 * '-')
    response = tokenizer.decode(sample_outputs[0], skip_special_tokens=True)[len(text):]
    if ("." in response):
        return response.split(".")[0]
    elif ("!" in response):  
        return response.split("!")[0]
    elif ("-" in response):  
        return response.split("-")[0]
    else:
        return response
    # for i, sample_output in enumerate(sample_outputs):
    #     print("{}: {}".format(i, tokenizer.decode(sample_output, skip_special_tokens=True)))


# wordy_words = gpt2generator("I am a robot")
# print(wordy_words)