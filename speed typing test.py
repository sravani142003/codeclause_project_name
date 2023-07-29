
import random
import time

def get_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Peter Piper picked a peck of pickled peppers.",
        "The rain in Spain stays mainly in the plain."
    ]
    return random.choice(sentences)

def calculate_typing_speed(start_time, end_time, text_length):
    elapsed_time = end_time - start_time
    words_per_minute = (text_length / 5) / (elapsed_time / 60)
    return words_per_minute

def main():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    
    sentence = get_sentence()
    print("\nType the following sentence:")
    print(sentence)

    input("Press Enter when you are ready...")
    start_time = time.time()
    
    user_input = input("\nEnter the sentence: ")
    end_time = time.time()

    words_typed = user_input.strip().split()
    sentence_words = sentence.split()
    correct_words = [w for w in words_typed if w in sentence_words]

    accuracy = len(correct_words) / len(sentence_words) * 100
    words_per_minute = calculate_typing_speed(start_time, end_time, len(user_input))

    print(f"\nYour typing speed: {words_per_minute:.2f} words per minute.")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()

