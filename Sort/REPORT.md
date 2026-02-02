# BÁO CÁO KẾT QUẢ THỬ NGHIỆM
### Sinh viên thực hiện: Lê Nhựt Trí
### MSSV: 25521904
### Lớp: IT003.Q21.CTTN

#### I.	Kết quả thử nghiệm
   1.	Bảng dữ liệu thời gian thực thi
<div align="center">

## Kết quả đo thời gian thực thi (ms)

| Bộ dữ liệu | Quicksort | Heapsort | Mergesort | PythonSort |
|--------:|----------:|---------:|----------:|-------------:|
| data1.txt  | 714.741  | 3506.804 | 1526.683 | 20.936 |
| data2.txt  | 789.278 | 3344.884 | 1528.829 | 24.232 |
| data3.txt  | 1957.229 | 5559.011 | 2875.602 | 207.181 |
| data4.txt  | 1820.744 | 5328.556 | 2998.063 | 205.432 |
| data5.txt  | 1669.468 | 5344.947| 3022.605 | 205.032 |
| data6.txt  | 1686.286 | 5009.834 | 2736.928 | 192.757 |
| data7.txt  | 1663.872 | 5507.634 | 2929.859 | 200.224 |
| data8.txt  | 1670.214 | 5204.637| 2891.858 | 201.384 |
| data9.txt | 1667.323 | 5829.832 | 3433.504 | 237.791 |
| data10.txt  | 1652.647  | 4811.547 | 2677.248 | 186.379 |
</div>

2. Biểu đồ thời gian thực thi
   <img width="1281" height="462" alt="image" src="https://github.com/user-attachments/assets/a7a20665-d638-4cef-8789-ceff7b39fed1" />

#### II.	Kết luận:
Theo kết quả thử nghiệm có thể thấy:
-	PythonSort luôn cho thời gian thực thi nhanh nhất trên tất cả các bộ dữ liệu (chỉ từ khoảng 20–240 ms), vượt trội so với ba thuật toán còn lại. Điều này cho thấy thuật toán sắp xếp có sẵn trong Python được tối ưu rất tốt.
-	Trong ba thuật toán tự cài đặt, QuickSort có hiệu năng tốt nhất, với thời gian trung bình khoảng 700–1900 ms. MergeSort đứng thứ hai, chậm hơn QuickSort nhưng ổn định hơn HeapSort. HeapSort là thuật toán chậm nhất, với thời gian thường trên 3000–5500 ms.
-	Nhìn chung, thứ tự hiệu năng từ nhanh đến chậm là: **PythonSort → QuickSort → MergeSort → HeapSort**.

