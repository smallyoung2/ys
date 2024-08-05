#4.1 MySql 데이터베이스 생성
#4.1.1 데이터 베이스 및 테이블 만들기
create database haksa;

show databases;

use haksa;

create table insa(
	bunho int(1) auto_increment,
    name char(8) not null,
    e_name char(4),
    town char(6) not null,
    primary key(bunho)
    );
    
insert into insa values('1','홍길동','hong','서울');
insert into insa values('2','제갈공명','je','부산');
insert into insa values('3','순자','soon','대구');
insert into insa values('4','이순신','lee','대전');
insert into insa values(null,'연개소문','yean','서울');
insert into insa values(null,'강감찬',NULL,'부산');
insert into insa values(null,'최영','','광주');
insert into insa (name,e_name,town) values('계백','gae','서울');

#4.1.2 commit/rollvack 작업

select * from insa;

set autocommit=0;			#autocommit 하지 않도록 설정
commit;

update insa					#번호 4 번의 town을 한산도로 업데이트
set town='한산도'
where bunho=4;
select * from insa;	

rollback;
select * from insa;

update insa					#town 부산을 인천으로 업데이트
set town='인천'
where town='부산';
select *from insa;

commit;						#insa 테이블 내용 데이터 베이스에 저장 :commit

rollback;					#commit 했으므로 복구 x
select * from insa;

#4.1.3 savepoint/truncate 작업
update insa 				#번호 2번의 town 여수로 업데이트
set town='여수'
where bunho=2;
select * from insa;

savepoint aa;				#savepoint 'aa' 지정

delete from insa 			#번호 3 의 행 삭제 
where bunho=3;
select * from insa;

rollback to aa;				#savepoint aa 로 rollback
select * from insa;

truncate table insa;		#'insa'테이블의 삭제 처리
select * from insa;

rollback;
select * from insa;			# truncate 작업의 삭제시 복구 처리 x

desc insa;					#describe 설명

#4.2 SQL 데이터형(data type)
#4.2.1 SQL 데이터형
"""
1. 숫자 데이터형
1) 정수 데이터형(int)
2) 실수 데이터형(float)

2. 문자 데이터형
1) char데이터형:1~255바이트,, 고정길이 문자열 저장,, varchar보다 검색속도 빠름
2) varchar데이터형:최대 255바이트, 정의된 저장공간보다 입력데이터가 길면 에러값 리턴 
3) blob,text데이터형:65535이상의 거대한 텍스트 데이터 저장시 사용(blob:대소문자구분o, text:대소문자구분x)

3. 날짜 데이터형
- sysdate라는 함수 사용하여 현재 OS의 날짜조회
- select now(); 사용하여 현재 시스텐 날짜, 시간 조회 

4. 바이너리 데이터형
- 음성,화상(이미지),동영상 같은 데이터를 저장,, 제약점으로는 내장함수 사용 x
- raw 데이터형, long raw 데이터형, blob 데이터형
"""

#4.2.2 NULL 값
-- not null 로 정의된 칼럼은 NULL 값 사용 X

#4.3 학사 관리 예제 만들기
#4.3.1 데이터 베이스 및 사용자 계정 생성
show databases;

#4.3.2 테이블 생성

#학과 테이블
create table department(
	dept_code int(2) not null,		#학과번호
	dept_name char(30) not null,	#학과명
	dept_ename varchar(50),			#학과영문이름
	create_date date default null,	#학과생성날짜
	primary key(dept_code)
	)engine=innoDB;
	
#학적(학생신상)테이블
create table student(
	stu_no char(10) not null,		#학번
	stu_name char(10) not null,		#학생이름
	stu_ename varchar(30) ,			#영문이름
	dept_code int(2) not null,		#학과코드
	grade int(1) not null,			#학년
	class int(1) not null,			#반
	juya char(2),					#주야구분
	birthday varchar(8) not null,	#생년월일
	gender varchar(1) not null,		#성별
	post_no varchar(5) not null,	#우편번호
	address varchar(100),			#주소
	tel1 varchar(3),				#집전화 지역
	tel2 varchar(4),				#집전화 국
	tel3 varchar(4),				#집전화 번호
	mobile varchar(14),				#휴대전화 번호
	primary key (stu_no),			
	constraint s_dp_fk foreign key(dept_code)	#외래키학과 테이블의 학과코드
	references department(dept_code)
	)engine=innoDB;
	
