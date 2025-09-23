# PostgreSQL CLI Command Cheat Sheet

## Connection and Basic Commands

| Command     | Description                    | Example Usage                           |
| ----------- | ------------------------------ | --------------------------------------- |
| `psql`      | Connect to PostgreSQL database | `psql -h localhost -U postgres -d mydb` |
| `psql -l`   | List all databases             | `psql -l`                               |
| `psql -c`   | Execute single command         | `psql -d mydb -c "SELECT version();"`   |
| `psql -f`   | Execute SQL file               | `psql -d mydb -f script.sql`            |
| `\q`        | Quit psql                      | `\q`                                    |
| `\c`        | Connect to different database  | `\c mydb`                               |
| `\conninfo` | Display connection information | `\conninfo`                             |
| `\password` | Change password                | `\password username`                    |

## Database Management

| Command           | Description                 | Example Usage                          |
| ----------------- | --------------------------- | -------------------------------------- |
| `createdb`        | Create new database         | `createdb -U postgres mydb`            |
| `dropdb`          | Delete database             | `dropdb -U postgres mydb`              |
| `\l`              | List all databases          | `\l`                                   |
| `\l+`             | List databases with details | `\l+`                                  |
| `CREATE DATABASE` | Create database (SQL)       | `CREATE DATABASE mydb OWNER postgres;` |
| `DROP DATABASE`   | Drop database (SQL)         | `DROP DATABASE mydb;`                  |
| `ALTER DATABASE`  | Modify database             | `ALTER DATABASE mydb RENAME TO newdb;` |

## Table Operations

| Command        | Description                 | Example Usage                                                   |
| -------------- | --------------------------- | --------------------------------------------------------------- |
| `\dt`          | List all tables             | `\dt`                                                           |
| `\dt+`         | List tables with sizes      | `\dt+`                                                          |
| `\d`           | List all relations          | `\d`                                                            |
| `\d tablename` | Describe table structure    | `\d users`                                                      |
| `\d+`          | List relations with details | `\d+`                                                           |
| `\dt schema.*` | List tables in schema       | `\dt public.*`                                                  |
| `CREATE TABLE` | Create new table            | `CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(50));` |
| `DROP TABLE`   | Delete table                | `DROP TABLE users;`                                             |

## Schema and Object Information

| Command | Description           | Example Usage |
| ------- | --------------------- | ------------- |
| `\dn`   | List all schemas      | `\dn`         |
| `\df`   | List all functions    | `\df`         |
| `\dv`   | List all views        | `\dv`         |
| `\di`   | List all indexes      | `\di`         |
| `\ds`   | List all sequences    | `\ds`         |
| `\dp`   | List table privileges | `\dp`         |
| `\du`   | List all users/roles  | `\du`         |
| `\dg`   | List all groups       | `\dg`         |
| `\db`   | List all tablespaces  | `\db`         |

## User and Permission Management

| Command       | Description             | Example Usage                                      |
| ------------- | ----------------------- | -------------------------------------------------- |
| `createuser`  | Create new user         | `createuser -U postgres -P newuser`                |
| `dropuser`    | Delete user             | `dropuser -U postgres olduser`                     |
| `CREATE USER` | Create user (SQL)       | `CREATE USER newuser WITH PASSWORD 'password123';` |
| `ALTER USER`  | Modify user             | `ALTER USER newuser WITH SUPERUSER;`               |
| `GRANT`       | Grant permissions       | `GRANT SELECT ON users TO newuser;`                |
| `REVOKE`      | Revoke permissions      | `REVOKE SELECT ON users FROM newuser;`             |
| `\du+`        | List users with details | `\du+`                                             |

## Data Import/Export

| Command      | Description             | Example Usage                                |
| ------------ | ----------------------- | -------------------------------------------- |
| `pg_dump`    | Backup database         | `pg_dump -U postgres mydb > backup.sql`      |
| `pg_dumpall` | Backup all databases    | `pg_dumpall -U postgres > all_backup.sql`    |
| `pg_restore` | Restore database        | `pg_restore -U postgres -d mydb backup.dump` |
| `psql -f`    | Import SQL file         | `psql -U postgres -d mydb -f backup.sql`     |
| `\copy`      | Copy data to/from file  | `\copy users FROM 'users.csv' CSV HEADER`    |
| `COPY`       | Copy data (server-side) | `COPY users TO '/tmp/users.csv' CSV HEADER;` |

## Query Execution and Results

| Command       | Description                  | Example Usage                              |
| ------------- | ---------------------------- | ------------------------------------------ |
| `\x`          | Toggle expanded output       | `\x`                                       |
| `\g`          | Execute previous command     | `\g`                                       |
| `\timing`     | Toggle timing display        | `\timing`                                  |
| `\watch`      | Repeat query every N seconds | `SELECT * FROM pg_stat_activity; \watch 5` |
| `\o filename` | Send output to file          | `\o output.txt`                            |
| `\qecho`      | Print text to output         | `\qecho "Starting backup..."`              |
| `\echo`       | Print text to stdout         | `\echo "Query completed"`                  |

