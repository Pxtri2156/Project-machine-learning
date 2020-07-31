# Project-machine-learning
Đây là đồ án cuối kì môn Machine learning tại UIT

## Đồ án làm về phân loại  trái cây 
Mô tả: Project này đi xây dựng mô hình dự đoán trái cây:
+ Input: Hình ảnh chứa một loại trái cây ( táo, cam, chuối, khế, xoài, quýt,.....)
+ Output: Đầu ra là dự đoán trái cây trong hình 
Bài toán này sẽ phân loại 12 loại trái cây là: Cam, chuối, ổi,thanh long, dưa hấu, mận, bơ, xoài, mãng cầu, dừa,  khế, táo

PS: Hướng phát triển tiếp theo có lẽ sẽ chuyển bài toàn nhận diện nhiều trái cây cùng lúc và mở rộng thành bài toán **Detection** hay cao hơn nữa là  **Segmentation** (Hi hi)

Các yêu cầu khi train và run mô hình: 
+ python 3.7
+ numpy x....
+ ......
## Dữ liệu 
2 Nguồn chính là: 
* Downnload tại kaggle [tại đây](https://www.kaggle.com/mbkinaci/fruit-images-for-object-detection)
* Tự thu thập :  Dữ liệu của đồ án 95% là tự thu thập
Dữ liệu 2 nguồn sau được trộn lại và chia ra thành 10% cho test và 90% cho train 
## How to bulid model 
### Xử lí dữ liệu
Trích xuất ROI của các ảnh. Có thể thực hiện bằng 2 cách:
* Sử dụng tool ( trong repo có tool nhưng code còn fail nhiều nên khuyến nghị ko nên dùng)
* Tự cắt bằng tay: Đây là cách thủ công nhưng tránh được các lỗi do tool tạo ra 
### Trích xuất các đặc trưng
Hình ảnh sẽ được resize về kích thước 64*64 trước khi đưa vào trích xuất đặc trưng 
Ở đây mình sẽ dùng 2 cách:
* Cách 1: Kết hợp ba đặc trưng Shape (hu_moment), Color(histogram), Texture(haralick) , tạo thành vector đặc trưng
* Cách 2: Sử dụng đặc trưng HOG 
## How to train and run model 
## Reference

