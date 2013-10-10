CREATE KEYSPACE duke
    WITH REPLICATION = { 'class':'SimpleStrategy', 'replication_factor': 2 };

USE duke;

CREATE TABLE safety_dance (
    url varchar PRIMARY KEY,
    hostname varchar,
    port int,
    path varchar,
    status varchar,
    reason text
);

INSERT INTO safety_dance (url, hostname, port, path, status, reason)
    VALUES ('curtis.lassam.net:80/', 'curtis.lassam.net', 80, '', 'SAFE', 'by fiat');

INSERT INTO safety_dance (url, hostname, port, path, status, reason)
    VALUES ('curtis.lassam.net:80/index.html', 'curtis.lassam.net', 80, 'index.html', 'SAFE', 'by fiat');

INSERT INTO safety_dance (url, hostname, port, path, status, reason)
    VALUES ('evil.ru:1001/index.html', 'evil.ru', 1001, 'index.html', 'NOPE', 'do not go here');

INSERT INTO safety_dance (url, hostname, port, path, status, reason)
    VALUES ('example.org:80/', 'example.org', 80, '', 'WARN', 'these guys are shady');
