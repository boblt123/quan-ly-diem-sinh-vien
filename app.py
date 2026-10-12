
# 1. QUAN LY DIEM SINH VIEN - STREAMLIT

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 2. Tao du lieu 10 sinh vien
data = {
    "Ho_va_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Van Cuong",
        "Pham Thi Dung",
        "Hoang Van Em",
        "Vu Thi Giang",
        "Dang Van Hung",
        "Bui Thi Lan",
        "Do Van Minh",
        "Ngo Thi Ngoc"
    ],
    "Chuyen_can": [9.0, 8.0, 7.5, 9.5, 6.0, 8.5, 7.0, 10.0, 5.5, 8.0],
    "Giua_ky":    [8.0, 7.5, 6.5, 9.0, 5.0, 8.0, 6.0, 9.5, 4.5, 7.0],
    "Cuoi_ky":    [7.5, 8.0, 7.0, 9.5, 4.5, 8.5, 5.5, 9.0, 4.0, 7.5]
}

df = pd.DataFrame(data)

# 3. Tinh diem tong ket
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)

# 4. Xep loai sinh vien
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. Tieu de va bang diem
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.subheader("Bảng điểm của 10 sinh viên")

st.dataframe(
    df.rename(columns={
        "Ho_va_ten": "Họ và tên",
        "Chuyen_can": "Chuyên cần",
        "Giua_ky": "Giữa kỳ",
        "Cuoi_ky": "Cuối kỳ",
        "Tong_ket": "Tổng kết",
        "Xep_loai": "Xếp loại"
    }),
    use_container_width=True,
    hide_index=True
)

# 6. Thong ke ket qua hoc tap
diem_tb = df["Tong_ket"].mean()
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

st.subheader("Thống kê kết quả")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Điểm trung bình", f"{diem_tb:.2f}")
c2.metric("Điểm cao nhất", f"{sv_cao_nhat['Tong_ket']:.2f}")
c3.metric("Điểm thấp nhất", f"{sv_thap_nhat['Tong_ket']:.2f}")
c4.metric("Số sinh viên đạt", f"{so_sv_dat}/10")

st.write("**Sinh viên có điểm cao nhất:**", sv_cao_nhat["Ho_va_ten"])
st.write("**Sinh viên có điểm thấp nhất:**", sv_thap_nhat["Ho_va_ten"])

# 7. Chon sinh vien va xem chi tiet
st.subheader("Tra cứu thông tin sinh viên")

ten_sv = st.selectbox(
    "Chọn sinh viên:",
    df["Ho_va_ten"].tolist()
)

sv = df[df["Ho_va_ten"] == ten_sv].iloc[0]

st.write("**Họ và tên:**", sv["Ho_va_ten"])
st.write("**Điểm chuyên cần:**", sv["Chuyen_can"])
st.write("**Điểm giữa kỳ:**", sv["Giua_ky"])
st.write("**Điểm cuối kỳ:**", sv["Cuoi_ky"])
st.write("**Điểm tổng kết:**", sv["Tong_ket"])
st.write("**Xếp loại:**", sv["Xep_loai"])

# 8. Ve bieu do cot
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_va_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 9. Thong tin nguoi tao ung dung
st.divider()
st.caption("Người tạo ứng dụng: Lại Thế Bắc - MSSV: 034208015505")
