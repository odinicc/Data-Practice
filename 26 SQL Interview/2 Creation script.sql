CREATE TABLE EmployeeSalary(
	EmpId INT8 PRIMARY KEY,
	Project VARCHAR(50) NOT NULL,
	Salary INT8 NOT NULL,
	Variable INT8 NOT NULL
);

INSERT INTO public.EmployeeSalary(empid, project, salary, variable)
VALUES (121,'P1',8000,500);


INSERT INTO public.EmployeeSalary(empid, project, salary, variable)
VALUES (321,'P2',10000,1000);

INSERT INTO public.EmployeeSalary(empid, project, salary, variable)
VALUES (421,'P1',12000,0);