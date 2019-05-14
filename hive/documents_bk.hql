drop table if exists cba.documents_bk;
create table cba.documents_bk as  select * from cba.documents;
