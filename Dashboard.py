import streamlit as st
import textwrap
from streamlit_ace import st_ace

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.user_codes = [""] * 30
    st.session_state.answers_checked = [False] * 30
    st.session_state.show_hint = [False] * 30
    st.session_state.show_solution = [False] * 30

# Question database
questions = [
    {
        "no": 1,
        "question": "Buat fungsi bernama 'tambah' yang menerima dua angka dan mengembalikan hasil penjumlahannya.",
        "function_name": "tambah",
        "test_cases": [((1, 2), 3), ((0, 0), 0), ((-1, 5), 4)],
        "hint": "Gunakan operator +",
        "solution": "def tambah(a, b):\n    return a + b"
    },
    {
        "no": 2,
        "question": "Buat fungsi bernama 'kali' yang menerima dua angka dan mengembalikan hasil perkaliannya.",
        "function_name": "kali",
        "test_cases": [((3, 4), 12), ((0, 5), 0), ((-2, 3), -6)],
        "hint": "Gunakan operator *",
        "solution": "def kali(a, b):\n    return a * b"
    },
    {
        "no": 3,
        "question": "Buat fungsi bernama 'sapa' yang menerima nama (string) dan mengembalikan 'Halo, [nama]!'.",
        "function_name": "sapa",
        "test_cases": [("Aries", "Halo, Aries!"), ("Budi", "Halo, Budi!"), ("", "Halo, !")],
        "hint": "Gunakan f-string atau concatenation",
        "solution": "def sapa(nama):\n    return f'Halo, {nama}!'"
    },
    {
        "no": 4,
        "question": "Buat fungsi bernama 'ganjil_genap' yang menerima angka dan mengembalikan 'ganjil' atau 'genap'.",
        "function_name": "ganjil_genap",
        "test_cases": [(1, 'ganjil'), (2, 'genap'), (0, 'genap')],
        "hint": "Gunakan modulus % 2",
        "solution": "def ganjil_genap(angka):\n    return 'genap' if angka % 2 == 0 else 'ganjil'"
    },
    {
        "no": 5,
        "question": "Buat fungsi bernama 'panjang_string' yang menerima string dan mengembalikan panjangnya.",
        "function_name": "panjang_string",
        "test_cases": [("Hello", 5), ("", 0), ("Python", 6)],
        "hint": "Gunakan fungsi len()",
        "solution": "def panjang_string(s):\n    return len(s)"
    },
    {
        "no": 6,
        "question": "Buat fungsi bernama 'faktorial' yang menghitung faktorial dari sebuah bilangan bulat non-negatif.",
        "function_name": "faktorial",
        "test_cases": [(0, 1), (1, 1), (5, 120)],
        "hint": "Gunakan rekursi atau loop",
        "solution": "def faktorial(n):\n    if n == 0:\n        return 1\n    return n * faktorial(n-1)"
    },
    {
        "no": 7,
        "question": "Buat fungsi bernama 'reverse_string' yang membalikkan sebuah string.",
        "function_name": "reverse_string",
        "test_cases": [("hello", "olleh"), ("Python", "nohtyP"), ("", "")],
        "hint": "Gunakan slicing [::-1]",
        "solution": "def reverse_string(s):\n    return s[::-1]"
    },
    {
        "no": 8,
        "question": "Buat fungsi bernama 'maksimum' yang menerima tiga angka dan mengembalikan angka terbesar.",
        "function_name": "maksimum",
        "test_cases": [((1, 2, 3), 3), ((9, 5, 7), 9), ((-1, -5, -3), -1)],
        "hint": "Gunakan fungsi max() atau if-else",
        "solution": "def maksimum(a, b, c):\n    return max(a, b, c)"
    },
    {
        "no": 9,
        "question": "Buat fungsi bernama 'adalah_vokal' yang menerima satu huruf dan mengembalikan True jika huruf tersebut vokal.",
        "function_name": "adalah_vokal",
        "test_cases": [("a", True), ("b", False), ("U", True)],
        "hint": "Gunakan operator in dan string 'aeiouAEIOU'",
        "solution": "def adalah_vokal(huruf):\n    return huruf in 'aeiouAEIOU'"
    },
    {
        "no": 10,
        "question": "Buat fungsi bernama 'kuadrat_list' yang menerima list angka dan mengembalikan list kuadrat dari angka-angka tersebut.",
        "function_name": "kuadrat_list",
        "test_cases": [([1, 2, 3], [1, 4, 9]), ([], []), ([0, -2], [0, 4])],
        "hint": "Gunakan list comprehension atau loop",
        "solution": "def kuadrat_list(lst):\n    return [x**2 for x in lst]"
    },
    {
        "no": 11,
        "question": "Buat fungsi bernama 'is_positive' yang menerima satu angka dan mengembalikan True jika positif.",
        "function_name": "is_positive",
        "test_cases": [(5, True), (0, False), (-3, False)],
        "hint": "Gunakan operator >",
        "solution": "def is_positive(n):\n    return n > 0"
    },
    {
        "no": 12,
        "question": "Buat fungsi bernama 'pangkat' yang menerima dua angka (basis dan eksponen) dan mengembalikan hasil perpangkatannya.",
        "function_name": "pangkat",
        "test_cases": [((2, 3), 8), ((5, 0), 1), ((3, 1), 3)],
        "hint": "Gunakan operator **",
        "solution": "def pangkat(a, b):\n    return a ** b"
    },
    {
        "no": 13,
        "question": "Buat fungsi bernama 'jumlah_list' yang menerima list angka dan mengembalikan jumlah seluruh elemennya.",
        "function_name": "jumlah_list",
        "test_cases": [([1, 2, 3], 6), ([0], 0), ([], 0)],
        "hint": "Gunakan fungsi sum()",
        "solution": "def jumlah_list(lst):\n    return sum(lst)"
    },
    {
        "no": 14,
        "question": "Buat fungsi bernama 'is_palindrom' yang mengecek apakah string adalah palindrom (dibaca sama dari depan dan belakang).",
        "function_name": "is_palindrom",
        "test_cases": [("katak", True), ("python", False), ("", True)],
        "hint": "Bandingkan string dengan versi yang dibalik",
        "solution": "def is_palindrom(s):\n    return s == s[::-1]"
    },
    {
        "no": 15,
        "question": "Buat fungsi bernama 'konversi_menit' yang menerima total detik dan mengembalikan jumlah menit (bilangan bulat).",
        "function_name": "konversi_menit",
        "test_cases": [(60, 1), (125, 2), (59, 0)],
        "hint": "Gunakan pembagian bulat //",
        "solution": "def konversi_menit(detik):\n    return detik // 60"
    },
    {
        "no": 16,
        "question": "Buat fungsi bernama 'hitung_diskon' yang menerima harga dan persen diskon, lalu mengembalikan harga setelah diskon.",
        "function_name": "hitung_diskon",
        "test_cases": [((100000, 10), 90000), ((50000, 20), 40000), ((75000, 0), 75000)],
        "hint": "Diskon = harga * persen / 100",
        "solution": "def hitung_diskon(harga, diskon):\n    return int(harga - (harga * diskon / 100))"
    },
    {
        "no": 17,
        "question": "Buat fungsi bernama 'huruf_besar' yang mengubah string menjadi huruf kapital semua.",
        "function_name": "huruf_besar",
        "test_cases": [("halo", "HALO"), ("Python", "PYTHON"), ("", "")],
        "hint": "Gunakan method .upper()",
        "solution": "def huruf_besar(teks):\n    return teks.upper()"
    },
    {
        "no": 18,
        "question": "Buat fungsi bernama 'nilai_tertinggi' yang menerima list nilai dan mengembalikan nilai terbesar.",
        "function_name": "nilai_tertinggi",
        "test_cases": [([80, 90, 100], 100), ([50], 50), ([0, -1, -5], 0)],
        "hint": "Gunakan fungsi max()",
        "solution": "def nilai_tertinggi(nilai):\n    return max(nilai)"
    },
    {
        "no": 19,
        "question": "Buat fungsi bernama 'bilangan_prima' yang mengecek apakah sebuah angka adalah bilangan prima.",
        "function_name": "bilangan_prima",
        "test_cases": [(2, True), (4, False), (7, True)],
        "hint": "Periksa pembagi dari 2 sampai akar n",
        "solution": (
            "def bilangan_prima(n):\n"
            "    if n < 2:\n"
            "        return False\n"
            "    for i in range(2, int(n**0.5)+1):\n"
            "        if n % i == 0:\n"
            "            return False\n"
            "    return True"
        )
    },
    {
        "no": 20,
        "question": "Buat fungsi bernama 'jumlah_digit' yang menghitung jumlah semua digit dalam sebuah angka positif.",
        "function_name": "jumlah_digit",
        "test_cases": [(123, 6), (0, 0), (4567, 22)],
        "hint": "Ubah angka ke string, lalu iterasi tiap digit",
        "solution": "def jumlah_digit(n):\n    return sum(int(d) for d in str(n))"
    }
]

