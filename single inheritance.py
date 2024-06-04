class test:
    def __init__(self):
        self.x=0
class test2(test):
    def __init__(self):
        self.y=1
        test.__init__(self)
def main():
    b=test2()
    print(b.x,b.y)
main()