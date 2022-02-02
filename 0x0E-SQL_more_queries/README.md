# 0x0E. SQL - More queries

## Resources:books:

Read or watch:

- [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/u4h2MXcCQfadszlRMQy-gw)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://intranet.hbtn.io/rltoken/9JjDTdvflUSxwxLNfW8sPg)
- [MySQL constraints](https://intranet.hbtn.io/rltoken/u1P3WmgxehiqwcLBMlksUA)
- [SQL technique: subqueries](https://intranet.hbtn.io/rltoken/YYpPtkqFeKSCsAU4Y_y3Og)
- [Basic query operation: the join](https://intranet.hbtn.io/rltoken/npLCp3WasK0SUSUQqCF25A)
- [SQL technique: multiple joins and the distinct keyword](https://intranet.hbtn.io/rltoken/GmRLMhkY-pPvjcpzyDvmRg)
- [SQL technique: join types](https://intranet.hbtn.io/rltoken/ryjyRRN7696rJV0maP03Xw)
- [SQL technique: union and minus](https://intranet.hbtn.io/rltoken/L7Fi5w8GZG5MSdQZ19e88g)
- [MySQL Cheat Sheet](https://intranet.hbtn.io/rltoken/V9vpLbtkFwV4EZYoiz2NBA)
- [The Seven Types of SQL Joins](https://intranet.hbtn.io/rltoken/ySKSdhFeMDddea07XrDzeQ)
- [MySQL Tutorial](https://intranet.hbtn.io/rltoken/-uqP0a89xUl3SsmV_ZtxRA)
- [SQL Style Guide](https://intranet.hbtn.io/rltoken/jn4SHgwVtOJF0LQYPEIs-g)
- [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/YjNAE7DcadDbT_a7iI0sYw)

---

## Learning Objectives:bulb:

What you should learn from this project:

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

---

### [0. My privileges!](./0-privileges.sql)

- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

### [1. Root user](./1-create_user.sql)

- Write a script that creates the MySQL server user user_0d_1.

### [2. Read user](./2-create_read_user.sql)

- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

### [3. Always a name](./3-force_name.sql)

- Write a script that creates the table force_name on your MySQL server.

### [4. ID can't be null](./4-never_empty.sql)

- Write a script that creates the table id_not_null on your MySQL server.

### [5. Unique ID](./5-unique_id.sql)

- Write a script that creates the table unique_id on your MySQL server.

### [6. States table](./6-states.sql)

- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

### [7. Cities table](./7-cities.sql)

- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

### [8. Cities of California](./8-cities_of_california_subquery.sql)

- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

### [9. Cities by States](./9-cities_by_state_join.sql)

- Write a script that lists all cities contained in the database hbtn_0d_usa.

### [10. Genre ID by show](./10-genre_id_by_show.sql)

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download

### [11. Genre ID for all shows](./11-genre_id_all_shows.sql)

- Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)

### [12. No genre](./12-no_genre.sql)

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)

### [13. Number of shows by genre](./13-count_shows_by_genre.sql)

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)

### [14. My genres](./14-my_genres.sql)

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)

### [15. Only Comedy](./15-comedy_only.sql)

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)

### [16. List shows and genres](./16-shows_by_genre.sql)

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)

---

## Author

JAMILA MOSEKA
