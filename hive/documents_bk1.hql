drop table if exists cba.documents_bk1;
create table cba.documents_bk1 as  select * from cba.documents;
