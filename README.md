# se06-13.1
## Tên đề tài : Nhận dạng khuôn mặt và xử lý thành cartoon, áp các filter như tiktok. (Đề tài mới do anh Hào hướng dẫn)

### Mục lục
[1. Mục tiêu](#1)

[2. Kiến trúc tổng thể của dự án](#2)

[3. Yêu cầu về môi trường để sử dụng project](#3)

[4. Cách cài đặt môi trường và thư viện](#4)
- [Các lệnh cài đặt môi trường](#4.1)

  - [Python](#4.1.1)
  - [Môi trường ảo](#4.1.2)
- [Các thư viện cần cài đặt](#4.2)

[5. Cách sử dụng project](#5)

[6. Cách để test chức năng mà không cần cài đặt](#6)

[7. Thành viên nhóm](#7)

===========================

<p align="center">
  <img src="https://user-images.githubusercontent.com/58498756/150540972-2f89575d-43c4-4cff-83ce-734ac8075bea.gif" alt="animated" />
</p>

<a name="1"></a>
### 1. Mục tiêu  
* Mục tiêu chính: Biến ảnh chụp người thành dạng như hoạt hình - [link web mẫu](https://huggingface.co/spaces/akhaliq/AnimeGANv2)
* Biết sử dụng `Flask` làm web server
* Làm quen với `Machine Learning`
<a name="2"></a>
### 2. Kiến trúc tổng thể của dự án
![flowchart](https://user-images.githubusercontent.com/58498756/149651768-e0a36e45-1f80-400a-8ada-056687d46218.png)

Ảnh từ user sẽ được truyền vào web server -> ML Server để xử lý hình ảnh. Ảnh sau xử lý  sẽ được gửi về user
<a name="3"></a>
### 3. Yêu cầu về môi trường để sử dụng project
* `Ubuntu (20.04)`
* `Python 3.6`
* `Tensorflow-gpu 1.15`
* `torch >= 1.7.1`
<a name="4"></a>
### 4. Cách cài đặt môi trường và thư viện
<a name="4.1"></a>
* Các lệnh cài môi trường
<a name="4.1.1"></a>
  - python 3.6 : 
    - sudo add-apt-repository ppa:deadsnakes/ppa
    - sudo apt-get update
    - sudo apt-get install python3.6
<a name="4.1.2"></a>
  - Môi trường ảo : 
    -  sudo apt-get update
    -  sudo apt install build-essential
    -  sudo apt-get install python3-virtualenv
    - virtualenv -p /usr/bin/python3.6 venv
  - Kích hoạt môi trường ảo : source venv/bin/activate
<a name="4.2"></a>
* Các thư viện cần cài đặt
  - pip install tensorflow-gpu==1.15
  - pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
  - pip install cmake
  - pip install dlib -vvv
  - pip install matplotlib
  - pip install scipy
  - pip install requests
<a name="5"></a>
### 5. Cách sử dụng project
* Clone git
    ```
   git clone https://github.com/tangtheduy/se06-13.1.git
   ```
* Kích hoạt môi trường sau khi đã cài đặt các thư viện ở trên
  ```
   source venv/bin/activate
   ```
* Chạy Flask trong folder project
  ```
   export FLASK_APP=demo.py
   ```
   ```
   flask run
   ```
<a name="6"></a>
### 6. Cách để test chức năng mà không cần cài đặt
Có thể truy cập qua link
   ```
  http://20.119.45.196/
  ``` 
<a name="7"></a>
### 7. Thành viên nhóm
* Lê Minh Dũng : Trưởng nhóm
* Bùi Việt Anh
* Tăng Thế Duy
* Trần Khánh Duy
