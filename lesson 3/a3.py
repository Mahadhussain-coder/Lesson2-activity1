# 1) Ask the user to enter a word or sentence and store it in `text`.
# 2) Reverse the string stored in `text` and store the reversed result in `revText`.
#    (Reversing means the last character becomes first, and the first becomes last.)
# 3) Replace `text` with the reversed string (set `text` equal to `revText`).
# 4) Print a message saying you are showing the reversed string.
# 5) Print the reversed string stored in `text`.

text = str(input("Enter a string"))

revText = text[::-1]
text = revText

print("Reverse of the given string is")
print(text)