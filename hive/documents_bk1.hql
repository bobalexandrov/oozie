drop table if exists share_catdiim01_dev7_stage_g0070.documents_bk1;
create table share_catdiim01_dev7_stage_g0070.documents_bk1 as  select * from share_catdiim01_dev7_stage_g0070.documents;
