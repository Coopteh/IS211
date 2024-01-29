# Описание
Паттерн "Адаптер" адаптирует методы одного (старого) класса к другому (новому), например
```
class IntObject:
    def __init__(self, n):
        self.__n = n
    def get(self):
        return self.__n

class StrObject:
    def __init__(self, str):
        self.__str = str
    def get(self):
        return self.__set

class AdapterToStr(IntObject):
    def __init__(self, int_obj):
        self.int_obj = int_obj
    def get_str(self):
        return str( self.int_obj.get() )


# Использование
def main():
    obj = IntObject(10)
    obj_str = AdapterToStr( obj ).get_str()
    print( obj_str, type(obj_str) )

if __name__ == "__main__":
    main()
```
