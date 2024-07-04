from caesercypherart import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(dir,input_text,shift_amount):
  if (dir=="encode"):
    cipher_text=""
    for i in input_text:
      if i in alphabet:
        index_no=alphabet.index(i)
        new_index=index_no+shift_amount
        if new_index>=len(alphabet):
          new_index%=len(alphabet)
        new_letter=alphabet[new_index]
        cipher_text+=new_letter
      else:
        cipher_text+=i
    print(f"The encoded text is {cipher_text}")

  elif (dir=="decode"):
    decipher_text=""
    for i in input_text:
      if i in alphabet:
        index_no=alphabet.index(i)
        new_index=index_no-shift_amount
        if new_index<len(alphabet):
          new_index%=len(alphabet)
        new_letter=alphabet[new_index]
        decipher_text+=new_letter
      else:
        decipher_text+=i
    print(f"The decoded text is {decipher_text}")

  else:
    print("Invalid Input!")

print(logo)
run_program=True
while(run_program):
  check=input("Type 'yes' to run the program. Type 'no' to terminate the program.\n").lower()
  if check=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(dir=direction,input_text=text,shift_amount=shift)
  else:
    print("GOODBYE...")
    run_program=False

