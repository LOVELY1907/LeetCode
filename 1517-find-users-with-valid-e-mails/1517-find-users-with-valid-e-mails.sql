SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$'
  AND BINARY SUBSTRING(mail, LOCATE('@', mail) + 1) = 'leetcode.com'
ORDER BY user_id;