#수강신청
create table attend(
	stu_no char(10) not null,		#학번
	att_year char(4) not null,		#수강년도
	att_term int(1) not null,		#수강학기
	att_isu int(1) not null,		#이수구분
	sub_code char(5) not null,		#과목코드
	prof_code char(4) not null,		#교수코드
	att_point int(1) not null,		#이수학점
	att_grade int(3) default '0',	#취득점수
	att_div char(1) default 'N' not null,	#수강신청구분
	att_jae char(1) default '1',			#재수강구분(1:본학기,2:재수강,3:계절학기)
	att_date date not null,					#수강처리일자
	primary key (stu_no,att_year,att_term,sub_code,prof_code,att_jae)
	)engine=innoDB;

# 등록금테이블
create table fee(
stu_no varchar(10) Not null, 	#학번
fee_year varchar(4) Not null,   #등록년도
fee_term int(1) Not null, 	    #등록학기
fee_enter int(7), 				#입학금
fee_price int(7) Not null, 		#등록금(수업료)
fee_total int(7) Default '0' Not null,	 #등록금총액=입학금+수업료
jang_code char(2) Null, 		#장학코드
jang_total int(7), 				#장학금액
fee_pay int(7) Default '0' Not null, 	 #납부총액=등록금총액-장학금액
fee_div char(1) Default 'N' Not null,	 #등록구분
fee_date date Not null, #등록날짜
primary key (stu_no, fee_year, fee_term)
) engine = innoDB;

# 성적테이블
create table score(
stu_no char(10) Not null, #학번
sco_year char(4) Not null, #성적취득년도
sco_term int(1) Not null, #학기
req_point int(2), #신청학점
take_point int(2), #취득학점
exam_avg float(2,1), #평점평균
exam_total int(4), #백분율 총점
sco_div char(1), #성적구분
sco_date date, #성적처리일자
primary key (stu_no, sco_year, sco_term)
) engine = innoDB;

# 교과목테이블
create table subject(
sub_code char(5) Not null, #과목번호
sub_name varchar(50) Not null, #과목명
sub_ename varchar(50), #영문과목명
create_year char(4), #개설년도
primary key (sub_code)
)engine = innoDB;

# 교수테이블
create table professor(
prof_code char(4) Not null, #교수번호
prof_name char(10) Not null, #교수명
prof_ename varchar(30), #교수영문이름
create_date date default null, #교수임용날짜
primary key (prof_code)
)engine = innoDB;

# 동아리테이블
create table circle(
cir_num int(4) Not null auto_increment, #동아리가입번호
cir_name char(30) Not null, #동아리명
stu_no char(10) Not Null, #학번
stu_name char(10) Not Null, #이름
president char(1) default '2' Not null, #동아리회장(0), 부회장(1), 회원(2)
primary key (cir_num)
)engine = innoDB;

# 도로명 우편번호테이블
create table post(
post_no varchar(6) Not null, #구역번호 1 신우편번호
sido_name varchar(20) Not null, #시도명 2
sido_eng varchar(40) Not null, #시도영문 3
sigun_name varchar(20) Not null, #시군구명 4
sigun_eng varchar(40) Not null, #시군구영문 5
rowtown_name varchar(20) Not null, #읍면 6
rowtown_eng varchar(40) Not null, #읍면영문 7
road_code varchar(12), #도로명코드 8 (시군구코드(5)+도로명번호(7))
road_name varchar(80), #도로명 9 
road_eng varchar(80), #도로영문명 10
underground_gubun varchar(1), #지하여부 11 (0 : 지상, 1 : 지하, 2 : 공중)
building_bon int(5), #건물번호본번 12
building_boo int(5), #건물번호부번 13
management_no varchar(25) Not null, #건물관리번호 14 
baedal varchar(40), #다량배달처명 15 (NULL)
town_building varchar(200), #시군구용 건물명 16
row_code varchar(10) Not null, #법정동코드 17
row_dongname varchar(20), #법정동명 18
ri_name varchar(20), #리명 19
administration_name varchar(40), #행정동명 20
mountain_gubun varchar(1), #산여부 21 (0 : 대지, 1 : 산)
bungi int(4), #지번본번(번지) 22
town_no varchar(2), #읍면동일련번호 23
ho int(4), #지번부번(호) 24
gu_post_no varchar(6), #구 우편번호 25 (NULL)
post_seq varchar(3), #우편일련번호 26 (NULL)
primary key (management_no)
)engine = innoDB;



