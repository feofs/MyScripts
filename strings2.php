<?
$string="&nbsp&nbsp&nbspsimple text&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp";
#������� ������ � ������ ������
echo ltrim($string);
echo "<br>";
echo chop($string);
echo "<br>";
$abzac="\n\n\n";
echo "������� \\n �� \<br\> � ������� ��� ������ ����� ���� ������";
$abzac=nl2br($abzac);
echo $abzac;

print("Hello world<br>");
$total=3.14;
echo gettype($total);
echo "<br>";
#��� printf ���� ���� ������������, ������� � �������� �������� ��� ����� ������
#%[�����-�� ������][-][������].[��������][���]
#% - � ��� �������
#�����-�� ������ - ������ ����������� �� ��������� �����
#- ������ ����� ������������� �� ������ ���� � �� �������
# �������� - ���-�� ������ ����� �������
$total=3.1422;
echo printf("The total amount is %.4f<br>",$total);
echo printf("The total emount s zapolnitelem %'*10.3f",$total);
echo "<br>";
echo printf("Chislo v 16 richnim vide : %.X",$chislo);
echo "<br>";
echo printf("Chislo v desyatichnom vide %.d",$chislo);
echo "<br>";
echo "-------------Razlichue ���������� ���� � ��������---------------<br>";
$string="This is string of UPPER and lower";
if (!isset($name) && !isset($surname))
{
	echo "��� ����� ����������<br>";
	}
$find="b";
switch ($find)
{
case "a":
	echo "By the internet";
	break;
case "b":
	echo "By the TV";
	break;
	}
echo "<br>---------------ucfirst,ucwords,strtolower,strtoupper-----------------<br>";
$string="hello wrold is we can";
echo ucfirst($string)."<br>";
#������ � python str.capitalize() - ��� str - ��� str ������-������
echo ucwords($string)."<br>";
#������ � python str.titled() 
echo strtolower($string)."<br>";
#������ � python str.lower()
echo strtoupper($string)."<br>";
#������ � python str.upper()
#���� ��� � python ������ ������� ���� ����� ���
#str.join
#
#
#
#

$slashes='This string \ is now " and %';
$with_slashes=AddSlashes($slashes);
echo $with_slashes."<br>";

echo StripSlashes($with_slashes)."<br>";

$email='user@mail@domain';
$arr=explode('@',$email);
echo $arr[0]."|".$arr[1]."|".$arr[2]."<br>";
#�������� ������ �� �������
$str=implode('@',$arr);


?>