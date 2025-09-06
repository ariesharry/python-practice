paket6 = [
    {
        "no": 1,
        "tipe": "OOP",
        "question": "Buat class bernama `Person` dengan atribut `name` dan `age`. Tambahkan method `introduce` yang mengembalikan string perkenalan dalam format: 'Halo, nama saya {name} dan umur saya {age} tahun.'",
        "function_name": "Person",
        "test_cases": [
            ((("Andi", 25), "introduce"), "Halo, nama saya Andi dan umur saya 25 tahun."),
            ((("Budi", 30), "introduce"), "Halo, nama saya Budi dan umur saya 30 tahun.")
        ],
        "hint": "Gunakan method `__init__` untuk atribut dan buat method `introduce` untuk mengembalikan string.",
        "solution": "class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    def introduce(self):\n        return f\"Halo, nama saya {self.name} dan umur saya {self.age} tahun.\""
    },
    {
        "no": 2,
        "tipe": "OOP",
        "question": "Buat class bernama `Rectangle` dengan atribut `width` dan `height`. Tambahkan method `area` yang mengembalikan luas persegi panjang.",
        "function_name": "Rectangle",
        "test_cases": [
            (( (5, 10), "area"), 50),
            (( (7, 3), "area"), 21)
        ],
        "hint": "Luas = width * height. Simpan atribut di `__init__`, lalu method `area` mengembalikan hasil perkalian.",
        "solution": "class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height"
    },
    {
        "no": 3,
        "tipe": "OOP",
        "question": "Buat class bernama `BankAccount` dengan atribut `owner` dan `balance`. Tambahkan method `deposit(amount)` untuk menambah saldo dan `withdraw(amount)` untuk mengurangi saldo. `withdraw` hanya boleh dilakukan jika saldo cukup.",
        "function_name": "BankAccount",
        "test_cases": [
            ((("Andi", 1000), "get_balance"), 1000),
            ((("Budi", 500), "get_balance"), 500)
        ],
        "hint": "Gunakan if untuk cek saldo sebelum withdraw. Tambahkan juga method `get_balance()` untuk melihat saldo akhir.",
        "solution": "class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n    def deposit(self, amount):\n        self.balance += amount\n    def withdraw(self, amount):\n        if self.balance >= amount:\n            self.balance -= amount\n    def get_balance(self):\n        return self.balance"
    },
    {
        "no": 4,
        "tipe": "OOP",
        "question": "Buat class `Animal` dengan method `sound()` yang mengembalikan string 'Suara hewan'. Kemudian buat class `Dog` yang mewarisi dari `Animal` dan override method `sound()` untuk mengembalikan 'Guk guk'.",
        "function_name": "Dog",
        "test_cases": [
            (((), "sound"), "Guk guk")
        ],
        "hint": "Gunakan inheritance: class Dog(Animal). Override method dengan nama yang sama.",
        "solution": "class Animal:\n    def sound(self):\n        return \"Suara hewan\"\n\nclass Dog(Animal):\n    def sound(self):\n        return \"Guk guk\""
    },
    {
        "no": 5,
        "tipe": "OOP",
        "question": "Buat class `Vehicle` dengan atribut `brand`. Tambahkan method `drive()` yang mengembalikan string '{brand} sedang berjalan'. Kemudian buat class `Car` yang mewarisi dari `Vehicle` dan tambahkan atribut `doors`. Override method `drive()` untuk mengembalikan '{brand} dengan {doors} pintu sedang melaju'.",
        "function_name": "Car",
        "test_cases": [
            ((("Toyota", 4), "drive"), "Toyota dengan 4 pintu sedang melaju")
        ],
        "hint": "Gunakan super().__init__ di subclass Car untuk memanggil constructor Vehicle.",
        "solution": "class Vehicle:\n    def __init__(self, brand):\n        self.brand = brand\n    def drive(self):\n        return f\"{self.brand} sedang berjalan\"\n\nclass Car(Vehicle):\n    def __init__(self, brand, doors):\n        super().__init__(brand)\n        self.doors = doors\n    def drive(self):\n        return f\"{self.brand} dengan {self.doors} pintu sedang melaju\""
    }
]
