CREATE KEYSPACE duke
    WITH REPLICATION = { 'class':'SimpleStrategy', 'replication_factor': 1 };

USE duke;

CREATE TABLE safety_dance (
    url varchar PRIMARY KEY,
    status varchar,
    reason text
);

INSERT INTO safety_dance (url, status, reason)
    VALUES ('http://curtis.lassam.net', 'SAFE', 'by fiat');

INSERT INTO safety_dance (url, status, reason)
    VALUES ('http://evil.ru', 'NOPE', 'not safe.');

INSERT INTO safety_dance (url, status, reason)
    VALUES('http://unsure.maybe', 'WARN', 'safe for now, I guess');
