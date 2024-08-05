-- 학사관리
create database haksa default character set utf8 collate utf8_general_ci;
show databases;

user mysql;

-- 사용자 조회
select user,host from user;
select user();

-- 사용자 권한 조회
show grants for 'root'@'localhost';

-- 사용자 추가
-- id : kimsy@localhost
-- pw : kimsy
create user kimsy@localhost identiied by 'kimsy'

-- 사용자 권한 부여
grant all pribileges on haksa.* to kimsy@localhost;
show grants for 'kimsy'@'localhost';

-- 사용자 삭제
drop user kimsy@localhost;

