class mammal():
    def walk(self):
        print("Walk")


class dog(mammal):
    def bark(self):
        print("Bark")


class cat(mammal):
    def meow(self):
        print("Meow")


dog1=dog()
dog1.walk()
dog1.bark()
cat1=cat()
cat1.meow()