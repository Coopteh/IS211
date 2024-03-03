### Задание: Работа с сериализацией и десериализацией объектов на PHP

Нужно создать классы, которые могут быть сериализованы и десериализованы в PHP.  

Они будут использовать встроенные функции PHP для сериализации объектов в строку и восстановления объекта из строки.
Читайте подробнее (serialize)[https://www.php.net/manual/ru/function.serialize.php], (unserialize)[https://www.php.net/manual/ru/function.unserialize.php]

**Шаги**

1. Создайте класс Student, содержащий свойства об объекте студента (например, имя `$name`, возраст `$age`, курс `$course`)

2. Реализуйте методы serialize() и unserialize() в классе Student:
   - Метод serialize() должен преобразовывать объект класса Student в строку.
   `serialize([$this->name, $this->age, $this->course]);`
   - Метод unserialize() должен извлекать объект класса Student из строки и восстанавливать его.  
    `[$this->name, $this->age, $this->course] = unserialize($data);`

3. Создайте объект класса Student, заполните его данными и протестируйте сериализацию и десериализацию объекта.
```
// Создание объекта и сериализация
$student = new Student("Андрей", 18, "ИС-211");
$serializedData = $student->serialize();

// Десериализация объекта
$restoredStudent = new Student("", 0, "");
$restoredStudent->unserialize($serializedData);

// Проверка десериализованного объекта
echo "Восстановленный студент: Имя - {$restoredStudent->name}, Возраст - {$restoredStudent->age}, Курс - {$restoredStudent->course}";
```

Это задание показывает как сохранять и восстанавливать состояние объекта (его поля с данными)
с использованием встроенных функций PHP сериализации и десериализации объекта (перевода его в строку и обратно).  
