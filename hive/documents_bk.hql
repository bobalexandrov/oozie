drop table if exists share_catdiim01_dev7_stage_g0070.documents_bk;
create table share_catdiim01_dev7_stage_g0070.documents_bk as  select * from share_catdiim01_dev7_stage_g0070.documents;
