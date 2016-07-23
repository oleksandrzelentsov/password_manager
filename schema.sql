create table if not exists service (
    serviceid integer not null primary key,
    servicename text not null,
    serviceurl text,
    serviceinfo text
);


create table if not exists location (
    locationid integer not null primary key,
    locationservice integer not null,
    locationlogin text not null,
    locationinfo text,
    foreign key(locationservice) references service(serviceid)
);

create table if not exists password (
    passwordid integer not null primary key,
    passwordlocation integer not null,
    password text not null,
    foreign key(passwordlocation) references location(locationid)
);

