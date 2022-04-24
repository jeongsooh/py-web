# py-web
	1. 가상환경 설정
	# pip install virtualenv
	
	새로 설치된 명령 virtualenv를 통해서 가상환경(project-name) 생성
	# virtualenv project-name
	
	2. 가상환경 활성화
	# source project-name/bin/activate 또는 그냥 # project-name/bin/activate 
	실행하면 프롬프트에 project-name이 포함되서 activation 된 것을 표시함
	(project-name) # 
	3. 다음으로 가상화된 상태에서 django 설치
	(project-name) # pip install django
	4. Django 설치하고 나면 django-admin 이란 새로운  명령이 설치되는데 이것을 이용해서 프로젝트와 앱을 만든다.
	(project-name) # django-admin startproject fc_community
	실행하고 나면 fc_community라는 folder가 생기고, 프로젝트의 구조를 형성하는 기본 화일들이 생성된다.
	5. 다음은 fc_community라는 folder로 들어가서 board라는 이름의 앱을 생성한다.
	(project-name) # cd fc_community
	(project-name) fc_community# django-admin startapp board
	Fc_community folder 안에 board라는 폴더가 생성되고 마찬가지로 기본적인 화일들이 생성된다.
  6. 다음으로 생성된 앱은 반드시 프로젝트에 등록을 해야 한다. Fc_community 프로젝트에 보면 같은 이름의 폴더가 있는데 그 안에 settings.py 란 화일이 있고 거기에 아래와 같이 등록한다.
  
![image](https://user-images.githubusercontent.com/29830424/164982446-ec3dd436-30e5-4743-8efa-48b2067a53e1.png)

  7. 다음 최초로 모델을 만든다. 모델은 DB와 관련된 것들로.. Models.py를 편집해서 완성한다. 그 다음 현재 프로젝트 폴더에 있는 manage.py를 실행시켜서 db를 생성할 수 있는 .py file을 생성한다. 
	(project-name) fc_community# python3 manage.py makemigration
  
  ![image](https://user-images.githubusercontent.com/29830424/164982581-61d8a7e7-e0db-4b25-bc20-db2e8386f076.png)

	8. 다음은 이렇게 생성된 0001_initial.py 화일을 실행해서 실제로 DB를 생성한다.
	(project-name) fc_community# python3 manage.py migrate
	
  ![image](https://user-images.githubusercontent.com/29830424/164982602-138f4210-4bc5-48e2-8055-cb9e450f785c.png)

	9. 끝나면 db.sqlite3란 이름으로 db가 생성된 것을 확인하고..  실제 내용 확인 (db tool이나 sqlite3 db.sqlite3로 확인)
  
	10. 다음은 사용자 생성
	(project-name) fc_community# python3 manage.py createsuperuser 
  
	11. 다음은 테스트 서버 실행
	(project-name) fc_community# python3 manage.py runserver
  
  12. 11번의 runserver 실행 후 알려주는 url을 통해서  브라우저에서 db 관리 기능 수행

  ![image](https://user-images.githubusercontent.com/29830424/164982883-ec8e623d-201f-44fa-bbff-be985a6ef3a0.png)

  13. 다음은  django admin을 보강하는 작업..  Fcuser/admin.py 작업..

	14. Models.py 작성 또는 변경 후엔 항상 makemigration
	(project-name) fc_community# python manage.py makemigrations
  
	15. 다음은 실제 데이터베이스에도 반영
  (project-name) fc_community# python manage.py migrate



