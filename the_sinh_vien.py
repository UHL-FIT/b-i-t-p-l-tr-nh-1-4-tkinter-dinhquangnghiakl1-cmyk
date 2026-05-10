import tkinter as tk
root = tk.Tk()
root.title("Thẻ Sinh Viên Số")
root.geometry("400x300")

# 1. Nhãn tiêu đề với Phông chữ và Màu sắc
nhan_truong = tk.Label(
    root, 
    text="KHOA CÔNG NGHỆ THÔNG TIN", 
    font=("Arial", 14, "bold"), 
    fg="green", 
    bg="#f8f9fa" # Màu xám thương hiệu
)
nhan_truong.pack(fill="x", pady=10) # fill="x" để màu nền trải rộng hết chiều ngang

# 2. Nhãn hiển thị họ tên
nhan_ten = tk.Label(root, text="Họ tên: Đinh Quang Nghĩa", font=("Arial", 12))
nhan_ten.pack(pady=5)
# 3. Nhãn hiển thị MSSV với màu đỏ nổi bật
nhan_msv = tk.Label(root, text="MSSV: 22010001", font=("Arial", 12), fg="red")
nhan_msv.pack(pady=5)
# 4. Tạo nút bấm để thoát chương trình
nut_thoat = tk.Button(
    root, 
    text="Đóng ứng dụng", 
    command=root.destroy, 
    bg="#dc3545", # Màu đỏ cảnh báo
    fg="white",
    width=20,
    height=5,
)
nut_thoat.pack(pady=20)

root.mainloop()


