DROP TABLE IF EXISTS students CASCADE;
DROP TABLE IF EXISTS cohorts CASCADE;

CREATE TABLE cohorts (
  id serial PRIMARY KEY,
  cohort_name varchar(100) NOT NULL
);

CREATE TABLE students (
  id serial PRIMARY KEY,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL,
  cohort_id integer REFERENCES cohorts
);

