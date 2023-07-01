import time

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import speech_to_text

speech_to_text.speak("Hey I am your personal chatbot called Sophie! We can have casual talks here.")

def chatbot():
    tokenizer = AutoTokenizer.from_pretrained("./DailoGPT_tokenizer", padding_side='left')
    # tokenizer.save_pretrained("./DailoGPT_tokenizer")
    model = AutoModelForCausalLM.from_pretrained("./DailoGPT_model")
    # model.save_pretrained("./DailoGPT_model")
    # Let's chat for 100 lines
    for step in range(5):
        input_statement = ">> User:" + speech_to_text.get_audio()
        print(input_statement)
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(input_statement + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens,
        chat_history_ids = model.generate(bot_input_ids,
                                          max_length=500,
                                          pad_token_id=tokenizer.eos_token_id,
                                          no_repeat_ngram_size=3,
                                          do_sample=True,
                                          top_k=100,
                                          top_p=0.7,
                                          temperature=0.8
                                          )

        # pretty print last ouput tokens from bot
        output = "{}".format(
            tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))
        print("Sophie:" + output)
        speech_to_text.speak(output)
chatbot()



