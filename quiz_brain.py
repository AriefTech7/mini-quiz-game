class Brain:
    def __init__(self, questions_list):
        # Constructor kelas Brain
        self.question_number = 0  # Menyimpan nomor pertanyaan saat ini (dimulai dari 0)
        self.score = 0  # Menyimpan skor pemain (dimulai dari 0)
        self.question_list = questions_list  # Menyimpan daftar pertanyaan

    def still_has_question(self):
        # Memeriksa apakah masih ada pertanyaan yang tersisa
        # Mengembalikan True jika nomor pertanyaan kurang dari jumlah total pertanyaan
        return self.question_number < len(self.question_list)
        
    # Metode alternatif untuk menangani pertanyaan (dikomentari):
    # def still_has_question2(self):
    #     on = True
    #     if not self.question_list:
    #         on = False
    #     else:
    #         while on:
    #             self.question_number += 1
    #             try:
    #                 current_question = self.question_list[self.question_number]
    #             except:
    #                 print("the question is finished")
    #                 break
    #             next_question = input(f"Q.{self.question_number}:{current_question.text} (True/False) ").capitalize()

    def nextquestion(self):
        # Menampilkan pertanyaan berikutnya kepada pengguna
        current_question = self.question_list[self.question_number]  # Mendapatkan pertanyaan saat ini
        self.question_number += 1  # Menambah nomor pertanyaan
        # Meminta input jawaban dari pengguna dan mengkapitalisasi huruf pertama
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False): ").capitalize()
        self.check_answer(user_answer, current_question.answer)  # Memeriksa jawaban

    def check_answer(self, user_answer, correct_answer):
        # Memeriksa apakah jawaban pengguna benar
        # Membandingkan jawaban pengguna dengan jawaban benar (case insensitive)
        if user_answer.lower() == correct_answer.lower():
            print("You got it answer")  # Pesan jika jawaban benar
            self.score += 1  # Menambah skor
        else:       
            print("you wrong")  # Pesan jika jawaban salah
        # Menampilkan jawaban yang benar
        print(f"The correct answer was: {correct_answer}")
        # Menampilkan skor saat ini
        print(f"Your current score: {self.score}/{self.question_number}\n")