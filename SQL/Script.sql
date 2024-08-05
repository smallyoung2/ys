-- 4.4.1 데이터 베이스 및 테이블 만들기
-- mysql 새로운 데이터베이스 ("haksa") 생성
create database haksa;

-- 생성된 database 확인
show databases;

-- 생성된 database 사용하기 위해 데이터베이스 변경
use haksa;

-- 인사테이블("insa") 생성 및 데이터 입력
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

select * from insa;