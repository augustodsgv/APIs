CREATE TABLE tasks(
    task_id serial PRIMARY KEY,
    task_name VARCHAR (50) NOT NULL,
    is_done BOOLEAN NOT NULL
);

CREATE TABLE tags(
    tag_id serial PRIMARY KEY,
    tag_name VARCHAR (50) NOT NULL,
    task_id serial,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);