show variables like 'secure_file_priv';

#4.3.3 테이블에 데이터 삽입
# DEPARTMENT 입력
INSERT INTO DEPARTMENT VALUES (10,'간호학과','Dept. of Nersing','1991-02-01');
INSERT INTO DEPARTMENT VALUES (20,'경영학과','Dept. of Management','1992-02-10');
INSERT INTO DEPARTMENT VALUES (30,'수학학과','Dept. of Mathematics','1993-02-20');
INSERT INTO DEPARTMENT VALUES (40,'컴퓨터정보학과','Dept. of Computer Information','1997-02-01');
INSERT INTO DEPARTMENT VALUES (50,'IT융합학과','Dept. of Information Technology Fusion','2019-02-10');
INSERT INTO DEPARTMENT VALUES (60,'회계학과','Dept. of Accounting','2019-02-01');

select * from department;

# STUDENT 학생 테이블 입력
INSERT INTO STUDENT VALUES ('201410012', '박도상', 'Park Do-Sang', 40, 4, 1, '주', 
'19960116','1','01066','101동 203호','02','744','6126','010-0611-9884');
insert into student values ('0161001', '박정인','Park Jung-In',40,3,1,'주',
'19970403','2','04957','102동 306호','02','652','2439','010-3142-1294');
INSERT INTO STUDENT VALUES ('20181001', '장수인', 'Jang Su-In', 40, 2, 1, '주', 
'19990209','1','57991','108동 1101호','061','791','1236','');
INSERT INTO STUDENT VALUES ('20181002', '정인정', 'Jung In-Jung', 40, 2, 2, '주', 
'19960315','2','05270','6동 1203호','02','723','1078','010-0605-7837');
INSERT INTO STUDENT VALUES ('20181003', '이상진', 'lee sang-jin', 40, 2, 1, '주', 
'19960819','1','17826','107동 504호','031','691','5426','');
INSERT INTO STUDENT VALUES ('20181004', '김유미', 'Kim Yoo-Mi', 40, 2, 2, '주', 
'19960207','2','15348','507동 302호','031','763','1439','010-0617-1290');
INSERT INTO STUDENT VALUES ('20191001', '김유신', 'Kim Yoo-Shin', 40, 1, 3, '야', 
'20001007','3','06034','109동 1203호','02','685','7818','010-9876-1299');
INSERT INTO STUDENT VALUES ('20191002', '홍길동', 'Hong GilDong', 40, 1, 3, '야', 
'20000402','3','59635','104동 605호','061','642','4034','010-6425-9245');
INSERT INTO STUDENT VALUES ('20191003', '고혜진', 'Ko Hea-Jin', 10, 1, 1, '주', 
'20000607','4','47783','1011동 102호','051','781','5135','');
INSERT INTO STUDENT VALUES ('20191004', '이순신', 'Lee Sun-Shin', 10, 1, 3, '야', 
'20000222','3','01901','2동 1004호','02','745','7667','010-7141-1860');
INSERT INTO STUDENT VALUES ('20191005', '김할리', 'Kim Hal-Li', 40, 1, 2, '주', 
'20010418','5','02463','561동 102호','02','746','5485','010-4624-0460');
INSERT INTO STUDENT VALUES ('20191006', '최예스터', 'Choi Esther', 40, 1, 2, '주', 
'20021003','6','03975','101동 540호','02','945','6793','');
INSERT INTO STUDENT VALUES ('20191007', '신안나', 'Shin An-Na', 40, 1, 2, '주', 
'20011214','4','06305','208동 402호','02','745','5485','010-5897-0874');
INSERT INTO STUDENT VALUES ('20191008', '연개소문', 'Yean Gae-So-Moon', 40, 1, 3, '야', 
'20000615','3','48020','정명빌라 2080호','051','632','9306','010-0641-9304');
INSERT INTO STUDENT VALUES ('20191009', '유하나', 'Yoo Ha-Na', 50, 1, 1, '주', 
'20000921','4','61053','204동 512호','062','651','5992','010-0651-0707');
INSERT INTO STUDENT VALUES ('20201001', '김영호', 'Yoo Young-Ho', 50, 1, 3, '야', 
'20000811','3','61689','107동 510호','062','652','5998','010-4605-5598');
INSERT INTO STUDENT VALUES ('20201002', '강감찬', 'Gang Gam-Chan', 50, 1, 3, '야', 
'20000312','3','34331','103동 505호','042','123','1234','010-1234-1567');

