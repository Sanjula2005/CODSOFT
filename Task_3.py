import random

logo="""
 __        __   __        __   __   __      __   ___       ___  __       ___  __   __  
|__)  /\  /__` /__` |  | /  \ |__) |  \    / _` |__  |\ | |__  |__)  /\   |  /  \ |__) 
|    /~~\ .__/ .__/ |/\| \__/ |  \ |__/    \__> |___ | \| |___ |  \ /~~\  |  \__/ |  \ 
                                                                                       
"""

characters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '*', '+']
print("Welcome to Password Generator!")
print(logo)
length=int(input("Enter the length of the password you would like to generate:"))
chosen=[]

for i in range(1,length+1):
    chosen.append(random.choice(characters))

random.shuffle(chosen)

password=""
for char in chosen:
    password+=char

print(f"Your password is {password}")