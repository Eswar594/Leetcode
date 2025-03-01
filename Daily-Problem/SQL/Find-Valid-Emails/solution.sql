SELECT user_id, email 
FROM Users
WHERE email REGEXP '^[A-Za-z0-9_]+@[A-Za-z][A-Za-z0-9_]*\.com$'
ORDER BY user_id ASC;