## psql Configuration and Settings

| Command     | Description              | Example Usage         |
| ----------- | ------------------------ | --------------------- |
| `\set`      | Set variable             | `\set AUTOCOMMIT off` |
| `\unset`    | Unset variable           | `\unset AUTOCOMMIT`   |
| `\pset`     | Set output format option | `\pset border 2`      |
| `\a`        | Toggle aligned output    | `\a`                  |
| `\t`        | Toggle tuple-only output | `\t`                  |
| `\H`        | Toggle HTML output       | `\H`                  |
| `\T`        | Set table title          | `\T 'User Report'`    |
| `\encoding` | Show/set encoding        | `\encoding UTF8`      |

## Transaction Control

| Command           | Description           | Example Usage         |
| ----------------- | --------------------- | --------------------- |
| `BEGIN`           | Start transaction     | `BEGIN;`              |
| `COMMIT`          | Commit transaction    | `COMMIT;`             |
| `ROLLBACK`        | Rollback transaction  | `ROLLBACK;`           |
| `SAVEPOINT`       | Create savepoint      | `SAVEPOINT sp1;`      |
| `ROLLBACK TO`     | Rollback to savepoint | `ROLLBACK TO sp1;`    |
| `\set AUTOCOMMIT` | Set autocommit mode   | `\set AUTOCOMMIT off` |

## System and Maintenance Commands

| Command          | Description                | Example Usage                               |
| ---------------- | -------------------------- | ------------------------------------------- |
| `pg_ctl start`   | Start PostgreSQL service   | `pg_ctl -D /usr/local/var/postgres start`   |
| `pg_ctl stop`    | Stop PostgreSQL service    | `pg_ctl -D /usr/local/var/postgres stop`    |
| `pg_ctl restart` | Restart PostgreSQL service | `pg_ctl -D /usr/local/var/postgres restart` |
| `pg_ctl status`  | Check service status       | `pg_ctl -D /usr/local/var/postgres status`  |
| `VACUUM`         | Clean up database          | `VACUUM ANALYZE users;`                     |
| `REINDEX`        | Rebuild indexes            | `REINDEX TABLE users;`                      |
| `ANALYZE`        | Update table statistics    | `ANALYZE users;`                            |

## Monitoring and Performance

| Command                          | Description                  | Example Usage                          |
| -------------------------------- | ---------------------------- | -------------------------------------- |
| `SELECT version()`               | Show PostgreSQL version      | `SELECT version();`                    |
| `SHOW`                           | Show configuration parameter | `SHOW max_connections;`                |
| `\dS`                            | List system tables           | `\dS`                                  |
| `SELECT * FROM pg_stat_activity` | Show active connections      | `SELECT * FROM pg_stat_activity;`      |
| `SELECT * FROM pg_stat_database` | Show database statistics     | `SELECT * FROM pg_stat_database;`      |
| `EXPLAIN`                        | Show query execution plan    | `EXPLAIN SELECT * FROM users;`         |
| `EXPLAIN ANALYZE`                | Show actual execution stats  | `EXPLAIN ANALYZE SELECT * FROM users;` |

## Advanced Features

| Command      | Description                      | Example Usage             |
| ------------ | -------------------------------- | ------------------------- |
| `\ef`        | Edit function in editor          | `\ef function_name`       |
| `\ev`        | Edit view in editor              | `\ev view_name`           |
| `\sf`        | Show function definition         | `\sf function_name`       |
| `\sv`        | Show view definition             | `\sv view_name`           |
| `\i`         | Execute commands from file       | `\i script.sql`           |
| `\ir`        | Execute file relative to current | `\ir ../scripts/init.sql` |
| `\! command` | Execute shell command            | `\! ls -la`               |
| `\cd`        | Change directory                 | `\cd /tmp`                |

## Connection Options

| Flag                | Description                   |
| ------------------- | ----------------------------- |
| `-h hostname`       | Database server host          |
| `-p port`           | Database server port          |
| `-U username`       | Database username             |
| `-d database`       | Database name                 |
| `-W`                | Force password prompt         |
| `-w`                | Never prompt for password     |
| `-f filename`       | Execute commands from file    |
| `-c command`        | Execute single command        |
| `-l`                | List databases and exit       |
| `-v variable=value` | Set psql variable             |
| `-X`                | Do not read startup file      |
| `-q`                | Quiet mode                    |
| `-1`                | Execute as single transaction |

## Environment Variables

- **PGHOST** - Default host
- **PGPORT** - Default port  
- **PGUSER** - Default username
- **PGDATABASE** - Default database
- **PGPASSWORD** - Default password (not recommended)
- **PGPASSFILE** - Password file location