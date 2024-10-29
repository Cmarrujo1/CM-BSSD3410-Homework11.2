import random
from collections import defaultdict, Counter
import re

def load_cleaned_text(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    return re.sub(r'-lrb-|-rrb-|\W+', '', text).strip()

def build_markov_chain(corpus, window_size):
    markov_chain = defaultdict(list)
    for i in range(len(corpus) - window_size):
        key = corpus[i:i + window_size]
        next_char = corpus[i + window_size]
        markov_chain[key].append(next_char)
    return markov_chain

def generate_name(chain, window_size, name_length, temperature=1.0):
    key = random.choice(list(chain.keys()))
    result = list(key)
    for _ in range(name_length - window_size):
        next_chars = chain.get(key, [])
        if not next_chars:
            break
        next_char = weighted_choice(next_chars, temperature)
        result.append(next_char)
        key = ''.join(result[-window_size:])
    return ''.join(result)

def weighted_choice(chars, temperature):
    char_counts = Counter(chars)
    chars, counts = zip(*char_counts.items())
    counts = [count ** (1.0 / temperature) for count in counts]
    total = sum(counts)
    probabilities = [count / total for count in counts]
    return random.choices(chars, weights=probabilities, k=1)[0]

def main():
    corpus = load_cleaned_text('valid.title')
    while True:
        window_size = int(input("Enter the window size: "))
        temperature = float(input("Enter temperature (1.0 is standard): "))
        name_length = int(input("Enter the desired name length: "))
        markov_chain = build_markov_chain(corpus, window_size)
        generated_name = generate_name(markov_chain, window_size, name_length, temperature)
        print("\nGenerated Name:\n")
        print(generated_name)
        repeat = input("\nWould you like to generate another name? (yes/no): ").strip().lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()
