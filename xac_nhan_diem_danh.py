import tkinter as tk
from tkinter import messagebox
def xu_ly_du_lieu():
    # 1. Lấy dữ liệu
    mssv = o_nhap_ma_sv.get()
    ho_ten = o_nhap_ho_ten.get()
    
    # 2. Kiểm tra bỏ trống
    if ho_ten == "" or mssv == "":
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng không để trống thông tin!")
        return  # Dừng hàm tại đây, không chạy các lệnh bên dưới nữa

    # 3. Kiểm tra định dạng số cho MSSV
    if not mssv.isdigit():
        messagebox.showerror("Lỗi định dạng", "Mã sinh viên phải là chữ số!")
        o_nhap_ma_sv.delete(0, tk.END) # Xóa mã sai
        return  # Dừng hàm nếu MSSV sai

    # 4. Nếu vượt qua các bước kiểm tra trên thì mới chạy xuống đây (Thành công)
    nhan_ket_qua.config(text=f"Chào sinh viên: {ho_ten} ({mssv})", fg="blue")
    
    # Xóa sạch ô nhập để đón người tiếp theo
    o_nhap_ma_sv.delete(0, tk.END)
    o_nhap_ho_ten.delete(0, tk.END)
    o_nhap_ma_sv.focus_set()

root = tk.Tk()
root.title("Quản lý Sinh viên - UHL")
root.geometry("400x350")
root.columnconfigure(1, weight=1)

# --- PHẦN GIAO DIỆN (Giữ nguyên từ Lộ trình 3) ---
tk.Label(root, text="Mã sinh viên:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
o_nhap_ma_sv = tk.Entry(root)
o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Họ và tên:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
o_nhap_ho_ten = tk.Entry(root)
o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# --- PHẦN MỚI: NÚT BẤM VÀ KẾT QUẢ ---

# Nút bấm có tham số 'command' kết nối tới hàm xử lý
nut_xac_nhan = tk.Button(root, text="Xác nhận điểm danh", command=xu_ly_du_lieu)
nut_xac_nhan.grid(row=2, column=0, columnspan=2, pady=10)

# Nhãn hiển thị kết quả ngay trên giao diện
nhan_ket_qua = tk.Label(root, text="Chưa có dữ liệu", font=("Arial", 10, "italic"))
nhan_ket_qua.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()