# Function to run tests
def run_tests(user_code, function_name, test_cases):
    try:
        exec(user_code, globals())
        func = globals().get(function_name)
        
        if not func:
            return None, "Function not defined"
        
        results = []
        for inputs, expected in test_cases:
            try:
                if not isinstance(inputs, tuple):
                    inputs = (inputs,)
                output = func(*inputs)
                results.append((inputs, output == expected, output, expected))
            except Exception as e:
                results.append((inputs, False, str(e), expected))
        return results, None
    except Exception as e:
        return None, str(e)

# UI Components
st.title("Python Function Practice")
st.caption(f"🧩 Beginner Python Function Challenges")

# Sidebar with question navigation
with st.sidebar:
    st.header("Soal")
    
    # Display question buttons in 2 columns
    col1, col2 = st.columns(2)
    
    for i in range(len(questions)):
        status = "✅" if st.session_state.answers_checked[i] else "❌" if st.session_state.user_codes[i] else str(i+1)
        
        if i % 2 == 0:
            if col1.button(f"{status}", key=f"q_{i}", use_container_width=True):
                st.session_state.current_question = i
        else:
            if col2.button(f"{status}", key=f"q_{i}", use_container_width=True):
                st.session_state.current_question = i
    
    # Sidebar footer
    st.markdown("---")
    st.caption("designed by Aries")

