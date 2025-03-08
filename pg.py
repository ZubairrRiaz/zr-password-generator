import streamlit as st
import random
import string


def password_gen(length, digits, special):
    characters = string.ascii_letters

    if digits:
        characters += string.digits

    if special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

st.title('Password Generator by Zubair!')

length = st.slider('Select Password Length', min_value=6, max_value=32, value=12)

use_digits = st.checkbox('Include Digits.')

use_special = st.checkbox('Use Special Characters.')

if st.button('Generate Password'):
    password = password_gen(length, use_digits, use_special)

    st.write(f'Password Generated: {password}')


#     echo "# zr-password-generator" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/ZubairrRiaz/zr-password-generator.git
# git push -u origin main