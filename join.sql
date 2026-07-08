show databases;
use employees;

-- join
create table emp (id int primary key,name text,salary int,deptId int);
create table dept(deptId int primary key,deptName text);

insert into emp values
(101,"aman",56000,1001),
(102,"rahul",34000,1001),
(103,"raman",76000,1002),
(104,"tanvi",23000,1001);

select * from emp;
select * from dept;


insert into dept values
(1001,"IT"),(1002,"sales");

select * from emp as e join dept as d on e.deptId=d.deptId;
