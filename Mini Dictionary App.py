dictionary={}
option=0
while option!=5:
    print("Mini Dictionary App\n1.Add/Update a word\n2.Retrieve a word's definition\n3.Delete a word\n4.View all words\n5.Exit")
    option=int(input("Enter your choice:"))
    if option==1:
        word=input("Enter your word:").strip()
        definition=input("Enter the definition:").strip()
        dictionary[word]=definition
        print(dictionary)
        print(f"{word} has been added to the dictionary")
