# onboarding-django

## Deployed demo page

> NOT_YET . . .
> 

## Implemented Requirements

- [x]  post CRUD
- [x]  sign-up | sign-in | sign-out
- [x]  authentication and permission
- [x]  pagination

## How to run

- clone repository
    
    ```python
    git clone https://github.com/study-by-myself/onboarding-django.git
    ```
    
- virtual env settings
    
    ```python
    python3 -m venv venv
    # turn on
    . venv/bin/activate
    
    # turn off
    deactivate
    ```
    
- pip install requirements
    
    ```python
    pip install -r requirements.txt
    ```
    
- db settings
    
    ```python
    python manage.py makemigrations
    python manage.py migrate
    ```
    
- run server
    
    ```python
    python manage.py runserver
    ```
    

## ERD
![Screen Shot 2021-10-27 at 12 39 06 AM](https://user-images.githubusercontent.com/60090391/138913166-118994be-8ff9-4853-adaf-7209774aeb85.png)

## Tech Spec

> **Django The web framework for perfectionists with deadlines.**
> 
- Django
- Django-Rest-Framework
- SQLite

## Directory Structure

```python
.
├── README.md
├── board
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── sign
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── venv

12 directories, 27 files
```

# API Document

## Board CRUD `/post`

### Create `POST` `/`

게시글을 생성합니다.

```python
# request

{
	"title": STRING,
	"content": STRING
}
```

### Read `GET` `/`

게시글 리스트를 불러옵니다.

```python
# request

{}
```

### Read Detail `GET` `/<id:int>`

게시글 상세 페이지를 조회합니다.

```python
# request

{}
```

### Update `PUT` `/<id:int>`

게시글을 업데이트합니다.

```python
# request

{
	"title": STRING,
	"content": STRING
}
```

### DELETE `DELETE` `/<id:int>`

게시글을 삭제합니다.

```python
# request

{}
```

### Pagination `GET` `/?limit=5&offset=0`

기본적으로 5개로 설정되어 있습니다. limit과 offset을 자유롭게 바꿀 수 있습니다.

```python
# request

{}
```

## 회원 `/user`

### 회원가입 `POST` `/signup`

```python
# request

{
	"nickname": STRING,
	"username": STRING,
	"email": STRING,
	"password": STRING,
}
```

### 로그인 `POST` `/api-auth/login`

```python
# request

{
	"nickname": STRING,
	"password": STRING,
}
```

### 로그아웃 `DELETE` `/api-auth/logout`

```python
# request

{}
```
