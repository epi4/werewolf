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
	"update `zetyx_board_werewolf_entry` set comment = '1' where no = 5887 or no = 5888";
	
	
	@mysql_query($instant_data, $connect) or Error("subrule ������ ���� ����", "");
	
	mysql_close($connect);
?>