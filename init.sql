
\set POSTGRES_DB `echo $POSTGRES_DB`
SELECT 'CREATE DATABASE $POSTGRES_DB;'
WHERE NOT EXISTS (SELECT 'SELECT FROM pg_database WHERE datname = $POSTGRES_DB;');

\c :POSTGRES_DB

CREATE TABLE IF NOT EXISTS incidents (
 id SERIAL PRIMARY KEY,
 description VARCHAR(200),
 status VARCHAR(20),
 source VARCHAR(100),
 create_dt timestamp with time zone
);
