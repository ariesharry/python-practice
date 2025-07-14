# file: latihan_representatif.py
paket3 = [
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
            ((15, 5), "This is a factor.")
        ],
        "hint": "Gunakan operator modulus (%) untuk mengecek apakah sisa pembagian n dengan k adalah nol. Jika ya, maka k adalah faktor dari n.",
        "solution": "def factor_check(n, k):\n    if n % k == 0:\n        return \"This is a factor.\"\n    else:\n        return \"This is not a factor.\""
    },
    {
        "no": 3,
        "tipe": "Looping",
        "question": "Buatlah fungsi bernama `count_evens` yang menerima satu parameter berupa list `nums` yang berisi angka-angka bulat. Fungsi harus menghitung dan mengembalikan jumlah bilangan genap di dalam list tersebut.",
        "function_name": "count_evens",
        "test_cases": [
            (([1, 2, 3, 4, 5],), 2),
            (([2, 4, 6, 8, 10],), 5),
            (([],), 0)
        ],
        "hint": "Gunakan perulangan (for loop) untuk mengecek setiap elemen dalam list. Jika elemen tersebut genap (mod 2 == 0), tambahkan ke penghitung.",
        "solution": "def count_evens(nums):\n    count = 0\n    for num in nums:\n        if num % 2 == 0:\n            count += 1\n    return count"
    },
    {
        "no": 4,
        "tipe": "Looping",
        "question": "Buatlah fungsi `promote_marks_list(student_marks_list, rate)` yang menerima dua parameter: `student_marks_list` adalah daftar yang berisi daftar nilai dari 3 ujian untuk setiap siswa, dan `rate` adalah angka desimal (float) yang menunjukkan faktor pengali untuk setiap nilai. Fungsi harus mengembalikan daftar baru yang berisi nilai-nilai hasil perkalian setiap nilai dengan `rate`, dibulatkan ke 1 angka di belakang koma.",
        "function_name": "promote_marks_list",
        "test_cases": [
            (
                ([[65, 70, 75], [80, 85, 90], [55, 60, 65]], 1.1),
                [[71.5, 77.0, 82.5], [88.0, 93.5, 99.0], [60.5, 66.0, 71.5]]
            )
        ],
        "hint": "Gunakan perulangan bersarang (nested loop) untuk mengakses setiap nilai dalam daftar siswa. Kalikan setiap nilai dengan `rate`, lalu gunakan `round(..., 1)` untuk membulatkannya ke satu angka desimal.",
        "solution": "def promote_marks_list(student_marks_list, rate):\n    result = []\n    for student in student_marks_list:\n        updated_marks = [round(mark * rate, 1) for mark in student]\n        result.append(updated_marks)\n    return result"
    },
    {
        "no": 5,
        "tipe": "Campuran",
        "question": "Fungsi `years_to_reach_target_quality(current_quality, annual_improvement, target_quality)` harus menghitung berapa tahun yang dibutuhkan agar kualitas air mencapai atau melebihi target. Jika kualitas saat ini sudah cukup atau peningkatannya nol/negatif dan belum cukup, kembalikan 0.",
        "function_name": "years_to_reach_target_quality",
        "test_cases": [
            ((90, 10, 100), 1),
            ((10, 1, 20), 10),
            ((100, -2, 90), 0)
        ],
        "hint": "Gunakan perulangan `while` untuk menambahkan peningkatan tahunan ke nilai saat ini sampai nilai tersebut mencapai atau melebihi target. Jangan lupa untuk mengecek apakah kondisi awal sudah memenuhi target atau tidak mungkin tercapai.",
        "solution": "def years_to_reach_target_quality(current_quality, annual_improvement, target_quality):\n    if current_quality >= target_quality or annual_improvement <= 0:\n        return 0\n    years = 0\n    while current_quality < target_quality:\n        current_quality += annual_improvement\n        years += 1\n    return years"
    },
    {
        "no": 6,
        "tipe": "Campuran",
        "question": "Buat fungsi `find_first_occurrence_item(elements, target)` yang menerima dua parameter:\n1. `elements`: sebuah list berisi item-item, dan\n2. `target`: sebuah item yang ingin dicari dalam list.\nFungsi harus mencari kemunculan pertama dari `target` dan mengembalikan item yang berada tepat setelahnya. Jika `target` tidak ditemukan atau di posisi terakhir, kembalikan `None`. Gunakan `for` loop.",
        "function_name": "find_first_occurrence_item",
        "test_cases": [
            ((['a', 'b', 'c', 'd', 'e'], 'c'), 'd'),
            (([1, 2, 3, 4, 5], 5), None),
            ((['apple', 'banana', 'cherry', 'date'], 'banana'), 'cherry')
        ],
        "hint": "Gunakan `for` loop dan iterasi dengan indeks. Bandingkan elemen saat ini dengan `target`, dan jika cocok serta bukan elemen terakhir, kembalikan elemen berikutnya.",
        "solution": "def find_first_occurrence_item(elements, target):\n    for i in range(len(elements)):\n        if elements[i] == target:\n            if i + 1 < len(elements):\n                return elements[i + 1]\n            else:\n                return None\n    return None"
    }
]
