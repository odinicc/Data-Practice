-- 1. Write an SQL query to fetch the EmpId and FullName of all the employees
-- working under the Manager with id – ‘986’

SELECT EmpId, FullName
FROM EmployeeDetails
WHERE ManagerId = 986;


-- 2. Write an SQL query to fetch the different projects available from the EmployeeSalary table.

select distinct project 
from employeesalary; 

-- 3. Write an SQL query to fetch the count of employees working in project ‘P1’.
select count(*)
from employeesalary
where project = 'P1';

-- 4. Write an SQL query to find the maximum, minimum, and average salary of the employees.
select min(salary),max(salary),avg(salary) 
from employeesalary


-- 5. Write an SQL query to find the employee id whose salary lies in the range of 9000 and 15000.
select *
from employeesalary
where salary < 15000 and salary > 9000

-- 6. Write an SQL query to fetch those employees who live in Toronto and work under the manager with ManagerId – 321.

select *
from employeedetails 
where 	managerid  = 321 and city = 'Toronto'

-- 7. Write an SQL query to fetch all the employees who either live in California or work under a manager with ManagerId – 321.
select *
from employeedetails 
where city = 'California' 
or managerid = 321;

-- 8. Write an SQL query to fetch all those employees who work on Projects other than P1.
select *
from employeesalary
where project != 'P1';

-- 9. Write an SQL query to display the total salary of each employee adding the Salary with Variable value.
select salary + variable  as super_salary
from employeesalary

-- 10. Write an SQL query to fetch the employees whose name begins with any two characters, 
-- followed by a text “hn” and ends with any sequence of characters.
select *
from employeedetails 
where fullname like '__hn%';

-- 11. Write an SQL query to fetch all the EmpIds which are present 
-- in either of the tables – ‘EmployeeDetails’ and ‘EmployeeSalary’.
select empid
from employeedetails
union 
select empid
from employeesalary 

-- 14. Write an SQL query to fetch the EmpIds that are present in both the tables –   
--‘EmployeeDetails’ and ‘EmployeeSalary.
SELECT EmpId FROM 
EmployeeDetails 
where EmpId IN 
(SELECT EmpId FROM EmployeeSalary);

-- 15. Write an SQL query to fetch the EmpIds that are present in
-- EmployeeDetails but not in EmployeeSalary.
SELECT EmpId FROM 
EmployeeDetails 
where EmpId Not IN 
(SELECT EmpId FROM EmployeeSalary);

-- 16 Write an SQL query to fetch the employee’s full names and replace the space with ‘-’.
SELECT regexp_replace(fullname, ' ', '-')
FROM EmployeeDetails;

-- 17 Write an SQL query to fetch the position of a given character(s) in a field.
SELECT position('Snow'in fullname)
FROM EmployeeDetails;

-- 18 Write an SQL query to display both the EmpId and ManagerId together.
SELECT CONCAT(EmpId,' - ' ,ManagerId) as NewId
FROM EmployeeDetails;

-- 19. Write a query to fetch only the first name(string before space) 
-- from the FullName column of the EmployeeDetails table.
SELECT 
substring(fullname from 1 for position(' 'in fullname)) as first_name,
substring(fullname from position(' 'in fullname)+1) as last_name
FROM EmployeeDetails;

-- 20. Write an SQL query to uppercase the name of the employee and lowercase the city values.
SELECT Upper(fullname), Lower(city)
FROM EmployeeDetails;

-- 21. Write an SQL query to find the count of the total occurrences of a particular character – ‘n’ in the FullName field.

SELECT 
fullname,
(char_length(fullname) - char_length(replace (fullname,'o' ,''))) as n_count 
FROM EmployeeDetails;

-- 22. Write an SQL query to update the employee names 
-- by removing leading and trailing spaces.
update EmployeeDetails
set fullname = trim(fullname);

-- 23. Fetch all the employees who are not working on any project. 
SELECT EmpId 
FROM EmployeeSalary 
WHERE Project IS NULL;