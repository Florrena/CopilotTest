import random

def load_file_content(file_path):
    """Załaduj zawartość pliku."""
    with open(file_path, 'r') as file:
        return file.read()

def paraphrase_intro(template, topic, file_content):
    """Generuje i parafrazuje wstęp na podstawie wzoru, tematu i pliku."""
    
    # Wstawienie tematu do szablonu
    intro = template.replace("[TOPIC]", topic)

    # Dodaj dane z pliku do kontekstu wstępu
    context_based_on_file = extract_key_points(file_content)

    # Połączenie wstępu z kontekstem
    paraphrased_intro = intro + " " + context_based_on_file

    # Prosta parafraza (można zastąpić zaawansowanym modelem NLP)
    paraphrased_intro = paraphrase_sentence(paraphrased_intro)

    return paraphrased_intro

def extract_key_points(file_content):
    """Wyciągnij kluczowe punkty z pliku."""
    sentences = file_content.split('.')
    if len(sentences) > 2:
        return sentences[0] + " " + sentences[1]
    return "Brak dodatkowych informacji."

def paraphrase_sentence(sentence):
    """Proste parafrazowanie – zamiana wyrażeń na synonimy."""
    replacements = {
        "is": "appears to be",
        "important": "significant",
        "field": "area",
        "study": "research"
    }
    
    words = sentence.split()
    paraphrased_words = [replacements.get(word, word) for word in words]
    
    return ' '.join(paraphrased_words)

# Funkcja obsługiwana przez Copilot Studio
def generate_and_paraphrase_intro(template, topic, filePath):
    # Załaduj plik z zawartością
    file_content = load_file_content(filePath)
    
    # Wygeneruj parafrazowany wstęp
    return paraphrase_intro(template, topic, file_content)
