paket8 = [
    {
        "no": 1,
        "tipe": "Function Basics",
        "question": "Buat fungsi bernama `greet` yang menerima satu input:\n- `name` (string), nama seseorang.\nFungsi harus mencetak pesan: 'Hello <name>'.\nFungsi tidak mengembalikan nilai (return None).",
        "function_name": "greet",
        "test_cases": [
            (("Angus",), None),
            (("Ngahuia",), None)
        ],
        "hint": "Gunakan f-string untuk mencetak 'Hello {name}'.",
        "solution": "def greet(name):\n    print(f\"Hello {name}\")"
    },
    {
        "no": 2,
        "tipe": "String Formatting",
        "question": "Buat fungsi bernama `create_greeting` yang menerima tiga input:\n- `event_type` (string), jenis acara.\n- `event_id` (string), kode acara.\n- `person_name` (string), nama orang.\nFungsi harus mengembalikan string dengan format: 'Welcome to <event_type> <event_id>, <person_name>!'.",
        "function_name": "create_greeting",
        "test_cases": [
            (("International Conference", "IntConf2024", "Alice"), "Welcome to International Conference IntConf2024, Alice!"),
            (("Local Workshop", "WorkshopA1", "Bob"), "Welcome to Local Workshop WorkshopA1, Bob!"),
            (("Virtual Webinar", "VW2024", "Charlie"), "Welcome to Virtual Webinar VW2024, Charlie!")
        ],
        "hint": "Gunakan f-string untuk menyusun string.",
        "solution": "def create_greeting(event_type, event_id, person_name):\n    return f\"Welcome to {event_type} {event_id}, {person_name}!\""
    },
    {
        "no": 3,
        "tipe": "Math",
        "question": "Buat fungsi bernama `add` yang menerima dua input:\n- `num1` (integer), bilangan pertama.\n- `num2` (integer), bilangan kedua.\nFungsi harus mengembalikan hasil penjumlahan num1 + num2.",
        "function_name": "add",
        "test_cases": [
            ((5, 3), 8),
            ((-1, -1), -2)
        ],
        "hint": "Gunakan operator +.",
        "solution": "def add(num1, num2):\n    return num1 + num2"
    },
    {
        "no": 4,
        "tipe": "Condition",
        "question": "Buat fungsi bernama `can_receive` yang menerima tiga input:\n- `income` (integer), pendapatan tahunan.\n- `age` (integer), usia dalam tahun.\n- `asset` (integer), total aset.\nFungsi harus mengembalikan True jika memenuhi syarat pensiun:\n  • income < 50000\n  • age >= 65\n  • asset < 250000\nSelain itu, return False.",
        "function_name": "can_receive",
        "test_cases": [
            ((120000, 50, 490000), False),
            ((9000, 70, 50000), True),
            ((80000, 70, 90000), False)
        ],
        "hint": "Gunakan operator logika and.",
        "solution": "def can_receive(income, age, asset):\n    return income < 50000 and age >= 65 and asset < 250000"
    },
    {
        "no": 5,
        "tipe": "Loop & Math",
        "question": "Buat fungsi bernama `factorial` yang menerima satu input:\n- `number` (integer), bilangan bulat >= 0.\nFungsi harus mengembalikan nilai faktorial dari number. Definisi faktorial: n! = 1 × 2 × ... × n dan 0! = 1. Tidak boleh menggunakan math.factorial().",
        "function_name": "factorial",
        "test_cases": [
            ((0,), 1),
            ((5,), 120),
            ((7,), 5040)
        ],
        "hint": "Gunakan loop untuk mengalikan angka.",
        "solution": "def factorial(number):\n    result = 1\n    for i in range(1, number+1):\n        result *= i\n    return result"
    },
    {
        "no": 6,
        "tipe": "Condition",
        "question": "Buat fungsi bernama `factor_check` yang menerima dua input:\n- `n` (integer), bilangan utama.\n- `k` (integer), bilangan pembagi.\nFungsi harus mengembalikan string:\n  • 'This is a factor.' jika k adalah faktor dari n.\n  • 'This is not a factor.' jika bukan faktor.",
        "function_name": "factor_check",
        "test_cases": [
            ((28, 7), "This is a factor."),
            ((29, 7), "This is not a factor.")
        ],
        "hint": "Gunakan operator modulo %.",
        "solution": "def factor_check(n, k):\n    if n % k == 0:\n        return \"This is a factor.\"\n    else:\n        return \"This is not a factor.\""
    },
    {
        "no": 7,
        "tipe": "Math (Geometry)",
        "question": "Buat fungsi bernama `cylinder_volume` yang menerima dua input:\n- `radius` (float atau integer), jari-jari alas tabung.\n- `height` (float atau integer), tinggi tabung.\nFungsi harus mengembalikan volume tabung dengan rumus V = π × r² × h. Gunakan math.pi.",
        "function_name": "cylinder_volume",
        "test_cases": [
            ((10, 23), 7225.663103256525),
            ((5, 20), 1570.7963267948967)
        ],
        "hint": "Gunakan math.pi untuk nilai π.",
        "solution": "import math\n\ndef cylinder_volume(radius, height):\n    return math.pi * radius * radius * height"
    },
    {
        "no": 8,
        "tipe": "Loop & Condition",
        "question": "Buat fungsi bernama `count_down` yang menerima satu input:\n- `start` (integer), bilangan awal.\nFungsi harus mencetak angka mundur dari start hingga 1. Jika start < 1, cetak 'Starting number must be at least 1.'. Fungsi tidak mengembalikan nilai (return None).",
        "function_name": "count_down",
        "test_cases": [
            ((5,), None),
            ((0,), None),
            ((-3,), None)
        ],
        "hint": "Gunakan while loop untuk hitung mundur.",
        "solution": "def count_down(start):\n    if start < 1:\n        print(\"Starting number must be at least 1.\")\n    else:\n        while start >= 1:\n            print(start)\n            start -= 1"
    },
    {
        "no": 9,
        "tipe": "Math & Formatting",
        "question": "Buat fungsi bernama `print_kinetic_energy` yang menerima dua input:\n- `mass` (float), massa dalam kilogram.\n- `velocity` (float), kecepatan dalam meter/detik.\nFungsi harus menghitung energi kinetik KE = 0.5 × m × v² lalu mencetak: 'Mass (m): <mass> kg, Velocity (v): <velocity> m/s, Kinetic Energy (KE): <ke> Joules.' dengan 2 angka desimal. Fungsi tidak me-return nilai.",
        "function_name": "print_kinetic_energy",
        "test_cases": [
            ((10, 5), None),
            ((50, 20), None)
        ],
        "hint": "Gunakan f-string dengan {value:.2f}.",
        "solution": "def print_kinetic_energy(mass, velocity):\n    ke = 0.5 * mass * (velocity**2)\n    print(f\"Mass (m): {mass:.2f} kg, Velocity (v): {velocity:.2f} m/s, Kinetic Energy (KE): {ke:.2f} Joules.\")"
    },
    {
    "no": 10,
    "tipe": "While Loop & List",
    "question": "Buat fungsi bernama `print_names` yang menerima satu input:\n- `names` (list of string), daftar nama.\nFungsi harus mencetak semua nama dalam urutan alfabet (A–Z), satu per baris. Jika list kosong, cetak 'None'. Gunakan while loop. Fungsi tidak mengembalikan nilai.",
    "function_name": "print_names",
    "test_cases": [
        ((["Alice", "Claire", "Elena", "Diana", "Bob"],), None),
        (([],), None),
        ((["Anna-Lee", "O'Connor", "Jean-Luc", "Maeve", "Zoë"],), None)
    ],
    "hint": "Cek list kosong lebih dulu. Jika tidak kosong, urutkan dengan sorted() lalu iterasi dengan while loop.",
    "solution": "def print_names(names):\n    if not names:\n        print(\"None\")\n        return\n    sorted_names = sorted(names)\n    i = 0\n    while i < len(sorted_names):\n        print(sorted_names[i])\n        i += 1"
    }
    ,{
        "no": 11,
        "tipe": "Dictionary",
        "question": "Buat fungsi bernama `add_or_update_address` yang menerima tiga input:\n- `address_dict` (dict), dictionary berisi pasangan username → alamat.\n- `username` (string), nama pengguna.\n- `address` (string), alamat baru.\nJika username belum ada, tambahkan ke dictionary dan cetak 'Address added'. Jika sudah ada, update alamat dan cetak 'Address updated'. Fungsi tidak mengembalikan nilai.",
        "function_name": "add_or_update_address",
        "test_cases": [
            (({'abc001': 'Sydney', 'xyz999': 'Auckland'}, 'rst123', 'LA'), None),
            (({'abc001': 'Sydney', 'rst123': 'Auckland'}, 'rst123', 'Jakarta'), None)
        ],
        "hint": "Gunakan `in` untuk mengecek apakah username ada di dictionary.",
        "solution": "def add_or_update_address(address_dict, username, address):\n    if username in address_dict:\n        address_dict[username] = address\n        print(\"Address updated\")\n    else:\n        address_dict[username] = address\n        print(\"Address added\")"
    },
    {
        "no": 12,
        "tipe": "Tuple & List",
        "question": "Buat fungsi bernama `total_value_and_weight` yang menerima satu input:\n- `item_list` (list of tuple), setiap tuple berisi (value, weight).\nFungsi harus mengembalikan tuple berisi (total_value, total_weight). Jika list kosong, return (0, 0).",
        "function_name": "total_value_and_weight",
        "test_cases": [
            (([(100.0, 10.5), (200.5, 20.0), (50.0, 5.0)],), (350.5, 35.5)),
            (([],), (0, 0))
        ],
        "hint": "Gunakan sum() dengan comprehension.",
        "solution": "def total_value_and_weight(item_list):\n    total_value = sum(v for v, w in item_list)\n    total_weight = sum(w for v, w in item_list)\n    return (total_value, total_weight)"
    },
    {
        "no": 13,
        "tipe": "Nested List",
        "question": "Buat fungsi bernama `promote_marks_list` yang menerima dua input:\n- `student_marks_list` (list of list of int/float), nilai ujian tiap siswa.\n- `rate` (float), faktor pengali.\nFungsi harus mengembalikan list baru dengan setiap nilai dikalikan rate, dibulatkan 1 angka desimal.",
        "function_name": "promote_marks_list",
        "test_cases": [
            (([[65, 70, 75], [80, 85, 90], [55, 60, 65]], 1.1), [[71.5, 77.0, 82.5], [88.0, 93.5, 99.0], [60.5, 66.0, 71.5]]),
            (([[50, 60, 70], [80, 90, 100]], 1), [[50, 60, 70], [80, 90, 100]]),
            (([[90, 95, 100], [70, 75, 80]], 0.9), [[81.0, 85.5, 90.0], [63.0, 67.5, 72.0]])
        ],
        "hint": "Gunakan nested list comprehension dengan round().",
        "solution": "def promote_marks_list(student_marks_list, rate):\n    return [[round(mark * rate, 1) for mark in student] for student in student_marks_list]"
    },
    {
    "no": 14,
    "tipe": "Tuple & List",
    "question": "Buat fungsi bernama `cities_with_population_over` yang menerima dua input:\n- `city_list` (list of tuple), setiap tuple berisi (city_name, country, population).\n- `threshold` (int), batas populasi.\nFungsi harus **mengembalikan** list nama kota unik (string, title-cased) yang memiliki population >= threshold. Urutan hasil mengikuti urutan pertama kali muncul di input. Jika tidak ada kota yang memenuhi syarat, kembalikan list kosong.",
    "function_name": "cities_with_population_over",
    "test_cases": [
        (([('sydney','Australia',3000000), ('sydney','Canada',500000)], 1000), ['Sydney']),
        (([('Tokyo','Japan',13900000), ('Osaka','Japan',2700000), ('Tokyo','Japan',13900000)], 2000000), ['Tokyo', 'Osaka']),
        (([], 1), [])
    ],
    "hint": "Gunakan struktur data set untuk memastikan nama kota tidak duplikat, tapi tetap jaga urutan dengan list tambahan.",
    "solution": "def cities_with_population_over(city_list, threshold):\n    seen = set()\n    result = []\n    for city, country, population in city_list:\n        if population >= threshold:\n            cname = city.title()\n            if cname not in seen:\n                seen.add(cname)\n                result.append(cname)\n    return result"
    },
    {
        "no": 15,
        "tipe": "Dictionary",
        "question": "Buat fungsi bernama `get_value_frequency` yang menerima dua input:\n- `freq_dict` (dict), dictionary berisi key dan frequency (int).\n- `target_frequency` (int), nilai frequency yang dicari.\nFungsi harus mengembalikan berapa kali target_frequency muncul sebagai value dalam dictionary.",
        "function_name": "get_value_frequency",
        "test_cases": [
            (({'apple': 2, 'banana': 3, 'cherry': 2}, 2), 2),
            (({'apple': 1, 'banana': 1}, 3), 0)
        ],
        "hint": "Gunakan list(freq_dict.values()).count().",
        "solution": "def get_value_frequency(freq_dict, target_frequency):\n    return list(freq_dict.values()).count(target_frequency)"
    },
    {
        "no": 16,
        "tipe": "Condition",
        "question": "Buat fungsi bernama `caught_speeding` yang menerima dua input:\n- `speed` (integer), kecepatan mobil.\n- `is_birthday` (boolean), True jika hari ulang tahun pengemudi.\nAturan:\n  • speed <= 60 → 'You have no tickets.'\n  • 61–80 → 'You have a small ticket.'\n  • >=81 → 'You have a big ticket.'\nJika is_birthday True, semua batas kecepatan naik +5 mph.\nFungsi harus mengembalikan string sesuai aturan.",
        "function_name": "caught_speeding",
        "test_cases": [
            ((60, False), "You have no tickets."),
            ((85, False), "You have a big ticket."),
            ((85, True), "You have a small ticket.")
        ],
        "hint": "Tambahkan allowance 5 jika is_birthday True.",
        "solution": "def caught_speeding(speed, is_birthday):\n    allowance = 5 if is_birthday else 0\n    if speed <= 60 + allowance:\n        return \"You have no tickets.\"\n    elif speed <= 80 + allowance:\n        return \"You have a small ticket.\"\n    else:\n        return \"You have a big ticket.\""
    },
    {
    "no": 17,
    "tipe": "NumPy",
    "question": "Buat fungsi bernama `extract_negatives` yang menerima satu input:\n- `numbers` (numpy array atau list of int/float).\nFungsi harus mengembalikan list berisi hanya bilangan negatif. Tidak boleh menggunakan loop/if/list comprehension.",
    "function_name": "extract_negatives",
    "test_cases": [
        (([0, -1, 2, -3, 4, -5, 6],), [-1, -3, -5]),
        (([-10, -20, -30],), [-10, -20, -30]),
        (([1, 2, 3, 4],), [])
    ],
    "hint": "Gunakan indexing boolean di numpy array lalu ubah hasilnya menjadi list dengan .tolist().",
    "solution": "import numpy as np\n\ndef extract_negatives(numbers):\n    arr = np.array(numbers)\n    return arr[arr < 0].tolist()"
    },
    {
    "no": 18,
    "tipe": "NumPy",
    "question": "Buat fungsi bernama `extract_positives` yang menerima satu input:\n- `numbers` (numpy array atau list of int/float).\nFungsi harus mengembalikan list berisi hanya bilangan positif (> 0). Tidak boleh menggunakan loop/if/list comprehension.",
    "function_name": "extract_positives",
    "test_cases": [
        (([0, -1, 2, -3, 4, -5, 6],), [2, 4, 6]),
        (([-10, -20, -30],), []),
        (([1, 2, 3, 4],), [1, 2, 3, 4])
    ],
    "hint": "Gunakan indexing boolean di numpy array lalu ubah hasilnya menjadi list dengan .tolist().",
    "solution": "import numpy as np\n\ndef extract_positives(numbers):\n    arr = np.array(numbers)\n    return arr[arr > 0].tolist()"
    },
    {
    "no": 19,
    "tipe": "NumPy",
    "question": "Buat fungsi bernama `extract_evens` yang menerima satu input:\n- `numbers` (numpy array atau list of int).\nFungsi harus mengembalikan list berisi hanya bilangan genap. Tidak boleh menggunakan loop/if/list comprehension.",
    "function_name": "extract_evens",
    "test_cases": [
        (([0, -1, 2, -3, 4, -5, 6],), [0, 2, 4, 6]),
        (([1, 3, 5],), []),
        (([10, 20, 30],), [10, 20, 30])
    ],
    "hint": "Gunakan operasi modulo (%) pada array NumPy, lalu indexing boolean, dan akhiri dengan .tolist().",
    "solution": "import numpy as np\n\ndef extract_evens(numbers):\n    arr = np.array(numbers)\n    return arr[arr % 2 == 0].tolist()"
    },
    {
        "no": 20,
        "tipe": "Exception Handling",
        "question": "Buat fungsi bernama `check_file` yang menerima dua input:\n- `data` (list), daftar elemen.\n- `n` (integer), posisi index.\nFungsi harus mencetak elemen ke-n. Jika index invalid, tangkap exception dan cetak 'Invalid position provided.'. Fungsi tidak mengembalikan nilai.",
        "function_name": "check_file",
        "test_cases": [
            (([10,20,30], 0), None),
            (([10,20,30], 3), None),
            ((['bob','carol','ted','alice'], 3), None),
            ((['bob','carol','ted','alice'], -6), None)
        ],
        "hint": "Gunakan try-except untuk IndexError.",
        "solution": "def check_file(data, n):\n    try:\n        print(data[n])\n    except IndexError:\n        print(\"Invalid position provided.\")"
    },
    {
        "no": 21,
        "tipe": "Class",
        "question": "Buat class bernama `Person` dengan atribut:\n- `name` (string), nama orang.\n- `height` (float), tinggi badan dalam cm.\nSaat objek dicetak, tampilkan format: Person('<name>', <height>).",
        "function_name": "Person",
        "test_cases": [],
        "hint": "Gunakan __str__ dan __repr__ untuk kontrol tampilan.",
        "solution": "class Person:\n    def __init__(self, name, height):\n        self.name = name\n        self.height = height\n    def __str__(self):\n        return f\"Person('{self.name}', {self.height})\"\n    def __repr__(self):\n        return self.__str__()"
    },
    {
        "no": 22,
        "tipe": "Class",
        "question": "Buat class bernama `Bird` dengan atribut:\n- `kind` (string), jenis burung.\n- `length` (float), panjang tubuh dalam cm.\n- `colour` (string), warna.\n- `can_fly` (boolean), True jika bisa terbang.\nSaat objek dicetak, tampilkan format: '<kind> (<length> cm), <colour>, can fly/flightless'.\nTambahkan method `grow(amount)` untuk menambah panjang burung sebanyak amount.",
        "function_name": "Bird",
        "test_cases": [],
        "hint": "Gunakan f-string dan cek kondisi can_fly.",
        "solution": "class Bird:\n    def __init__(self, kind, length, colour, can_fly):\n        self.kind = kind\n        self.length = length\n        self.colour = colour\n        self.can_fly = can_fly\n    def __str__(self):\n        fly_status = 'can fly' if self.can_fly else 'flightless'\n        return f\"{self.kind} ({self.length:.1f} cm), {self.colour}, {fly_status}\"\n    def __repr__(self):\n        return self.__str__()\n    def grow(self, amount):\n        self.length += amount"
    }
    
]
