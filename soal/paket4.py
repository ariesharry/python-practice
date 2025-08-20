# file: paket_tuple_set_dict.py
paket4 = [
    {
        "no": 1,
        "tipe": "Tuple",
        "question": "Buat fungsi bernama `get_second_item` yang menerima sebuah tuple dan mengembalikan elemen kedua dari tuple tersebut.",
        "function_name": "get_second_item",
        "test_cases": [
            ((("apel", "jeruk", "mangga"),), "jeruk"),
            ((("x", "y", "z"),), "y"),
            ((("satu", "dua"),), "dua")
        ],
        "hint": "Gunakan indexing pada tuple: tuple[1].",
        "solution": "def get_second_item(data):\n    return data[1]"
    },
    {
        "no": 2,
        "tipe": "Tuple",
        "question": "Buat fungsi bernama `swap_coordinates` yang menerima sebuah tuple (x, y) dan mengembalikan tuple baru dengan posisi dibalik (y, x).",
        "function_name": "swap_coordinates",
        "test_cases": [
            (((3, 5),), (5, 3)),
            (((10, -2),), (-2, 10)),
            (((0, 0),), (0, 0))
        ],
        "hint": "Lakukan tuple unpacking ke variabel x dan y, lalu kembalikan (y, x).",
        "solution": "def swap_coordinates(coords):\n    x, y = coords\n    return (y, x)"
    },
    {
        "no": 3,
        "tipe": "Set",
        "question": "Buat fungsi bernama `unique_numbers` yang menerima sebuah list angka dan mengembalikan set berisi angka-angka unik dari list tersebut.",
        "function_name": "unique_numbers",
        "test_cases": [
            (([1, 2, 2, 3, 4, 4, 5],), {1, 2, 3, 4, 5}),
            (([10, 10, 10],), {10}),
            (([],), set())
        ],
        "hint": "Gunakan fungsi set() untuk menghilangkan duplikasi dari list.",
        "solution": "def unique_numbers(nums):\n    return set(nums)"
    },
    {
        "no": 4,
        "tipe": "Set",
        "question": "Buat fungsi bernama `common_fruits` yang menerima dua set berisi nama buah dan mengembalikan set berisi buah yang ada di kedua set tersebut.",
        "function_name": "common_fruits",
        "test_cases": [
            (({'apel', 'jeruk', 'mangga'}, {'mangga', 'apel', 'pisang'}), {'apel', 'mangga'}),
            (({'melon', 'semangka'}, {'apel', 'jeruk'}), set()),
            (({'durian'}, {'durian'}), {'durian'})
        ],
        "hint": "Gunakan operasi intersection pada set (operator & atau method .intersection()).",
        "solution": "def common_fruits(set1, set2):\n    return set1 & set2"
    },
    {
        "no": 5,
        "tipe": "Dictionary",
        "question": "Buat fungsi bernama `get_score` yang menerima dictionary `nilai` dan sebuah nama siswa. Fungsi harus mengembalikan nilai siswa tersebut.",
        "function_name": "get_score",
        "test_cases": [
            (({"Andi": 90, "Budi": 80}, "Budi"), 80),
            (({"Siti": 95, "Rina": 85}, "Siti"), 95),
            (({"Ali": 70}, "Ali"), 70)
        ],
        "hint": "Akses value dictionary menggunakan key: dict[key].",
        "solution": "def get_score(nilai, nama):\n    return nilai[nama]"
    },
    {
    "no": 6,
    "tipe": "Dictionary",
    "question": "Buat fungsi bernama `count_students` yang menerima dictionary nilai siswa (nama sebagai key, nilai sebagai value). Fungsi harus mengembalikan jumlah siswa dalam dictionary tersebut.",
    "function_name": "count_students",
    "test_cases": [
        (({'Andi': 85, 'Budi': 78, 'Siti': 92},), 3),
        (({'Rina': 88, 'Tono': 70},), 2),
        (({},), 0)
    ],
    "hint": "Gunakan fungsi bawaan len() untuk menghitung jumlah item dalam dictionary.",
    "solution": "def count_students(scores):\n    return len(scores)"
    },
    {
        "no": 7,
        "tipe": "File Processing",
        "question": "Buat fungsi bernama `count_lines` yang menerima nama file (string). Fungsi harus mengembalikan jumlah baris dalam file tersebut.",
        "function_name": "count_lines",
        "test_cases": [
            (("sample1.txt",), 3),   # isi file sample1.txt punya 3 baris
            (("sample2.txt",), 0)    # isi file sample2.txt kosong
        ],
        "hint": "Gunakan with open(filename, 'r') as f lalu iterasi setiap baris atau gunakan read().splitlines().",
        "solution": "def count_lines(filename):\n    with open(filename, 'r') as f:\n        return len(f.read().splitlines())"
    },
    {
        "no": 8,
        "tipe": "File Processing",
        "question": "Buat fungsi bernama `write_uppercase` yang menerima dua parameter: `input_file` dan `output_file`. Fungsi harus membaca isi `input_file`, mengubah semua huruf menjadi kapital, lalu menuliskannya ke `output_file`.",
        "function_name": "write_uppercase",
        "test_cases": [
            (("input1.txt", "output1.txt"), None),  # cek manual apakah output1.txt berisi huruf kapital
        ],
        "hint": "Gunakan string.upper() untuk mengubah isi file menjadi huruf kapital, lalu tulis dengan mode 'w'.",
        "solution": "def write_uppercase(input_file, output_file):\n    with open(input_file, 'r') as f:\n        data = f.read()\n    with open(output_file, 'w') as f:\n        f.write(data.upper())"
    }

]
