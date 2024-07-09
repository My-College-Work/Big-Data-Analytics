import re

# Read the MySQL dump file
with open('test.sql', 'r') as file:
    data = file.read()

# Define the type mapping between MySQL and PostgreSQL
type_mapping = {
    'INT': 'INTEGER',
    'TINYINT(1)': 'BOOLEAN',
    'VARCHAR': 'VARCHAR',
    'TEXT': 'TEXT',
    'DATE': 'DATE',
    'TIME': 'TIME',
    'DATETIME': 'TIMESTAMP',
    'TIMESTAMP': 'TIMESTAMP',
    'DECIMAL': 'NUMERIC',
    'DOUBLE': 'DOUBLE PRECISION',
    'FLOAT': 'REAL',
    'BLOB': 'BYTEA'
}

# Replace MySQL data types with PostgreSQL data types
for mysql_type, pg_type in type_mapping.items():
    data = re.sub(r'\b' + mysql_type + r'\b', pg_type, data)

# Remove backticks
data = re.sub(r'`', '', data)

# Replace AUTO_INCREMENT with SERIAL
data = re.sub(r'\bAUTO_INCREMENT\b', 'SERIAL', data)

# Handle character sets and collations (PostgreSQL does not use these in the same way)
data = re.sub(r' CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci', '', data)
data = re.sub(r' DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci', '', data)
data = re.sub(r' DEFAULT CHARSET=utf8mb4', '', data)
data = re.sub(r' COLLATE utf8mb4_0900_ai_ci', '', data)

# Handle CURRENT_TIMESTAMP
data = re.sub(r'\bDEFAULT CURRENT_TIMESTAMP\b', 'DEFAULT NOW()', data)

# Handle unique key constraints
data = re.sub(r'UNIQUE KEY', 'UNIQUE', data)

# Handle table options
data = re.sub(r'ENGINE=InnoDB', '', data)
data = re.sub(r'DEFAULT ENCRYPTION=\'N\'', '', data)

# Handle comments and directives specific to MySQL
data = re.sub(r'/\*!.*\*/;', '', data)
data = re.sub(r'--.*\n', '', data)

# Remove USE database statement
data = re.sub(r'\bUSE\b \S+;', '', data)

# Remove LOCK TABLES and UNLOCK TABLES statements
data = re.sub(r'LOCK TABLES .*?;', '', data)
data = re.sub(r'UNLOCK TABLES;', '', data)

# Write the modified data to a new PostgreSQL-compatible SQL file
with open('modified_test.sql', 'w') as file:
    file.write(data)
