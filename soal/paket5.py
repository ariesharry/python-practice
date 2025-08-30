paket5 = [
    {
        "no": 1,
        "tipe": "NumPy",
        "question": "Buat fungsi bernama `create_array` yang menerima dua parameter: `start` dan `end`. Fungsi harus mengembalikan list Python berisi angka dari start sampai end (inklusif).",
        "function_name": "create_array",
        "test_cases": [
            ((1, 5), [1, 2, 3, 4, 5]),
            ((0, 3), [0, 1, 2, 3]),
            ((5, 5), [5])
        ],
        "hint": "Gunakan numpy.arange(start, end+1). Jangan lupa convert ke **LIST** dengan .tolist().",
        "solution": "import numpy as np\ndef create_array(start, end):\n    return np.arange(start, end+1).tolist()"
    },
    {
        "no": 2,
        "tipe": "NumPy",
        "question": "Buat fungsi bernama `reshape_matrix` yang menerima sebuah list dengan 6 angka. Fungsi harus mengembalikan **LIST** 2D berbentuk 2 baris × 3 kolom.",
        "function_name": "reshape_matrix",
        "test_cases": [
            (([1, 2, 3, 4, 5, 6],), [[1, 2, 3], [4, 5, 6]])
        ],
        "hint": "Gunakan numpy.array lalu reshape(2,3), kemudian convert ke list dengan .tolist().",
        "solution": "import numpy as np\ndef reshape_matrix(data):\n    return np.array(data).reshape(2,3).tolist()"
    },
    {
        "no": 3,
        "tipe": "NumPy",
        "question": "Buat fungsi bernama `matrix_multiply` yang menerima dua list 2D, lalu mengembalikan hasil perkalian matriks dalam bentuk list 2D.",
        "function_name": "matrix_multiply",
        "test_cases": [
            (([[1,2],[3,4]], [[5,6],[7,8]]), [[19,22],[43,50]])
        ],
        "hint": "Gunakan numpy.dot atau operator @, lalu convert hasil ke list dengan .tolist().",
        "solution": "import numpy as np\ndef matrix_multiply(a, b):\n    return (np.dot(np.array(a), np.array(b))).tolist()"
    },
    {
        "no": 4,
        "tipe": "Matplotlib",
        "question": "Buat fungsi bernama `plot_simple` yang membuat grafik garis dari x = [1,2,3,4] dan y = [1,4,9,16]. Fungsi tidak mengembalikan apa-apa, hanya menampilkan grafik.",
        "function_name": "plot_simple",
        "test_cases": [
            ((), None)
        ],
        "hint": "Gunakan matplotlib.pyplot sebagai plt, lalu plt.plot(x,y), plt.show().",
        "solution": "import matplotlib.pyplot as plt\ndef plot_simple():\n    x = [1,2,3,4]\n    y = [1,4,9,16]\n    plt.plot(x,y)\n    plt.show()"
    },
    {
        "no": 5,
        "tipe": "Matplotlib",
        "question": "Buat fungsi bernama `plot_bar_chart` yang menerima sebuah dictionary (key = kategori, value = angka). Fungsi harus menampilkan grafik batang berdasarkan data tersebut.",
        "function_name": "plot_bar_chart",
        "test_cases": [
            (({'A': 3, 'B': 7, 'C': 5},), None)
        ],
        "hint": "Gunakan plt.bar(list(data.keys()), list(data.values())).",
        "solution": "import matplotlib.pyplot as plt\ndef plot_bar_chart(data):\n    plt.bar(list(data.keys()), list(data.values()))\n    plt.show()"
    }
]
