<?
	// register_globals�� off�� ���� ���� ���� ������
	@extract($HTTP_SERVER_VARS);
	@extract($HTTP_ENV_VARS);

	// ���κ��� ���̺귯�� ������
	$_zb_path = realpath("../../")."/";
	include $_zb_path."lib.php";

	// DB �������� ������
    $connect = dbConn();
    
    #$gameinfo_add_mustkill = 
    #"ALTER TABLE `zetyx_board_werewolf_truecharacter` DROP `mustkill`";
    #"ALTER TABLE `zetyx_board_werewolf_truecharacter` ADD `mustkill` int(1) unsigned NOT NULL DEFAULT 0;";
    #@mysql_query($gameinfo_add_mustkill, $connect) or Error("�ű� �÷� ���� ����", "");

    // Į�� �߰�
	#$insert_data = 
    #"INSERT INTO `zetyx_board_werewolf_truecharacter` 
    #(`no`, `race`, `wintype`, `character`, `secretchat`, `forecast`, 
    #`mediumism`, `assault`, `guard`, `telepathy`, `detect`, `revenge`, `half-assault`, 
    #`secretletter`, `double-vote`, `forecast-odd`, `assault-con`, `mustkill`) VALUES
    #(18, 1, 1, '��Ȥ�� �ζ�', 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    #(19, 0, 0, '���� ����', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);";
	
    #@mysql_query($insert_data, $connect) or Error("�ű� ���̺� ���� ����", "");

    // ������ Ȯ��
    #$mustkill_load =
    #"select * from `zetyx_board_werewolf_truecharacter`;";
	
	#$result = mysql_query($mustkill_load, $connect);

	#while($temp = mysql_fetch_array($result)) {
    #    echo $temp[no]." :: ".$temp['forecast-odd']." :: ".$temp['assault-con']." :: ".$temp['mustkill']."<br>";
    #}

    // ���̺� �߰�
	#$mustkill_schema = 
	#"CREATE TABLE `zetyx_board_werewolf_mustkill` (
	#`game` int(20) unsigned NOT NULL DEFAULT 0,
	#`day` tinyint(5) unsigned NOT NULL DEFAULT 0,
	#`target` int(20) unsigned NOT NULL DEFAULT 0
    #) ENGINE=MyISAM;";
    
    #@mysql_query($mustkill_schema, $connect) or Error("�ű� ���̺� mustkill ����� ����", "");;


    // ������ Ȯ��
	#$mustkill_schema_load = 
	#"select * from `zetyx_board_werewolf_mustkill`";
	
	#$result2 = mysql_query($mustkill_schema_load, $connect);
	#while($temp = mysql_fetch_array($result2)) {
	#	echo $temp[game]." :: ".$temp[day]." :: ".$temp[target]."<br>";
    #}
    
    #$rule_add_data = 
	#"INSERT INTO `zetyx_board_werewolf_rule` (`no`, `name`, `min_player`, `max_player`) VALUES (6, '����', 11, 16);";

	#@mysql_query($rule_add_data, $connect) or Error("����� ������ ���� ����", "");
	
	mysql_close($connect);
?>