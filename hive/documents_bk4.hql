drop table if exists cba.documents_bk4;
create table cba.documents_bk4 as  select * from cba.documents;
