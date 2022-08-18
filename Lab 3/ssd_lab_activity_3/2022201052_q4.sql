select S.Dnumber,S.Dname,COUNT(distinct L.Dlocation) from DEPARTMENT S,DEPT_LOCATIONS L where S.Dnumber=L.Dnumber and S.Mgr_ssn
in 
(select F.Essn  from DEPARTMENT D, DEPENDENT F where F.Sex="F" 
group by F.Essn having COUNT(F.Bdate)>1)
group by  L.Dnumber;
