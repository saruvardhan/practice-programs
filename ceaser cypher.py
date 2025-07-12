print('                   hello welcome to chiper world     ')
V = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

#hello

encoded= []
decoded=[]

def encode(sentense,count):
    for letter in sentense:    
        index_num = (V.index(letter)+ count)%25
        list_of= V[index_num]
        encoded.append(list_of)
    print("your encodded msg:",''.join(encoded))

def decode(sentense,count):
    for letter in sentense:    
        index_num = (V.index(letter)- count)%25
        list_o= V[index_num]
        decoded.append(list_o)
    print("your decodded msg:",''.join(decoded))
start = True

while start:
    select=input('what would you like to do(encrypt or decrypt):').lower()

    if select == 'encrypt':
        sentense=input("enter the sentence or word to encode: " ).lower()
        count=int(input("enter the number of letters to shift: " ))
        encode(sentense,count)
    elif select == 'decrypt':
        sentense=input("enter the sentence or word to decode: " ).lower()
        count=int(input("enter the number of letters to shift: " ))
        decode(sentense,count)
    else:
        print("enter any two of the given option" )
    choice=input("do you want to continue(yes or no): ").lower()
    if choice == 'yes':
        start = True
    else:
        start = False



