class calc:
    def div(self, a, b):

        try:
            print(a / b)
        except Exception as e:
            print(e)
        else:
            print("Valid values")
        finally:
            print("The End")

add = calc()
add.div(10,0)
add.div(20,10)
