"""class Shark:
    animal_type = 'fish'
    location = 'ocean'
    followers = 5

new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)

class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age

new_shark = Shark('nemo', 20)
print(new_shark.name)
print(new_shark.age)

"""
class Shark:
    animal_type = 'fish'
    location = 'ocean'
    followers = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def set_followers(self, followers_p):
        self.followers = followers_p
        print('esse cara tem ' + str(followers_p) + ' seguidores')
    
    def set_name(self, name_p):
        self.name = name_p
        print('o nome do tubarao e ' + str(name_p))

    def zera_tudo(self):
         self.animal_type = ''
         self.location = ''
         self.followers = 0
         self.name = ''
         self.age = 0
         print('tudo limpo')


new_shark = Shark('Sammy', 20)
print('o nome do tubarao e: ' + str(new_shark.name))

#print(new_shark.followers)
new_shark.set_followers(5)
print(new_shark.followers)
new_shark.set_name('ze')
print(new_shark.name)

new_shark.zera_tudo()
print(new_shark.name)


