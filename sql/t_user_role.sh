#db config
set encoding=utf-8

while read line;do
    eval "$line"
done < ./config.sh

#table config
table_sum=1
table_base_name="t_user_role"

mycmd="mysql -h$host -u$username -p$password -P$port --default-character-set=utf8mb4"
for i in seq 1 $table_sum;
do
table_index=expr $i - 1
table_name=${table_base_name}_$table_index
if [ $table_sum -eq 1 ];then
	table_name=$table_base_name
fi

$mycmd -e "drop table if exists $db.$table_name;"
sql="
create table $db.$table_name (
  F_id                  int(11)                                   NOT NULL AUTO_INCREMENT,
  F_user_account        varchar(64)   COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT ''  COMMENT '用户账号',
  F_role_code           varchar(64)   COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT ''  COMMENT '组织代码',
  F_remark              text          COLLATE utf8mb4_unicode_ci  NOT NULL             COMMENT '备注',
  F_deleted             bool          COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT  false COMMENT '路径是否展示 enum:true,display,YES#1,flase,NO',
  F_operator            varchar(32)   COLLATE utf8mb4_unicode_ci  NOT NULL DEFAULT ''  COMMENT '操作员',
  F_create_time         bigint(20)                                NOT NULL DEFAULT '0' COMMENT '创建时间戳 单位秒',
  F_modify_time         bigint(20)                                NOT NULL DEFAULT '0' COMMENT '更新时间戳 单位秒',
  PRIMARY KEY (F_id) USING BTREE,
  UNIQUE KEY ${table_name}_F_role_code (F_role_code),
  INDEX ${table_name}_modify_time (F_modify_time)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户角色关联表';
"

$mycmd -e "$sql"
echo "table: $table_name create success!"
done