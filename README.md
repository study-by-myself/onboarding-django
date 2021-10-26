# onboarding-django

### wiki
https://github.com/study-by-myself/onboarding-django/wiki

## Implemented Requirements
> ViewSets으로 CRUD를 간단하게 구현했습니다.
> 
> DRF로 rest api를 만들었습니다.
> 
> settings.py에 rest framework에서 제공하는 pagination 설정을 추가하였습니다.
> 
> 회원 가입 시 검증과정이 필요하므로 validated_data를 추가하여 create을 overriding 했습니다.
> 
> rest framework에서 기본적으로 제공하는 login을 그대로 썼습니다.
> 

- [x]  post CRUD
- [x]  sign-up | sign-in | sign-out
- [x]  authentication and permission
- [x]  pagination

## How to run


### clone repository
    
    git clone https://github.com/study-by-myself/onboarding-django.git
    
### virtual env settings
    
    python3 -m venv venv

    # turn on
    . venv/bin/activate
    
    # turn off
    deactivate
    
### pip install requirements
    
    pip install -r requirements.txt

    
### db settings
    
    python manage.py makemigrations
    python manage.py migrate
    
    
### run server
    
    python manage.py runserver
    
    

## ERD
![Screen Shot 2021-10-27 at 12 39 06 AM](https://user-images.githubusercontent.com/60090391/138913166-118994be-8ff9-4853-adaf-7209774aeb85.png)

## Tech Spec

> **Django The web framework for perfectionists with deadlines.**
> 
> 장고를 선택한 이유 : 마감까지 빠르고 쉽게 요구사항을 충족시킬 수 있어서
> 
- Django
- Django-Rest-Framework
- SQLite

## Directory Structure
> 재사용성을  회원가입 / 로그인 / 로그아웃과 게시판 CRUD를 각각 다른 app으로 분리하였습니다.
> 

- config : project

- board : post crud

- sign : signup / sigin / signout

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
