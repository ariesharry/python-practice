import streamlit as st
import textwrap
from streamlit_ace import st_ace
import importlib
import os
import sys

# Setup path untuk folder soal
current_dir = os.path.dirname(os.path.abspath(__file__))
soal_dir = os.path.join(current_dir, "soal")
if soal_dir not in sys.path:
    sys.path.insert(0, soal_dir)

# Import paket soal
soal_paket = {}
paket_names = []

try:
    # Cari semua file paket di folder soal
    for filename in os.listdir(soal_dir):
        if filename.startswith("paket") and filename.endswith(".py"):
            paket_num = filename.replace("paket", "").replace(".py", "")
            mod_name = f"paket{paket_num}"
            
            try:
                mod = importlib.import_module(mod_name)
                # Ambil variabel paketX (X adalah angka)
                paket_var = getattr(mod, mod_name)
                soal_paket[f"Paket {paket_num}"] = paket_var
                paket_names.append(f"Paket {paket_num}")
            except (ImportError, AttributeError) as e:
                st.warning(f"Gagal mengimpor {mod_name}: {str(e)}")
    
    # Urutkan paket berdasarkan nomor
    paket_names = sorted(paket_names, key=lambda x: int(x.split()[-1]))
    
    # Jika tidak ada paket yang ditemukan
    if not paket_names:
        raise ImportError("Tidak ada paket soal yang ditemukan di folder 'soal'")
except Exception as e:
    st.error(f"Error: {str(e)}")
    st.stop()

# Build all_questions list with added paket information
all_questions = []
for paket_name, questions in soal_paket.items():
    for q in questions:
        q_with_paket = q.copy()
        q_with_paket["paket"] = paket_name
        all_questions.append(q_with_paket)

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.user_codes = [""] * len(all_questions)
    st.session_state.answers_checked = [False] * len(all_questions)
    st.session_state.show_hint = [False] * len(all_questions)
    st.session_state.show_solution = [False] * len(all_questions)

# Group questions by paket and tipe
grouped_questions = {}
for paket in paket_names:
    grouped_questions[paket] = {}
    # Get questions for this paket
    paket_questions = [q for q in all_questions if q["paket"] == paket]
    # Group by tipe
    tipe_names = set(q["tipe"] for q in paket_questions)
    
    for tipe in tipe_names:
        grouped_questions[paket][tipe] = [
            q for q in paket_questions if q["tipe"] == tipe
        ]

# Function to run tests
import matplotlib.pyplot as plt

def run_tests(user_code, function_name, test_cases, tipe=None):
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
                
                # kalau tipe Matplotlib, jalankan dan render fig
                if tipe == "Matplotlib":
                    plt.close("all")  # bersihkan plot lama
                    output = func(*inputs)
                    fig = plt.gcf()
                    results.append((inputs, True, "Grafik ditampilkan", expected))
                    # tampilkan grafik di Streamlit
                    st.pyplot(fig)
                else:
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
# ... (kode sebelumnya tetap sama)

# Sidebar with question navigation
with st.sidebar:
    st.header("Navigasi Soal")
    
    # Package selection dropdown
    selected_paket = st.selectbox(
        "Pilih Paket Soal",
        options=paket_names,
        index=0
    )
    
    # Filter tipe soal
    tipe_options = ["All", "Basic", "Logic Control", "Looping", "Campuran"]
    selected_tipe = st.selectbox(
        "Filter Tipe Soal",
        options=tipe_options,
        index=0
    )
    
    # Dapatkan soal untuk paket yang dipilih
    if selected_paket in grouped_questions:
        # Kumpulkan semua soal dalam paket
        all_paket_questions = []
        for tipe in grouped_questions[selected_paket]:
            all_paket_questions.extend(grouped_questions[selected_paket][tipe])
        
        # Filter berdasarkan tipe yang dipilih
        if selected_tipe != "All":
            filtered_questions = [q for q in all_paket_questions if q["tipe"] == selected_tipe]
        else:
            filtered_questions = all_paket_questions
        
        # Urutkan soal berdasarkan nomor JSON
        sorted_questions = sorted(filtered_questions, key=lambda q: q["no"])
        
        # Tampilkan jumlah soal yang difilter
        st.caption(f"Menampilkan {len(sorted_questions)} soal")
        
        # Buat grid 2 kolom untuk tombol soal
        cols = st.columns(2)
        for i, q in enumerate(sorted_questions):
            # Find global index of this question
            global_idx = next(i for i, q_global in enumerate(all_questions) 
                      if q_global["no"] == q["no"] and q_global["paket"] == q["paket"])
            
            # Tentukan status tombol
            if st.session_state.answers_checked[global_idx]:
                status_icon = "✅"
            elif st.session_state.user_codes[global_idx].strip():
                status_icon = "❌"
            else:
                status_icon = ""
            
            with cols[i % 2]:
                if st.button(
                    f"{status_icon}{q['no']}",
                    key=f"nav_{q['paket']}_{q['no']}",
                    use_container_width=True,
                ):
                    st.session_state.current_question = global_idx
                    st.rerun()
    # Sidebar footer
    # CSS untuk menaruh footer sidebar di bawah
    st.markdown("""
    <style>
    [data-testid="stSidebar"]::after {
        content: "Designed by Aries";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 10px;
        text-align: center;
        background-color: #F0F2F6;
        font-size: 0.8rem;
        color: #333;
        box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)


# Display current question
if all_questions:
    q = all_questions[st.session_state.current_question]
    st.subheader(f"Soal {q['no']} - {q['tipe']} ({q['paket']})")
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
            results, error = run_tests(user_code, q['function_name'], q.get('test_cases', []), q['tipe'])

            
            if error:
                st.error(f"Error: {error}")
            else:
                st.session_state.answers_checked[st.session_state.current_question] = True
                all_passed = all(passed for _, passed, _, _ in results)
                
                if all_passed:
                    st.success("✅ Semua test case berhasil!")
                    for i, (inputs, passed, output, expected) in enumerate(results):
                        status = "✅" if passed else "❌"
                        st.write(f"**Test case {i+1} {status}:** `{q['function_name']}{inputs}`")
                        st.code(f"Output Anda: {output}\nDiharapkan: {expected}")
                        st.divider()
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
else:
    st.warning("Tidak ada soal yang tersedia. Silakan tambahkan paket soal di folder 'soal'.")