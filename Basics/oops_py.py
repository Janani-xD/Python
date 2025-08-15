class MyClass:
    class_variable = "Hello!, Class!"

    @staticmethod
    def static_method():
        return "I dont access the class or instance"

    @classmethod
    def class_method(cls):
        return f"Class Variable is {cls.class_variable}"

print(MyClass.static_method())
print(MyClass.class_method())