from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import speech_to_text

speech_to_text.speak("Which langauge you want translate book to among English, Hindi, Urdu and arabic?")
def sentence_translation_mbart(text):
    article_en = text
    model = MBartForConditionalGeneration.from_pretrained("./mbart_model")
    # model.save_pretrained("./mbart_model")
    tokenizer = MBart50TokenizerFast.from_pretrained("./mbart_tokenizer", src_lang="en_XX")
    # tokenizer.save_pretrained("./mbart_tokenizer")

    model_inputs = tokenizer(article_en, return_tensors="pt")

    # translate from English to Hindi
    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]
    )
    output = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    # => 'संयुक्त राष्ट्र के नेता कहते हैं कि सीरिया में कोई सैन्य समाधान नहीं है'
    return output[0]
