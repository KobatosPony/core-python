class Single:
    _instance = False

    def __new__(cls, *args, **kwargs):
        if not Single._instance:
            Single._instance =  object.__new__(cls)
        return Single._instance

    def __init__(self):
        self.name = "Single"

print(id(Single()))
print(id(Single()))