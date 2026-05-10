print ('hello world')
import tkinter as tk

# 1. Khởi tạo cửa sổ gốc
root = tk.Tk()
root.title("Ứng dụng đầu tiên - UHL")
root.geometry("500x500")

# 2. Tạo thành phần hiển thị văn bản (Label)
nhan_chao = tk.Label(root, text="Chào mừng Đinh Quang Nghĩa!")
nhan_chao.pack(pady=50) # Đưa nhãn vào cửa sổ và tạo khoảng cách lề

# 3. Duy trì cửa sổ (Vòng lặp chính)
root.mainloop()

import tkinter as tk
root = tk.Tk()
root.title("Thẻ Sinh Viên Số")
root.geometry("400x300")



