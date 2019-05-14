drop table if exists cba.documents_bk2;
create table cba.documents_bk2 as  select * from cba.documents;