select * from student;

 UPDATE student
SET gender = '1' 
 WHERE stu_name ='장수인'; 

commit;
# 조인 :join
select s.stu_no,s.stu_name,s.dept_code,d.dept_name,d.dept_ename
	from student s,department d
	where s.dept_code=d.dept_code;


# SUBJECT 입력
INSERT INTO SUBJECT VALUES ('4001', '데이터베이스 응용', 'Database Application', '2002');
INSERT INTO SUBJECT VALUES ('4002', '웹사이트 구축', 'Web Site Construction', '2003');
INSERT INTO SUBJECT VALUES ('4003', '소프트웨어공학', 'Software Engineering', '2003');
INSERT INTO SUBJECT VALUES ('4004', '웹프로그래밍', 'Web Programming', '2004');
INSERT INTO SUBJECT VALUES ('4005', '컴퓨터구조', 'Computer Structure', '2001');
INSERT INTO SUBJECT VALUES ('4006', '정보처리실무', 'Information Process Practical business', '2001');
INSERT INTO SUBJECT VALUES ('4007', 'UML', 'UML(Unified Modeling Language)', '2005');
INSERT INTO SUBJECT VALUES ('4008', '운영체제', 'Operating System', '2002');
INSERT INTO SUBJECT VALUES ('4009', '전자상거래 실무', 'Electronic Commerce', '2003');
INSERT INTO SUBJECT VALUES ('4010', '윈도우즈 프로그래밍', 'Windows Programming', '2006');
INSERT INTO SUBJECT VALUES ('4011', '자바프로그래밍', 'Java Programming', '2006');
INSERT INTO SUBJECT VALUES ('4012', '파이썬 프로그래밍', 'Python Programming', '2019');
INSERT INTO SUBJECT VALUES ('4013', '스크래치 프로그래밍', 'Scratch Programming', '2019');

select * from subject;


# PROFESSOR 입력
INSERT INTO PROFESSOR VALUES ('4001','정진용','Jung jin-yong','1995-09-01');
INSERT INTO PROFESSOR VALUES ('4002','나인섭','Na in-sub','2006-02-02');
INSERT INTO PROFESSOR VALUES ('4003','오승재','Oh sung-jae','2003-03-01');
INSERT INTO PROFESSOR VALUES ('4004','고진광','Go jin-gwang','2000-01-15');
INSERT INTO PROFESSOR VALUES ('4005','정병열','Jung byeong-yeol','1998-03-01');
INSERT INTO PROFESSOR VALUES ('4006','박심심','Park sim-sim','1988-03-01');
INSERT INTO PROFESSOR VALUES ('4007','김영식','Kim young-sik','1986-03-01');
INSERT INTO PROFESSOR VALUES ('4008','최우철','Choi woo-chel','1997-03-01');
INSERT INTO PROFESSOR VALUES ('4009','문창우','Moon chang-woo','1995-03-01');
INSERT INTO PROFESSOR VALUES ('5010','정종선','Jung jong-sun','1997-03-01');
INSERT INTO PROFESSOR VALUES ('5011','최종주','Choi jong-joo','1992-03-05');

select * from professor;



