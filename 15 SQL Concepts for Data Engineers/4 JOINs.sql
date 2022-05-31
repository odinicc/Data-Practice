SELECT E.F_NAME ,E.L_NAME, J.START_DATE,JOBS.JOB_TITLE ,D.DEP_NAME
FROM EMPLOYEES E
LEFT JOIN JOB_HISTORY J
ON E.EMP_ID = J.EMPL_ID
LEFT JOIN JOBS
ON JOBS.JOB_IDENT = E.JOB_ID
LEFT JOIN DEPARTMENTS D
ON D.DEPT_ID_DEP = E.DEP_ID
WHERE E.DEP_ID = 5