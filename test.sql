select * from tbl_vw_user where telephone = '13783783183';
update  tbl_vw_user  set expert_level = 1,unlock_medal=1 where telephone in (
'17000000011',
'17000000012',
'17000000013',
'17000000021',
'17000000022',
'17000000027'
);

select  expert_level,unlock_medal from tbl_vw_user    where telephone in (
'17000000011',
'17000000012',
'17000000013',
'17000000021',
'17000000022',
'17000000027'
);

update  tbl_vw_user  set expert_level = 4,unlock_medal=1 where telephone = '13516852872'