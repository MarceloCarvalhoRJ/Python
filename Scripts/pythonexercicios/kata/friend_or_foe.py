def friend(x):  
    return [c for c in x if len(c) == 4]

print(friend(["Ryan", "Kieran", "Mark"]))

'''def friend(x):
    friends = list()
    friends.extend(c for c in x if len(c) == 4) #extend() -> adiciona cada amigo como elemento individual ao inves de adicionar como unico elemento.  
    return friends'''