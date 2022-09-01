select F.Essn as'Manager SSN', D.Dnumber as 'Dept NUM',COUNT(*) as 'Number of Dependents' from DEPENDENT F, DEPARTMENT D
where F.Essn=D.Mgr_ssn and F.Essn in 
		(select Mgr_ssn from DEPARTMENT where Dnumber in 
        (select Dnumber from DEPT_LOCATIONS group by Dnumber having COUNT(Dnumber)>1 )
        ) group by D.Dnumber;
