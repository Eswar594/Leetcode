SELECT P.firstName,P.lastname,A.city,A.state  from Person P
LEFT JOIN
Address A ON P.personId = A.personId;
