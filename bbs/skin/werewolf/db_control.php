<?
	// register_globals�� off�� ���� ���� ���� ������
	@extract($HTTP_SERVER_VARS);
	@extract($HTTP_ENV_VARS);

	// ���κ��� ���̺귯�� ������
	$_zb_path = realpath("../../")."/";
	include $_zb_path."lib.php";

	// DB �������� ������
	$connect = dbConn();

	// Į�� �߰�
	$instant_data = 
	"INSERT INTO `zetyx_board_werewolf_rule` (`no`, `name`, `min_player`, `max_player`) VALUES (5, '�ν���Ʈ', 7, 8);";
	
	
	@mysql_query($instant_data, $connect) or Error("subrule ������ ���� ����", "");
	
	mysql_close($connect);
?>