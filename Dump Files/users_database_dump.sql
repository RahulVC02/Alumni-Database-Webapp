drop database users;
create database users;
use users;

create table login_details(
     name varchar(30),
     password varchar(30),	
     role varchar(30)
);

insert into login_details values
("Kanishk", "pass123", "admin"),
("Rahul", "pass123", "admin"),
("Inder", "pass123", "admin"),
("Dhairya", "pass123", "admin"),
("Bhavesh", "pass345", "Student"),
("Kalash", "pass123", "admin"),
("Nokzendi", "pass567", "employee"),
("Jimmy", "pass567", "employee"),
("Harsh", "pass123", "admin"),
("Medhansh", "pass345", "Student"),
("TA", "pass123", "admin");

select * from login_details;
