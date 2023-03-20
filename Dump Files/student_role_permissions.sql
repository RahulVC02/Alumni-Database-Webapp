use alumni;

-- Alumni Details
select Roll_Number, Full_Name, Contact_Number, Branch, Degree, Email, DoB, Year_of_Graduation, Picture from alumni;
create view Alumni_Details as select Roll_Number, Full_Name, Contact_Number, Branch, Degree, Email, DoB, Year_of_Graduation, Picture from alumni;
GRANT select on Alumni_Details to student;

-- Instructors
SELECT instructor.*, belongsto.Department_name FROM instructor NATURAL JOIN belongsto order by belongsto.Department_name, instructor.Instructor_ID;
create view Instructors as SELECT instructor.*, belongsto.Department_name FROM instructor NATURAL JOIN belongsto order by belongsto.Department_name, instructor.Instructor_ID;
GRANT select on Instructors to student;

-- Departments
GRANT select ON department TO student;

-- Alumni Projects
select project_guide.Roll_Number, alumni.Full_Name as Student_Name, project_guide.Title as Project_Title, instructor.Instructor_name, projects.Outcome, projects.Duration from project_guide natural join alumni natural join projects natural join instructor order by project_guide.Roll_Number, project_guide.Title;
create view Alumni_Projects as select project_guide.Roll_Number, alumni.Full_Name as Student_Name, project_guide.Title as Project_Title, instructor.Instructor_name, projects.Outcome, projects.Duration from project_guide natural join alumni natural join projects natural join instructor order by project_guide.Roll_Number, project_guide.Title;
GRANT select on Alumni_Projects to student;

-- Alumni Achievements
select alumni.Roll_Number, alumni.Full_Name, achievements.Purpose, achievements.Achievement_Date, achievements.Description from alumni natural join achievements order by achievements.Purpose, achievements.Achievement_Date;
create view Alumni_Achievements as select alumni.Roll_Number, alumni.Full_Name, achievements.Purpose, achievements.Achievement_Date, achievements.Description from alumni natural join achievements order by achievements.Purpose, achievements.Achievement_Date;
GRANT select on Alumni_Achievements to student;

-- Faculty Advisors
SELECT Instructor_Name, Work_email as Email FROM (SELECT DISTINCT Instructor_ID FROM fa) AS f_advisor NATURAL JOIN instructor;
create view Faculty_Advisors as SELECT Instructor_Name, Work_email as Email FROM (SELECT DISTINCT Instructor_ID FROM fa) AS f_advisor NATURAL JOIN instructor;
GRANT select on Faculty_Advisors to student;
