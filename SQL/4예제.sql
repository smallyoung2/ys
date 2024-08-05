#4.3.4 질의 테이블
-- select 명령문은 테이블로 부터 데이터를 검색할때 사용

#예제4-1 성별 남자(1,3,5)인 학생의 학번,이름,영문이름,학년 성별을 영문이름 순서대로 출력하기
-- asc(오름차순),desc(내림차순)

select * from student;

select stu_no,stu_name,stu_ename,grade,gender
from student 
where gender=1 or gender=3 or gender=5
order by stu_ename;


#예제4-2 1학년이고 성별이 여자인 학생의 학번,이름을 학번내림차순으로 출력
select * from student;

select stu_no,stu_name,gender
from student 
where grade=1
and gender=2 or gender=4 or gender=6
order by stu_no desc;

select stu_no,stu_name,gender
from student 
where (gender=2 or gender=4 or gender=6)
and grade=1
order by stu_no desc;


#예제4-3 교과목 테이블에 관한 모든 정보 출력
select * from subject;


#예제4-4 교과목중 '운영체제'의 생성년도를 2006년으로 변경

update subject
set create_year='2006'
where sub_name='운영체제';

select * from subject;


#예제4-5 교과목 테이블에서 교과목코드,교과목명,교과목영문이름,생성년도를 출력하여라
select sub_code, sub_name, sub_ename, create_year from subject;



-- 테이블의 행내용을 삭제하려면 delete from student
-- 테이블 자체를 삭제하려면    drop table student

#예제4-6 과목명이 'UML'인 과목을 삭제
delete 
from subject 
where sub_name='UML';

select *from subject;


#예제4-7 교과목중 '운영체제'의 생산년도를 2002년으로 변경
update subject 
set create_year='2002'
where sub_name='운영체제';

select *from subject;

#예제4-8 교과목 테이블에 교과목코드 4007, 교과목명 UML, 교과목 영문이름(Unified Modeling Language), 생성년도 2005 행 추가
insert into subject values('4007','UML','Unified Modeling Language','2005');

select *from subject;


##질의(Query) 처리의 최적화
select *
from subject 
where create_year='2002';				#만약 2002년인 행이 많다면 시간소요 큼-> 인덱스 설정하면 시간단축o

create index createix on 				#create_year 열에 인덱스 createix 생성
subject (create_year);

show index from subject;




#4.3.6 뷰(view)
-- 필요에 다라 사용자가 재정의 하여 생성해주는 테이블,,기억공간 차지x
-- 유도된 가상테이블,, 실제 데이터 행을 가지고있는 것처럼 동작하지만 데이터행 존재 x

select * from student;
#예제4-9 student 테이블의 stu_no,stu_name,생년월일, 나이 출력

select stu_no,stu_name,birthday "생년월일",
year(now())-substring(birthday,1,4)+1 "나이"
from student;



#예제4-10 student 테이블의 학번,이름,나이로 구성된 ages뷰테이블을 생성

create view ages(stu_no,stu_name,age) as
select stu_no,stu_name,year(now())-substring(birthday,1,4)+1
from student;

select * from ages;



#4.4 보안설정
#4.4.1 root 사용자의 데이터 보안
use mysql;
database changed

update user set password=password('12345') where user='root';
flush privileges;