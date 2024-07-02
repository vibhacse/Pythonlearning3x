#Multiple Inheritance - Another Example

class maruti():
    print("I am maruti")

    def hybrid(self):
        print("I am maruti petrol engine")

class toyota():
    print("I am toyota")

    def hybrid(self):
        print("I am toyota hybrid engine")


class hyryder_mild(maruti, toyota): # method resolution
    pass

mildhyryder = hyryder_mild()
mildhyryder.hybrid()

class hyryder_strong(toyota, maruti): # method resolution
    pass

stronghyryder = hyryder_strong()
stronghyryder.hybrid()
