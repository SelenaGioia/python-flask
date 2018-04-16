create table users
(
  id       int auto_increment
    primary key,
  username varchar(50)  not null,
  password varchar(50)  null,
  fullname varchar(100) null,
  constraint users_username_uindex
  unique (username)
)
  engine = InnoDB;

create table alarms
(
  id      int auto_increment
    primary key,
  user_id int  not null,
  hour    time not null,
  constraint alarms_users_id_fk
  foreign key (user_id) references users (id)
)
  engine = InnoDB;

create index alarms_users_id_fk
  on alarms (user_id);


