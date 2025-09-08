paket7 = [
    {
        "no": 1,
        "tipe": "Function Basics",
        "question": "Buat fungsi bernama `greet` yang menerima sebuah nama dan mencetak 'Hello <nama>'.",
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
        "tipe": "Formatting",
        "question": "Buat fungsi `print_coordinates` yang menerima dua float dan mencetak dalam format (x, y) dengan 1 digit desimal.",
        "function_name": "print_coordinates",
        "test_cases": [
            ((3.14159, 2.71828), None),
            ((-1.2345, 6.789), None),
            ((0.0, -0.12345), None)
        ],
        "hint": "Gunakan format string dengan {value:.1f}.",
        "solution": "def print_coordinates(x_coord, y_coord):\n    print(f\"({x_coord:.1f}, {y_coord:.1f})\")"
    },
    {
        "no": 3,
        "tipe": "Math Conversion",
        "question": "Buat fungsi `to_kilometres` yang mengubah mil ke kilometer (1 mil = 1.60934 km).",
        "function_name": "to_kilometres",
        "test_cases": [
            ((2.0,), 3.21868),
            ((100.0,), 160.934)
        ],
        "hint": "Kalikan miles dengan 1.60934.",
        "solution": "def to_kilometres(miles):\n    return float(miles * 1.60934)"
    },
    {
        "no": 4,
        "tipe": "Math",
        "question": "Buat fungsi `calculate_rectangle_area` untuk menghitung luas persegi panjang.",
        "function_name": "calculate_rectangle_area",
        "test_cases": [
            ((5, 3), 15),
            ((2.5, 4), 10.0),
            ((0, 10), 0)
        ],
        "hint": "Gunakan rumus luas = width * height.",
        "solution": "def calculate_rectangle_area(width, height):\n    return width * height"
    },
    {
        "no": 5,
        "tipe": "Loop & Formatting",
        "question": "Buat fungsi `print_reciprocals` yang mencetak kebalikan (1/n) setiap angka dalam list dengan 4 digit desimal.",
        "function_name": "print_reciprocals",
        "test_cases": [
            (([3, 5, 1],), None),
            (([11],), None)
        ],
        "hint": "Iterasi list, hitung 1/n, cetak dengan format {value:.4f}.",
        "solution": "def print_reciprocals(nums):\n    for n in nums:\n        reciprocal = 1 / n\n        print(f\"1/{n} = {reciprocal:.4f}\")"
    },
    {
        "no": 6,
        "tipe": "Math Conversion",
        "question": "Buat fungsi `convert_to_celsius` yang mengubah Fahrenheit ke Celsius dengan rumus (F - 32) * 5/9.",
        "function_name": "convert_to_celsius",
        "test_cases": [
            ((32.0,), 0.0),
            ((212.0,), 100.0),
            ((-40.0,), -40.0)
        ],
        "hint": "Gunakan formula (F - 32) * 5/9.",
        "solution": "def convert_to_celsius(degrees_f):\n    return (degrees_f - 32) * (5/9)"
    },
    {
        "no": 7,
        "tipe": "List & Math",
        "question": "Buat fungsi `sum_products` yang menjumlahkan hasil perkalian elemen-elemen dua list dengan panjang sama.",
        "function_name": "sum_products",
        "test_cases": [
            (([1.5, 10.0], [10.0, 2.0]), 35.0),
            (([40.0, 60.0], [0.7, 0.3]), 46.0)
        ],
        "hint": "Gunakan zip() untuk mengiterasi dua list sekaligus.",
        "solution": "def sum_products(nums1, nums2):\n    total = 0\n    for a, b in zip(nums1, nums2):\n        total += a * b\n    return total"
    },
    {
        "no": 8,
        "tipe": "Condition",
        "question": "Buat fungsi `num_adult_tickets` yang menghitung jumlah tiket yang dibutuhkan untuk 2 kakek/nenek (gratis jika usia >= 65) + 1 untuk diri sendiri.",
        "function_name": "num_adult_tickets",
        "test_cases": [
            ((63, 64), 3),
            ((63, 65), 2),
            ((65, 63), 2),
            ((66, 100), 1)
        ],
        "hint": "Mulai dengan 1 tiket (diri sendiri), tambah jika usia < 65.",
        "solution": "def num_adult_tickets(grandparent1_age, grandparent2_age):\n    tickets = 1\n    if grandparent1_age < 65:\n        tickets += 1\n    if grandparent2_age < 65:\n        tickets += 1\n    return tickets"
    },
    {
        "no": 9,
        "tipe": "List & Condition",
        "question": "Buat fungsi `num_good_wines` yang menghitung jumlah wine dengan kualitas >= 7.",
        "function_name": "num_good_wines",
        "test_cases": [
            (([7.5, 6.7, 7.0, 9.1, 6.9, 4.9],), 3),
            (([6.5, 6.9, 5.9, 3.1, 6.0],), 0)
        ],
        "hint": "Gunakan loop atau list comprehension dengan kondisi >= 7.",
        "solution": "def num_good_wines(quality_values):\n    return sum(1 for q in quality_values if q >= 7)"
    },
    {
        "no": 10,
        "tipe": "Nested List",
        "question": "Buat fungsi `promote_marks_list` yang mengalikan setiap nilai ujian dalam list siswa dengan rate, hasil dibulatkan 1 desimal.",
        "function_name": "promote_marks_list",
        "test_cases": [
            (([[65, 70, 75], [80, 85, 90], [55, 60, 65]], 1.1), [[71.5, 77.0, 82.5], [88.0, 93.5, 99.0], [60.5, 66.0, 71.5]]),
            (([[50, 60, 70], [80, 90, 100]], 1), [[50, 60, 70], [80, 90, 100]]),
            (([[90, 95, 100], [70, 75, 80]], 0.9), [[81.0, 85.5, 90.0], [63.0, 67.5, 72.0]])
        ],
        "hint": "Gunakan nested loop atau list comprehension dengan round().",
        "solution": "def promote_marks_list(student_marks_list, rate):\n    return [[round(mark * rate, 1) for mark in student] for student in student_marks_list]"
    },
    {
        "no": 11,
        "tipe": "Loop & Math",
        "question": "Buat fungsi `sum_of_squares` yang menghitung jumlah kuadrat dari 1 sampai n.",
        "function_name": "sum_of_squares",
        "test_cases": [
            ((0,), 0),
            ((3,), 14),
            ((5,), 55)
        ],
        "hint": "Gunakan range(1, n+1) lalu jumlahkan i*i.",
        "solution": "def sum_of_squares(n):\n    return sum(i*i for i in range(1, n+1))"
    },
    {
        "no": 12,
        "tipe": "Condition",
        "question": "Buat fungsi `is_positive` yang mengembalikan True jika angka > 0, jika tidak False.",
        "function_name": "is_positive",
        "test_cases": [
            ((5,), True),
            ((-4,), False),
            ((0,), False)
        ],
        "hint": "Cukup cek apakah num > 0.",
        "solution": "def is_positive(num):\n    return num > 0"
    },
    {
        "no": 13,
        "tipe": "Condition",
        "question": "Buat fungsi `grade` yang menerima nilai 0-100 dan mengembalikan huruf A/B/C/D/F sesuai rentang.",
        "function_name": "grade",
        "test_cases": [
            ((95,), "A"),
            ((82,), "B"),
            ((50,), "F")
        ],
        "hint": "Gunakan if-elif-else dengan rentang nilai.",
        "solution": "def grade(score):\n    if score >= 90:\n        return 'A'\n    elif score >= 80:\n        return 'B'\n    elif score >= 70:\n        return 'C'\n    elif score >= 60:\n        return 'D'\n    else:\n        return 'F'"
    },
    {
        "no": 14,
        "tipe": "List",
        "question": "Buat fungsi `repeat_elements` yang mengulang setiap elemen list sebanyak n kali.",
        "function_name": "repeat_elements",
        "test_cases": [
            (([1, 2, 3], 2), [1, 1, 2, 2, 3, 3]),
            ((['a', 'b'], 3), ['a', 'a', 'a', 'b', 'b', 'b']),
            (([1], 4), [1, 1, 1, 1])
        ],
        "hint": "Gunakan loop atau list comprehension untuk mengulang elemen.",
        "solution": "def repeat_elements(lst, n):\n    return [x for x in lst for _ in range(n)]"
    },
    {
        "no": 15,
        "tipe": "List & Condition",
        "question": "Buat fungsi `get_element_at_index` yang mengambil elemen list sesuai index. Jika out of bounds, return None.",
        "function_name": "get_element_at_index",
        "test_cases": [
            (([1, 2, 3], 1), 2),
            ((['a', 'b', 'c'], 0), 'a'),
            (([1, 2, 3], 3), None)
        ],
        "hint": "Gunakan try-except atau cek panjang list.",
        "solution": "def get_element_at_index(lst, index):\n    if 0 <= index < len(lst):\n        return lst[index]\n    return None"
    },
    {
        "no": 16,
        "tipe": "List",
        "question": "Buat fungsi `modify_list` yang memindahkan elemen terakhir ke depan list.",
        "function_name": "modify_list",
        "test_cases": [
            (([1, 2, 3],), [3, 1, 2]),
            ((['a', 'b', 'c'],), ['c', 'a', 'b']),
            (([5],), [5])
        ],
        "hint": "Gunakan pop() untuk ambil elemen terakhir, lalu insert(0, elem).",
        "solution": "def modify_list(lst):\n    if not lst:\n        return lst\n    last = lst.pop()\n    lst.insert(0, last)\n    return lst"
    }
]
