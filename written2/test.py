# Vigenere Cipher Dictionary Hacker
 2. # http://inventwithpython.com/hacking (BSD Licensed)
 3.
 4. import detectEnglish, vigenereCipher, pyperclip
 5.
 6. def main():
 7.     ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
 8.     hackedMessage = hackVigenere(ciphertext)
 9.
10.     if hackedMessage != None:
11.         print('Copying hacked message to clipboard:')
12.         print(hackedMessage)
13.         pyperclip.copy(hackedMessage)
14.     else:
15.         print('Failed to hack encryption.')
16.
17.
18. def hackVigenere(ciphertext):
19.     fo = open('dictionary.txt')
20.     words = fo.readlines()
21.     fo.close()
22.
23.     for word in words:
24.         word = word.strip() # remove the newline at the end
25.         decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
26.         if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
27.             # Check with user to see if the decrypted key has been found.
28.             print()
29.             print('Possible encryption break:')
30.             print('Key ' + str(word) + ': ' + decryptedText[:100])
31.             print()
32.             print('Enter D for done, or just press Enter to continue breaking:')
33.             response = input('> ')
34.
35.             if response.upper().startswith('D'):
36.                 return decryptedText
37.
38. if __name__ == '__main__':
39.     main()
