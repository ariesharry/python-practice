paket2 = [
    {
    "no": 1,
    "tipe": "Basic",
    "question": "Buatlah fungsi bernama `create_greeting` yang menerima tiga parameter: `event_type` (jenis acara), `event_id` (kode acara), dan `person_name` (nama peserta). Fungsi ini harus mengembalikan kalimat sambutan seperti: 'Welcome to the [event_type] ([event_id]), [person_name]!'",
    "function_name": "create_greeting",
    "test_cases": [
        (("International Conference", "IntConf2024", "Alice"), "Welcome to the International Conference (IntConf2024), Alice!"),
        (("Local Workshop", "WorkshopA1", "Bob"), "Welcome to the Local Workshop (WorkshopA1), Bob!"),
        (("Virtual Webinar", "W2024", "Charlie"), "Welcome to the Virtual Webinar (W2024), Charlie!")
    ],
    "hint": "Gunakan parameter string dan f-string atau string formatting untuk menyusun kalimat sambutan berdasarkan input pengguna. Pastikan tanda kurung dan tanda baca sesuai dengan contoh.",
    "solution": "def create_greeting(event_type, event_id, person_name):\n    return f\"Welcome to the {event_type} ({event_id}), {person_name}!\""
    },
    {
    "no": 2,
    "tipe": "Logic Control",
    "question": "Buatlah fungsi bernama `factor_check` yang menerima dua parameter: `n` dan `k`. Fungsi ini harus mengecek apakah `k` adalah faktor dari `n`. Jika ya, kembalikan string 'This is a factor.' dan jika tidak, kembalikan 'This is not a factor.'",
    "function_name": "factor_check",
    "test_cases": [
        ((28, 7), "This is a factor."),
        ((29, 7), "This is not a factor."),
        ((15, 5), "This is a factor."),
        ((20, 3), "This is not a factor."),
        ((100, 10), "This is a factor.")
    ],
    "hint": "Gunakan operator modulus (%) untuk mengecek apakah sisa pembagian n dengan k adalah nol. Jika ya, maka k adalah faktor dari n.",
    "solution": "def factor_check(n, k):\n    if n % k == 0:\n        return \"This is a factor.\"\n    else:\n        return \"This is not a factor.\""
    },
    {
    "no": 3,
    "tipe": "Campuran",
    "question": "Buatlah fungsi bernama `count_evens` yang menerima satu parameter berupa list `nums` yang berisi angka-angka bulat. Fungsi harus menghitung dan mengembalikan jumlah bilangan genap di dalam list tersebut.",
    "function_name": "count_evens",
    "test_cases": [
        (([1, 2, 3, 4, 5],), 2),
        (([2, 4, 6, 8, 10],), 5),
        (([],), 0),
        (([1, 3, 5, 7],), 0),
        (([0, 1, 2, 3, 4],), 3)
    ],
    "hint": "Gunakan perulangan (for loop) untuk mengecek setiap elemen dalam list. Jika elemen tersebut genap (mod 2 == 0), tambahkan ke penghitung.",
    "solution": "def count_evens(nums):\n    count = 0\n    for num in nums:\n        if num % 2 == 0:\n            count += 1\n    return count"
    },
    {
    "no": 4,
    "tipe": "Logic Control",
    "question": "Buatlah fungsi bernama `classify_number` yang menerima satu bilangan bulat `n` sebagai input, dan mengembalikan string yang menunjukkan apakah bilangan tersebut 'Positive', 'Negative', atau 'Zero'. Gunakan pernyataan if, elif, dan else untuk mengklasifikasikan bilangan.",
    "function_name": "classify_number",
    "test_cases": [
        ((3,), "Positive"),
        ((-15,), "Negative"),
        ((0,), "Zero"),
        ((-5,), "Negative"),
        ((27,), "Positive")
    ],
    "hint": "Gunakan struktur if-elif-else untuk memeriksa apakah bilangan lebih besar dari nol, kurang dari nol, atau sama dengan nol, dan kembalikan string yang sesuai.",
    "solution": "def classify_number(n):\n    if n > 0:\n        return \"Positive\"\n    elif n < 0:\n        return \"Negative\"\n    else:\n        return \"Zero\""
    },
    {
    "no": 5,
    "tipe": "Basic",
    "question": "Buatlah fungsi bernama `calculate_circle_area` yang menerima satu parameter berupa jari-jari (`radius`) dan mengembalikan luas lingkaran. Gunakan rumus: luas = π × radius². Untuk nilai π, gunakan `math.pi` dari modul math.",
    "function_name": "calculate_circle_area",
    "test_cases": [
        ((1,), 3.141592653589793),
        ((2,), 12.566370614359172),
        ((0,), 0.0),
        ((5,), 78.53981633974483),
        ((3.5,), 38.48451000647496)
    ],
    "hint": "Import modul math terlebih dahulu (`import math`) dan gunakan `math.pi` untuk menghitung nilai π. Gunakan operasi pemangkatan atau operator `**` untuk menghitung kuadrat radius.",
    "solution": "import math\n\ndef calculate_circle_area(radius):\n    return math.pi * (radius ** 2)"
    },
    {
    "no": 6,
    "tipe": "Looping",
    "question": "Buatlah fungsi bernama `sum_products` yang menerima dua buah list `nums1` dan `nums2` berisi bilangan float non-negatif dengan panjang yang sama. Fungsi harus mengembalikan jumlah dari hasil perkalian elemen-elemen yang bersesuaian dari kedua list tersebut.",
    "function_name": "sum_products",
    "test_cases": [
        (([1.5, 10.0], [10.0, 2.0]), 35.0),
        (([2.0, 4.0], [3.0, 5.0]), 26.0),
        (([0.0, 7.0], [8.0, 1.0]), 7.0),
        (([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]), 32.0),
        (([1.0], [1.0]), 1.0)
    ],
    "hint": "Gunakan perulangan (loop) untuk mengakses elemen-elemen yang sesuai dari kedua list. Kalikan elemen pada indeks yang sama dan jumlahkan hasilnya.",
    "solution": "def sum_products(nums1, nums2):\n    total = 0\n    for i in range(len(nums1)):\n        total += nums1[i] * nums2[i]\n    return total"
    },
    {
    "no": 7,
    "tipe": "Logic Control",
    "question": "Buatlah fungsi bernama `divisible_by_n` yang menerima dua parameter bilangan bulat positif: `num` dan `n`. Fungsi harus mengembalikan nilai boolean `True` jika `num` habis dibagi `n`, dan `False` jika tidak. Gunakan operator modulus (`%`) untuk menentukan sisa pembagian.",
    "function_name": "divisible_by_n",
    "test_cases": [
        ((10, 2), True),
        ((10, 3), False),
        ((15, 5), True),
        ((17, 4), False),
        ((100, 10), True)
    ],
    "hint": "Gunakan ekspresi `num % n == 0` untuk mengecek apakah `num` habis dibagi `n`. Jika iya, kembalikan `True`, jika tidak, kembalikan `False`.",
    "solution": "def divisible_by_n(num, n):\n    return num % n == 0"
    },
    {
    "no": 8,
    "tipe": "Looping",
    "question": "Buatlah fungsi bernama `double_char` yang menerima sebuah string `s`, dan mengembalikan string baru di mana setiap karakter dalam string `s` muncul dua kali secara berurutan.",
    "function_name": "double_char",
    "test_cases": [
        (("a",), "aa"),
        (("1234",), "11223344"),
        (("abc",), "aabbcc"),
        (("",), ""),
        (("Hi!",), "HHii!!")
    ],
    "hint": "Gunakan perulangan untuk membaca setiap karakter dalam string, lalu tambahkan dua kali karakter tersebut ke string hasil. Bisa juga menggunakan list comprehension atau string join.",
    "solution": "def double_char(s):\n    result = ''\n    for char in s:\n        result += char * 2\n    return result"
    },
    {
    "no": 9,
    "tipe": "Campuran",
    "question": "Buatlah fungsi bernama `longest_string` yang menerima sebuah list non-kosong `str_list` berisi string. Fungsi harus mengembalikan string yang paling panjang dari list tersebut. Jika terdapat beberapa string dengan panjang maksimum yang sama, kembalikan yang muncul lebih dahulu.",
    "function_name": "longest_string",
    "test_cases": [
        ((["hello", "world", "this", "is", "a", "test"],), "hello"),
        ((["single"],), "single"),
        ((["123", "abc", "xyz", "456"]), "123"),
        ((["", "a", "ab", "abc", "abcd"]), "abcd"),
        ((["long", "longer", "longest", "tiny"]), "longest")
    ],
    "hint": "Gunakan perulangan untuk membandingkan panjang setiap string. Simpan string terpanjang yang ditemukan sejauh ini dan perbarui jika ditemukan yang lebih panjang.",
    "solution": "def longest_string(str_list):\n    longest = str_list[0]\n    for s in str_list:\n        if len(s) > len(longest):\n            longest = s\n    return longest"
    },
    {
    "no": 10,
    "tipe": "Looping",
    "question": "Buatlah fungsi bernama `my_product` yang menerima sebuah list berisi data numerik (`int` atau `float`) dan mengembalikan hasil perkalian dari seluruh elemen dalam list tersebut. Jika list kosong, kembalikan 1.",
    "function_name": "my_product",
    "test_cases": [
        (([2, 3, 4],), 24),
        (([1.5, 2, 3],), 9.0),
        (([-2, 3, 4],), -24),
        (([],), 1),
        (([5],), 5)
    ],
    "hint": "Gunakan perulangan untuk mengalikan setiap elemen dalam list. Inisialisasi nilai hasil dengan 1, lalu kalikan dengan setiap angka di dalam list.",
    "solution": "def my_product(numbers):\n    result = 1\n    for num in numbers:\n        result *= num\n    return result"
    },
    {
    "no": 11,
    "tipe": "Looping",
    "question": "Buatlah fungsi `get_print_percentage()` yang meminta pengguna untuk memasukkan dua bilangan bulat positif: total dan bagian. Fungsi akan menghitung persentase bagian dari total dan mencetak hasilnya dengan dua angka di belakang koma dalam format berikut: `Percentage: x.xx%`. Pastikan bahwa input total tidak boleh nol. Jika nol, minta ulang input dari pengguna dengan pesan: `Total cannot be zero, please enter a non-zero total: `. Input bagian boleh nol. Contoh tampilan: \n\nTotal? 50\nPart? 25\nPercentage: 50.00%",
    "function_name": "get_print_percentage",
    "test_cases": [
        (("50", "25"), "Percentage: 50.00%"),
        (("100", "0"), "Percentage: 0.00%"),
        (("0", "10", "50", "25"), "Percentage: 50.00%") 
    ],
    "hint": "Gunakan perulangan untuk mengecek apakah input total adalah nol. Jika nol, minta input ulang sampai mendapatkan nilai total yang valid. Gunakan format string untuk menampilkan persentase hingga 2 angka di belakang koma.",
    "solution": "def get_print_percentage():\n    total = int(input(\"Total? \"))\n    while total == 0:\n        total = int(input(\"Total cannot be zero, please enter a non-zero total: \"))\n    part = int(input(\"Part? \"))\n    percentage = (part / total) * 100\n    print(f\"Percentage: {percentage:.2f}%\")"
    },
    {
    "no": 12,
    "tipe": "Looping",
    "question": "Buatlah fungsi `promote_marks_list(student_marks_list, rate)` yang menerima dua parameter: `student_marks_list` adalah daftar yang berisi daftar nilai dari 3 ujian untuk setiap siswa, dan `rate` adalah angka desimal (float) yang menunjukkan faktor pengali untuk setiap nilai. Fungsi harus mengembalikan daftar baru yang berisi nilai-nilai hasil perkalian setiap nilai dengan `rate`, dibulatkan ke 1 angka di belakang koma. Gunakan fungsi `round(nilai, 1)` untuk membulatkan hasil. Contoh: `round(71.45, 1)` akan menjadi `71.5`. ",
    "function_name": "promote_marks_list",
    "test_cases": [
        (
            ([[65, 70, 75], [80, 85, 90], [55, 60, 65]], 1.1),
            [[71.5, 77.0, 82.5], [88.0, 93.5, 99.0], [60.5, 66.0, 71.5]]
        ),
        (
            ([[50, 60, 70], [80, 90, 100]], 1),
            [[50.0, 60.0, 70.0], [80.0, 90.0, 100.0]]
        ),
        (
            ([[90, 95, 100], [75, 80, 85]], 0.9),
            [[81.0, 85.5, 90.0], [67.5, 72.0, 76.5]]
        )
    ],
    "hint": "Gunakan perulangan bersarang (nested loop) untuk mengakses setiap nilai dalam daftar siswa. Kalikan setiap nilai dengan `rate`, lalu gunakan `round(..., 1)` untuk membulatkannya ke satu angka desimal.",
    "solution": "def promote_marks_list(student_marks_list, rate):\n    result = []\n    for student in student_marks_list:\n        updated_marks = [round(mark * rate, 1) for mark in student]\n        result.append(updated_marks)\n    return result"
    },
    {
    "no": 13,
    "tipe": "Basic",
    "question": "Buatlah fungsi `inflation_adjusted(price, inflation_percent)` yang menerima dua parameter: `price` (float) dan `inflation_percent` (float). Fungsi ini harus mengembalikan harga baru setelah disesuaikan dengan inflasi, menggunakan rumus:\n\n**Adjusted Price = price × (1 + inflation_percent / 100)**\n\nHasil akhir harus berupa nilai float. Anda dapat menampilkan hasilnya menggunakan format string seperti `f\"{price:.2f}\"` untuk dua angka di belakang koma.",
    "function_name": "inflation_adjusted",
    "test_cases": [
        ((100.0, 20.0), 120.0),
        ((20.0, 5.0), 21.0),
        ((250.0, 10.0), 275.0),
        ((80.0, 0.0), 80.0),
        ((100.0, -10.0), 90.0)
    ],
    "hint": "Gunakan operator aritmatika dasar untuk menghitung persentase inflasi. Pastikan membagi `inflation_percent` dengan 100 agar nilainya dalam format desimal. Lalu kalikan dengan harga awal.",
    "solution": "def inflation_adjusted(price, inflation_percent):\n    return price * (1 + inflation_percent / 100)"
    },
    {
    "no": 14,
    "tipe": "Logic Control",
    "question": "Buatlah fungsi `love6(num1, num2)` yang menerima dua bilangan bulat `num1` dan `num2`. Fungsi harus mengembalikan `True` jika salah satu dari angka tersebut adalah 6, atau jika jumlah atau selisih (absolut) dari kedua angka tersebut adalah 6. Jika tidak memenuhi kondisi tersebut, maka fungsi harus mengembalikan `False`.\n\nContoh:\n- `love6(6, 4)` → `True` (karena salah satu angkanya adalah 6)\n- `love6(7, 1)` → `True` (karena selisih 7 - 1 = 6)\n- `love6(3, 3)` → `True` (karena jumlah 3 + 3 = 6)\n- `love6(7, 0)` → `False` (tidak memenuhi semua kondisi)",
    "function_name": "love6",
    "test_cases": [
        ((6, 4), True),
        ((7, 1), True),
        ((7, 0), False),
        ((3, 3), True),
        ((0, 6), True)
    ],
    "hint": "Gunakan operator logika `or` untuk menggabungkan kondisi: apakah salah satu angka bernilai 6, apakah jumlahnya 6, atau apakah selisih absolutnya 6 (gunakan `abs(num1 - num2)`).",
    "solution": "def love6(num1, num2):\n    return num1 == 6 or num2 == 6 or (num1 + num2 == 6) or (abs(num1 - num2) == 6)"
    },
    {
    "no": 15,
    "tipe": "Campuran",
    "question": "Sebuah badan lingkungan melakukan proyek untuk meningkatkan kualitas air di danau lokal. Fungsi `years_to_reach_target_quality(current_quality, annual_improvement, target_quality)` harus menghitung berapa tahun yang dibutuhkan agar kualitas air mencapai atau melebihi target yang ditentukan. Kualitas air meningkat setiap tahun sebesar `annual_improvement`.\n\nJika kualitas saat ini sudah lebih tinggi atau sama dengan target, atau jika peningkatan tahunan bernilai nol atau negatif dan target belum tercapai, maka fungsi harus langsung mengembalikan `0`.",
    "function_name": "years_to_reach_target_quality",
    "test_cases": [
        ((90, 10, 100), 1),
        ((10, 1, 20), 10),
        ((100, -2, 90), 0),
        ((50, 5, 75), 5),
        ((30, 0, 100), 0),
        ((100, 10, 100), 0)
    ],
    "hint": "Gunakan perulangan `while` untuk menambahkan peningkatan tahunan ke nilai saat ini sampai nilai tersebut mencapai atau melebihi target. Jangan lupa untuk mengecek apakah kondisi awal sudah memenuhi target atau tidak mungkin tercapai.",
    "solution": "def years_to_reach_target_quality(current_quality, annual_improvement, target_quality):\n    if current_quality >= target_quality or annual_improvement <= 0:\n        return 0\n\n    years = 0\n    while current_quality < target_quality:\n        current_quality += annual_improvement\n        years += 1\n    return years"
    },
    {
    "no": 16,
    "tipe": "Campuran",
    "question": "Buatlah fungsi `count_category_occurrences(category_list, category)` yang menerima dua parameter:\n1. `category_list`: list berisi nama-nama kategori (bertipe string), dan\n2. `category`: kategori yang ingin dihitung jumlah kemunculannya dalam list.\n\nFungsi harus mengembalikan jumlah kemunculan kategori tersebut dalam list **tanpa menggunakan list comprehension atau fungsi bawaan Python seperti `.count()`**.\n\nContoh:\n```python\ncount_category_occurrences([\"fruit\", \"vegetable\", \"fruit\", \"meat\"], \"fruit\") → 2\ncount_category_occurrences([\"a\", \"b\", \"c\", \"a\", \"a\"], \"a\") → 3\ncount_category_occurrences([\"apple\", \"banana\"], \"orange\") → 0\n```",
    "function_name": "count_category_occurrences",
    "test_cases": [
        ((["fruit", "vegetable", "fruit", "meat"], "fruit"), 2),
        ((["a", "b", "c", "a", "a"], "a"), 3),
        ((["apple", "banana"], "orange"), 0),
        (([], "any"), 0),
        ((["x", "x", "x"], "x"), 3)
    ],
    "hint": "Gunakan loop `for` untuk menelusuri setiap elemen dalam list. Tambahkan variabel penghitung yang naik setiap kali elemen sama dengan `category`.",
    "solution": "def count_category_occurrences(category_list, category):\n    count = 0\n    for item in category_list:\n        if item == category:\n            count += 1\n    return count"
    },
    {
    "no": 17,
    "tipe": "Logic Control",
    "question": "Buatlah fungsi `caught_speeding(speed, is_birthday)` yang menerima dua parameter:\n1. `speed`: sebuah bilangan bulat yang menunjukkan kecepatan mobil (dalam mph).\n2. `is_birthday`: sebuah nilai boolean yang menunjukkan apakah hari itu adalah ulang tahun pengemudi.\n\nFungsi harus mengembalikan string yang menunjukkan jenis tilang yang didapat berdasarkan aturan berikut:\n\n- Batas kecepatan normal adalah 60 mph.\n- Jika kecepatan pengemudi **60 mph atau kurang**, maka: \"You have no tickets.\"\n- Jika kecepatan **antara 61 sampai 80 mph**, maka: \"You have a small ticket.\"\n- Jika kecepatan **81 mph atau lebih**, maka: \"You have a big ticket.\"\n- **Jika hari itu adalah ulang tahun**, maka pengemudi diberikan tambahan toleransi 5 mph terhadap batasan di atas (jadi batasannya menjadi 65, 85, dst).\n\nContoh:\n```python\ncaught_speeding(60, False) → \"You have no tickets.\"\ncaught_speeding(85, False) → \"You have a big ticket.\"\ncaught_speeding(85, True) → \"You have a small ticket.\"\n```",
    "function_name": "caught_speeding",
    "test_cases": [
        ((60, False), "You have no tickets."),
        ((85, False), "You have a big ticket."),
        ((85, True), "You have a small ticket."),
        ((65, True), "You have no tickets."),
        ((81, False), "You have a big ticket."),
        ((80, True), "You have no tickets.")
    ],
    "hint": "Tambahkan toleransi 5 mph ke batas jika `is_birthday == True`. Gunakan percabangan `if`, `elif`, `else` untuk menentukan jenis tilang berdasarkan kecepatan yang sudah disesuaikan.",
    "solution": "def caught_speeding(speed, is_birthday):\n    if is_birthday:\n        speed -= 5\n\n    if speed <= 60:\n        return \"You have no tickets.\"\n    elif speed <= 80:\n        return \"You have a small ticket.\"\n    else:\n        return \"You have a big ticket.\""
    },
    {
    "no": 18,
    "tipe": "Campuran",
    "question": "Buatlah fungsi `find_first_occurrence_item(elements, target)` yang menerima dua parameter:\n1. `elements`: sebuah list berisi item-item (bisa berupa string, angka, dll), dan\n2. `target`: sebuah item yang ingin dicari dalam list.\n\nFungsi harus mencari **kemunculan pertama** dari `target` di dalam list dan **mengembalikan item yang berada tepat setelahnya**.\n\n- Jika `target` tidak ditemukan dalam list, atau berada di **posisi terakhir**, maka fungsi harus mengembalikan `None`.\n- Anda **wajib menggunakan `for` loop**, dan **tidak diperbolehkan menggunakan `while` loop**.\n\nContoh:\n```python\nfind_first_occurrence_item(['a', 'b', 'c', 'd', 'e'], 'c') → 'd'\nfind_first_occurrence_item([1, 2, 3, 4, 5], 5) → None\nfind_first_occurrence_item(['apple', 'banana', 'cherry', 'date'], 'banana') → 'cherry'\n```",
    "function_name": "find_first_occurrence_item",
    "test_cases": [
        ((['a', 'b', 'c', 'd', 'e'], 'c'), 'd'),
        (([1, 2, 3, 4, 5], 5), None),
        ((['apple', 'banana', 'cherry', 'date'], 'banana'), 'cherry'),
        ((['x', 'y', 'z'], 'a'), None),
        ((['a', 'b', 'a', 'c'], 'a'), 'b')
    ],
    "hint": "Gunakan `for` loop dan iterasi dengan indeks. Bandingkan elemen saat ini dengan `target`, dan jika cocok serta bukan elemen terakhir, kembalikan elemen berikutnya.",
    "solution": "def find_first_occurrence_item(elements, target):\n    for i in range(len(elements)):\n        if elements[i] == target:\n            if i + 1 < len(elements):\n                return elements[i + 1]\n            else:\n                return None\n    return None"
    }

]