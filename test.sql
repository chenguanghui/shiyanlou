CREATE TABLE files(id int(10) auto_increment, title VARCHAR(80) unique, created_time DATETIME, category_id INT(10), content Text, primary key (id), constraint fk_categories foreign key (category_id) references categories(id))
CREATE TABLE categories(id int(10) auto_increment, name VARCHAR(80), primary key (id));



