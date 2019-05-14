drop table if exists cba.documents_bk3;
create table cba.documents_bk3 as  select * from cba.documents;