# ATTEND 입력
INSERT INTO ATTEND VALUES ('20140001','2014',1,3,4001,'4002',3, 99,'Y','1','2014-03-05');
INSERT INTO ATTEND VALUES ('20140001','2014',1,4,4002,'4003',3, 95,'Y','1','2014-03-05');
INSERT INTO ATTEND VALUES ('20140001','2014',1,4,4003,'4004',3, 97,'Y','1','2014-03-05');
INSERT INTO ATTEND VALUES ('20140001','2014',1,4,4004,'4001',3, 98,'Y','1','2014-03-05');
INSERT INTO ATTEND VALUES ('20140001','2014',1,4,4005,'4007',3, 96,'Y','1','2014-03-05');
INSERT INTO ATTEND VALUES ('20140001','2014',1,4,4006,'4008',3, 95,'Y','1','2014-03-05');
INSERT INTO ATTEND VALUES ('20140001','2014',2,3,4007,'4009',3, 93,'Y','1','2014-09-03');
INSERT INTO ATTEND VALUES ('20140001','2014',2,4,4008,'4005',3, 92,'Y','1','2014-09-03');
INSERT INTO ATTEND VALUES ('20140001','2014',2,4,4009,'4006',3, 94,'Y','1','2014-09-03');
INSERT INTO ATTEND VALUES ('20140001','2014',2,4,4010,'4001',3, 90,'Y','1','2014-09-03');
INSERT INTO ATTEND VALUES ('20140001','2014',2,4,4011,'4002',3, 91,'Y','1','2014-09-03');
INSERT INTO ATTEND VALUES ('20140001','2014',2,4,4012,'4003',3, 92,'Y','1','2014-09-03');

INSERT INTO ATTEND VALUES ('20161001','2014',1,3,4001,'4002',3, 99,'Y','1','2016-03-05');
INSERT INTO ATTEND VALUES ('20161001','2014',1,4,4002,'4003',3, 95,'Y','1','2016-03-05');
INSERT INTO ATTEND VALUES ('20161001','2014',1,4,4003,'4004',3, 97,'Y','1','2016-03-05');
INSERT INTO ATTEND VALUES ('20161001','2014',1,4,4004,'4001',3, 98,'Y','1','2016-03-05');
INSERT INTO ATTEND VALUES ('20161001','2014',1,4,4005,'4007',3, 93,'Y','1','2016-03-05');
INSERT INTO ATTEND VALUES ('20161001','2014',1,4,4006,'4008',3, 95,'Y','1','2016-03-05');

 

select * from attend;


