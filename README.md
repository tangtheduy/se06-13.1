# se06-13.1
## Tên đề tài : Nhận dạng khuôn mặt và xử lý thành cartoon, áp các filter như tiktok. (Đề tài mới do anh Hào hướng dẫn)
### 1.Mục tiêu  
* Mục tiêu chính: Biến ảnh chụp người thành dạng như hoạt hình - [link web mẫu](https://huggingface.co/spaces/akhaliq/AnimeGANv2)
* Biết sử dụng Flask làm web server
* Làm quen với Machine Learning
### 2. Kiến trúc tổng thể của dự án
![flowchart](https://user-images.githubusercontent.com/58498756/149651768-e0a36e45-1f80-400a-8ada-056687d46218.png)

Ảnh từ user sẽ được truyền vào web server -> ML Server để xử lý hình ảnh. Ảnh sau xử lý  sẽ được gửi về user
### 3. Yêu cầu về môi trường để sử dụng project
* 
### 4. Cách cài đặt môi trường và thư viện
* Các lệnh cài môi trường
  - python 3.6 : 
    - sudo add-apt-repository ppa:deadsnakes/ppa
    - sudo apt-get update
    - sudo apt-get install python3.6
  - Môi trường ảo : 
    -  sudo apt-get update
    -  sudo apt-get install python3-virtualenv
    - virtualenv -p /usr/bin/python3.6 venv
  - Kích hoạt môi trường ảo : source venv/bin/activate
* Các thư viện cần cài đặt
  - pip install tensorflow-gpu==1.15
  - pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
  - pip install cmake
  - pip install dlib -vvv
  - pip install matplotlib
  - pip install scipy
  - pip install requests
### 5. Cách sử dụng project
* Clone git
    ```
   git clone https://github.com/tangtheduy/se06-13.1.git
   ```
* Chạy Flask
  ```
   export FLASK_APP=demo.py
   ```
   ```
   flask run
   ```
### 6.
### 7.. Thành viên nhóm
* Lê Minh Dũng : Trưởng nhóm
* Bùi Việt Anh
* Tăng Thế Duy
* Trần Khánh Duy

