-- SQLite
SELECT AVG(salary) FROM employees WHERE name LIKE 'john';
UPDATE employees
SET hireDate = "2017-05-19"
WHERE id = 13;