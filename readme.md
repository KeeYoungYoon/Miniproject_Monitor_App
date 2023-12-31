//directory tree of this project
```
├── README.md
├── app.py
├── templates
│   ├── index.html
│   ├── request.html
│   └── insert_api_info.html

키값 등은 제거한 상태에서 커밋했습니다.
로컬에서 실행을 위해서는 mariaDB를 설치하고, 테이블을 생성하셔야 합니다.
추가로 슬랙의 bot 토큰 값 및 USER ID 추가해서 사용하시면 됩니다.

현재 DB 상에 저장되어 있는 api 정보를 불러와 호출하는 부분이 아직 수정 필요합니다.
테스트 버튼 생성하여 하드코딩 해둔 api 호출 및 호출 결과 200인 경우 슬랙에 메세지 전송하는 기능까지 구현한 상태입니다.

Readme는 사람이 작성한 부분과 Copilot이 작성한 부분으로 이루어져 있고 Copilot이 작성한 Readme에는 수정이 필요합니다.
추천 해주는 기능이 어느순간부터 중복되는 부분이 있습니다.



```
```
Copilot good recommendation cases
```

![import time](images_copilot/copilot_recomm_slack_cases1.png)
![import time](images_copilot/copilot_recomm_slack_cases2.png)
```
하드코딩으로 구현 되어 있던 message를 변경하기 위한 추천 코드 제공
```

![import time](images_copilot/copilot_recomm_database_info.png)
```
초기 구현을 위해서 DB정보 파악이 가능 추천 코드로 세팅 제공
```

![import time](images_copilot/copilot_recomm_basic_redirect.png)

```
페이지 기본 구성에 도움 되는 기본적인 퍼튼 및 페이지 redirect 처리 제공
위는 index 페이지에서 request 페이지로 이동뒤 다시 index 페이지로 이동하는 버튼 추천
```

![import time](images_copilot/copilot_recomm_database_get.png)

```
기본적인 DB CRUD 기능 제공 하는 버튼 및 function은 추천으로 제공(세부적인 디버깅은 필요했음)
```

![import time](images_copilot/copilot_recomm_database_crud.png)

```
DB CRUD 추가하는데에는 확실히 위처럼 도움되는것 확인 했음
```

```
Copilot bad recommendation cases
```

![import time](images_copilot/copilot_bad_recomm_case_no_fetch.png)

```
fetch로 가져올수 없는 함수에 대한 추천
Backend가 구성되어 있는 상태였기때문에 다음 api를 호출하도록 fetch 될줄 알았으나 그냥 2 붙인걸 추천
```

![import time](images_copilot/copilot_recomm_bad_readme.png)
![import time](images_copilot/copilot_bad_recomm_script.png)

```
readme 작성시와 Front code 작성시에도 딱히 추천 내용 없는 경우에 루프 돌듯 나오는 경우가 있음
추천이 아예 안나오는 경우도 있기 때문에 좀 다른케이스로 보임
```

![import time](images_copilot/copilot_bad_recomm_annotation.png)
![import time](images_copilot/copilot_bad_recomm_annotation_indentataion.png)

```
Swagger Annotation 작성시 전체적으로 추천은 되나 annotation 자체가 주석의 형태로 작성 되다 보니 syntax 오류를 잡지 못함
```

```
Above written by Kee Young
```


Below written by copilot

## 1. Introduction
This project is used to manage the API information. The user can input the API information and save it to the database. The user can also check, delete, update and insert the API information.
## 2. How to install the project
### 2.1. Install the python3.6
```
sudo apt-get install python3.6
```
### 2.2. Install the pip3
```
sudo apt-get install python3-pip
```
### 2.3. Install the virtualenv
```
sudo pip3 install virtualenv
```
### 2.4. Create the virtualenv
```
virtualenv -p python3.6 venv
```
### 2.5. Activate the virtualenv
```
source venv/bin/activate
```
### 2.6. Install the required packages
```
pip install -r requirements.txt
```
### 2.7. Install the mysql
```
sudo apt-get install mysql-server
```
### 2.8. Create the database
```
mysql -u root -p
```
```
CREATE DATABASE api_info;
```
### 2.9. Create the table
```
CREATE TABLE `api_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `api_name` varchar(255) NOT NULL,
  `api_url` varchar(255) NOT NULL,
  `api_method` varchar(255) NOT NULL,
  `api_headers` varchar(255) NOT NULL,
  `api_body` varchar(255) NOT NULL,
  `api_response` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
```
### 2.10. Insert the data


## 3. How to run the project
### 3.1. Install the required packages
```
pip install -r requirements.txt
``` 
### 3.2. Run the project
```
python app.py
```
### 3.3. Open the browser and type the url
```
http://127.0.0.1:5000/
```
### 3.4. Input the API information
```
Input the API information and click the "Submit" button
```
### 3.5. Check the API information
```
Click the "Check" button to check the API information
```
### 3.6. Delete the API information
```
Click the "Delete" button to delete the API information
```
### 3.7. Update the API information
```
Click the "Update" button to update the API information
```
### 3.8. Insert the API information
```
Click the "Insert" button to insert the API information
```
### 3.9. Check the API information
```
Click the "Check" button to check the API information
```
### 3.10. Delete the API information
```
Click the "Delete" button to delete the API information
```
### 3.11. Update the API information
```
Click the "Update" button to update the API information
```
### 3.12. Insert the API information
```
Click the "Insert" button to insert the API information
```
### 3.13. Check the API information
```
Click the "Check" button to check the API information
```

## 4. How to test the project
### 4.1. Install the required packages
```
pip install -r requirements.txt
```
### 4.2. Run the test
```
python test.py
```
### 4.3. Check the test result
```
Check the test result
```

## 5. How to deploy the project
### 5.1. Install the required packages
```
pip install -r requirements.txt
```
### 5.2. Run the project
```
python app.py
```
### 5.3. Open the browser and type the url
```
http://
```
### 5.4. Input the API information
```
Input the API information and click the "Submit" button
```
### 5.5. Check the API information
```
Click the "Check" button to check the API information
```
### 5.6. Delete the API information
```
Click the "Delete" button to delete the API information
```
### 5.7. Update the API information
```
Click the "Update" button to update the API information
```
### 5.8. Insert the API information
```
Click the "Insert" button to insert the API information
```
### 5.9. Check the API information
```
Click the "Check" button to check the API information
```
### 5.10. Delete the API information
```
Click the "Delete" button to delete the API information
```
### 5.11. Update the API information
```
Click the "Update" button to update the API information
```
### 5.12. Insert the API information
```
Click the "Insert" button to insert the API information
```
### 5.13. Check the API information
```
Click the "Check" button to check the API information
```
### 5.14. Delete the API information
```
Click the "Delete" button to delete the API information
```
### 5.15. Update the API information
```
Click the "Update" button to update the API information
```
### 5.16. Insert the API information
```
Click the "Insert" button to insert the API information
```

## 6. How to contribute to the project
### 6.1. Fork the project
```
Fork the project
```
### 6.2. Clone the project
```
git clone
```
### 6.3. Create the branch
```
git checkout -b <branch_name>
```
### 6.4. Commit the change
```
git commit -m "message"
```
### 6.5. Push the change to the branch
```
git push origin <branch_name>
```
### 6.6. Create the pull request
```
Create the pull request
```
### 6.7. Merge the pull request
```
Merge the pull request
```
### 6.8. Check the result
```
Check the result
```

