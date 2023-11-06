"""Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді коду Морзе та виводить декодоване значення
(латинськими літерами).
   Особливості:
    - використовуються лише крапки, тире і пробіли (.- )
    - один пробіл означає нову літеру
    - три пробіли означають нове слово
    - результат може бути case-insensetive (на ваш розсуд - велики чи маленькими літерами).
    - для простоти реалізації - цифри, знаки пунктуацїї, дужки, лапки тощо використовуватися не будуть.
Лише латинські літери.
    - додайте можливість декодування сервісного сигналу SOS (...---...)
    Приклад:
    --. . . -.- .... ..- -...   .. ...   .... . .-. ."""


def morse_decoder(morse_input: str) -> str:
    letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
             '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
             '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    morse_alphabet = dict(zip(morse, letters))
    morse_alphabet["...---..."] = "SOS"  # або в ручну прописувати словник , або костиль

    morse_separated_words = morse_input.strip().split("   ")
    decoded_words = []
    for word in morse_separated_words:
        morse_letters = word.split()
        decoded_word = ""
        for letter in morse_letters:
            if letter in morse_alphabet:
                decoded_word += morse_alphabet[letter]
        decoded_words.append(decoded_word)
    decoded_text = " ".join(decoded_words)
    return decoded_text


if __name__ == "__main__":
    morse_input: str = "--. . . -.- .... ..- -...   .. ...   .... . .-. .   ...---..."
    print(morse_decoder(morse_input))
