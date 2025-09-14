# from data import question_data  # Import data pertanyaan (dikomentari karena menggunakan data2)
from question_model import Question  # Import kelas Question untuk membuat objek pertanyaan
from quiz_brain import Brain  # Import kelas Brain untuk mengelola logika kuis
from data2 import question_dataa  # Import data pertanyaan dari sumber alternatif

# Inisialisasi bank pertanyaan sebagai list kosong
question_bank = []

# Loop melalui setiap pertanyaan dalam data untuk membuat objek Question
for question in question_dataa:
    question_text = question['question']  # Mengambil teks pertanyaan
    question_answer = question['correct_answer']  # Mengambil jawaban benar
    new_question = Question(question_text, question_answer)  # Membuat objek Question baru
    question_bank.append(new_question)  # Menambahkan objek Question ke bank pertanyaan

# Kode untuk debugging (dikomentari):
# print(question_bank[1].text)
# print(question_bank) # output = <question_model.Question object at 0x000001EEE9176F90>
# print(question_bank[1].answer)

# Membuat instance Brain dengan bank pertanyaan
brain = Brain(question_bank)
# brain adalah instance/objek yang dibuat dari kelas Brain
# Instance adalah objek yang dibuat berdasarkan kelas tertentu

# Loop utama kuis: terus berjalan selama masih ada pertanyaan
while brain.still_has_question():
    brain.nextquestion()  # Menampilkan pertanyaan berikutnya

# Menampilkan pesan setelah kuis selesai
print("You've completed the quiz")
print(f"Your final score was: {brain.score}/{brain.question_number}")  # Menampilkan skor akhir
print("Thank you for playing")  # Pesan penutup