# FEE 입력
INSERT INTO FEE VALUES ('20141001','2014',1,500000,3000000,3500000,01,500000,3000000,'Y','2014-02-18');
INSERT INTO FEE VALUES ('20141001','2014',2,NULL,3000000,3000000,10,2500000,500000,'Y','2014-08-20');
INSERT INTO FEE VALUES ('20141001','2015',1,NULL,3000000,3000000,11,2000000,1000000,'Y','2015-02-18');
INSERT INTO FEE VALUES ('20141001','2015',2,NULL,3000000,3000000,21,800000,2200000,'Y','2015-08-10');
INSERT INTO FEE VALUES ('20141001','2018',1,500000,2500000,3000000,10,2500000,0,'Y','2018-02-01');
INSERT INTO FEE VALUES ('20141001','2018',2,NULL,2500000,2500000,10,2500000,300000,'Y','2018-08-10');
INSERT INTO FEE VALUES ('20141001','2019',1,NULL,2800000,2800000,10,2500000,300000,'Y','2019-02-15');
INSERT INTO FEE VALUES ('20141001','2019',2,NULL,2800000,2800000,10,2500000,300000,'Y','2019-08-16');
INSERT INTO FEE VALUES ('20161001','2016',1,NULL,3000000,3000000,10,2500000,500000,'Y','2016-02-14');
INSERT INTO FEE VALUES ('20161001','2016',2,NULL,3000000,3000000,10,2500000,500000,'Y','2016-08-18');
INSERT INTO FEE VALUES ('20161001','2019',1,NULL,3000000,3000000,11,2000000,1000000,'Y','2019-02-10');
INSERT INTO FEE VALUES ('20161001','2019',2,NULL,3000000,3000000,10,2500000,500000,'Y','2019-08-19');
INSERT INTO FEE VALUES ('20191004','2019',1,500000,3000000,3500000,01,500000,3000000,'Y','2019-02-18');
INSERT INTO FEE VALUES ('20191004','2019',2,NULL,3000000,3000000,NULL,NULL,3000000,'Y','2019-08-10');
INSERT INTO FEE VALUES ('20191005','2019',1,500000,3000000,3500000,01,500000,3000000,'Y','2019-02-18');
INSERT INTO FEE VALUES ('20191005','2019',2,NULL,3000000,3000000,0,2000000,2920000,'Y','2006-02-18');
INSERT INTO FEE VALUES ('20191006','2019',1,500000,3000000,3500000,01,500000,3000000,'Y','2019-02-18');
INSERT INTO FEE VALUES ('20191006','2019',2,NULL,3000000,3000000,NULL,NULL,3000000,'Y','2006-02-18');
INSERT INTO FEE VALUES ('20191007','2019',1,500000,3000000,3500000,01,500000,3000000,'Y','2019-02-18');
INSERT INTO FEE VALUES ('20191007','2019',2,NULL,3000000,3000000,NULL,NULL,3000000,'Y','2019-08-10');
INSERT INTO FEE VALUES ('20191008','2019',1,500000,3000000,3500000,01,500000,3000000,'Y','2019-02-18');
INSERT INTO FEE VALUES ('20191008','2019',2,NULL,3000000,3000000,NULL,NULL,3000000,'Y','2019-08-10');
INSERT INTO FEE VALUES ('20201002','2020',1,500000,3000000,3500000,01,500000,3000000,'Y','2020-02-18');
INSERT INTO FEE VALUES ('20201002','2020',2,NULL,3000000,3000000,10,2500000,500000,'Y','2020-08-10');

select * from fee;

# SCORE 입력
INSERT INTO SCORE VALUES ('20141001','2014',1,18,18,4.5,580,'Y','2014-08-10');
INSERT INTO SCORE VALUES ('20141001','2014',2,18,18,4.0,552,'Y','2015-01-11');
INSERT INTO SCORE VALUES ('20191001','2019',1,18,18,4.2,572,'Y','2019-08-09');
INSERT INTO SCORE VALUES ('20191002','2019',1,18,18,4.5,575,'Y','2019-08-09');
INSERT INTO SCORE VALUES ('20191005','2019',1,18,18,4.4,577,'Y','2019-08-09');
INSERT INTO SCORE VALUES ('20191006','2019',1,18,18,4.4,579,'Y','2019-08-09');
INSERT INTO SCORE VALUES ('20191007','2019',2,18,18,0.0,0,'N','2019-11-10');
INSERT INTO SCORE VALUES ('20191001','2019',2,18,18,0.0,0,'N','2019-11-10');
INSERT INTO SCORE VALUES ('20191002','2019',2,18,18,0.0,0,'N','2019-11-10');

select * from score;

# CIRCLE 입력
INSERT INTO CIRCLE VALUES (1,'컴맹탈출','20141001','박도상','0');
INSERT INTO CIRCLE VALUES (2,'컴맹탈출','20191009','유하나','1');
INSERT INTO CIRCLE VALUES (3,'컴맹탈출','20191001','김유신','2');
INSERT INTO CIRCLE VALUES (4,'Java길라잡이','20181001','장수인','2');
INSERT INTO CIRCLE VALUES (5,'Java길라잡이','20191004','이순신','1');
INSERT INTO CIRCLE VALUES (6,'Java길라잡이','20161001','박정인','0');
INSERT INTO CIRCLE VALUES (7,'PHP길라잡이','20191002','홍길동','0');

select * from circle;






START TRANSACTION;

#조인 : join
select distinct s.stu_no,s.stu_name,s.dept_code,d.dept_name,d.dept_ename,s.post_no,p.road_name
	from student s, department d, post p
	where s.dept_code=d.dept_code 
	and s.post_no=p.post_no;












