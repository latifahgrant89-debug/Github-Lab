import sys

shift = int(sys.argv[1])

message = sys.stdin.read()
message = message.upper()

clean_text = ""
for ch in message:
    if ch.isalpha():
        clean_text += ch

encoded = ""
for ch in clean_text:
    new_letter = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
    encoded += new_letter

count = 0
for i in range(0, len(encoded), 5):
    print(encoded[i:i+5], end=" ")
    count += 1

    if count == 10:
        print()
        count = 0

print()