# Display current question
q = questions[st.session_state.current_question]
st.subheader(f"Soal {q['no']}")
st.write(q['question'])

# Enhanced code editor with syntax highlighting
st.write("**Kode Anda:**")
user_code = st_ace(
    value=st.session_state.user_codes[st.session_state.current_question],
    language="python",
    theme="chrome",
    key=f"editor_{st.session_state.current_question}",
    height=200,
    font_size=14,
    auto_update=True
)
st.session_state.user_codes[st.session_state.current_question] = user_code

# Action buttons
col1, col2, col3 = st.columns(3)

with col1:
    check_btn = st.button("🚀 Periksa Jawaban", use_container_width=True)

with col2:
    hint_btn = st.button("💡 Tampilkan Hint", use_container_width=True)

with col3:
    solution_btn = st.button("🛟 Tampilkan Solusi", use_container_width=True)

# Handle button actions
if check_btn:
    if user_code.strip() == "":
        st.warning("Silakan tulis kode Anda terlebih dahulu!")
    else:
        results, error = run_tests(user_code, q['function_name'], q.get('test_cases', q.get('test_cases', [])))
        
        if error:
            st.error(f"Error: {error}")
        else:
            st.session_state.answers_checked[st.session_state.current_question] = True
            all_passed = all(passed for _, passed, _, _ in results)
            
            if all_passed:
                st.success("✅ Semua test case berhasil!")
            else:
                st.error("❌ Beberapa test case gagal:")
            
            for i, (inputs, passed, output, expected) in enumerate(results):
                status = "✅" if passed else "❌"
                st.write(f"**Test case {i+1} {status}:** `{q['function_name']}{inputs}`")
                st.code(f"Output Anda: {output}\nDiharapkan: {expected}")
                st.divider()

if hint_btn:
    st.session_state.show_hint[st.session_state.current_question] = True

if solution_btn:
    st.session_state.show_solution[st.session_state.current_question] = True

# Display hint
if st.session_state.show_hint[st.session_state.current_question]:
    st.info(f"**Hint:** {q['hint']}")

# Display solution
if st.session_state.show_solution[st.session_state.current_question]:
    st.warning("**Solusi:**")
    st.code(textwrap.dedent(q['solution']))