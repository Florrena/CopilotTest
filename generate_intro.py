import random

def paraphrase_text(text):
    """Funkcja parafrazująca podany tekst."""
    sentences = text.split('. ')
    paraphrased_sentences = []
    
    for sentence in sentences:
        operation = random.choice([shuffle_words, add_intro, split_sentence, change_tense])
        paraphrased_sentences.append(operation(sentence))
    
    return '. '.join(paraphrased_sentences)

def shuffle_words(sentence):
    """Przestawia słowa w zdaniu."""
    words = sentence.split()
    random.shuffle(words)
    return ' '.join(words)

def add_intro(sentence):
    """Dodaje wstęp do zdania."""
    intro = "W kontekście omawianego tematu, "
    return intro + sentence

def split_sentence(sentence):
    """Rozdziela zdanie na dwa krótsze."""
    words = sentence.split()
    if len(words) > 5:  # Upewniamy się, że zdanie jest wystarczająco długie
        mid = len(words) // 2
        first_part = ' '.join(words[:mid]) + '.'
        second_part = ' '.join(words[mid:]) + '.'
        return first_part + " " + second_part
    return sentence  # Jeśli zdanie jest za krótkie, zwracamy oryginał

def change_tense(sentence):
    """Zmienia czas gramatyczny w zdaniu na przyszły."""
    if "jest" in sentence:
        return sentence.replace("jest", "będzie")
    elif "był" in sentence:
        return sentence.replace("był", "będzie")
    return sentence  # Jeśli nie ma odpowiednich słów, zwracamy oryginał
