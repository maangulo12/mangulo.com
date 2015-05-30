--> Drop All Tables
DROP TABLE IF EXISTS users;

--> Users Table
CREATE TABLE users (
  user_id SERIAL,
  username VARCHAR(25) NOT NULL UNIQUE,
  pw_hash VARCHAR(60) NOT NULL,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  email VARCHAR(50) NOT NULL UNIQUE,
  PRIMARY KEY (user_id)
);