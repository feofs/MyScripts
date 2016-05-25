<?
$string="&nbsp&nbsp&nbspsimple text&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp";
#удаляет пробелі в начале строки
echo ltrim($string);
echo "<br>";
echo chop($string);
echo "<br>";
$abzac="\n\n\n";
echo "Заменим \\n на \<br\> и получим три абзаца после єтой строки";
$abzac=nl2br($abzac);
echo $abzac;

print("Hello world<br>");
$total=3.14;
echo gettype($total);
echo "<br>";
#Для printf есть своя спецификация, которая в принципе подходит для любых языков
#%[допол-ий символ][-][ширина].[точность][тип]
#% - и так понятен
#допол-ий символ - символ заполнитель до указанной ширині
#- данные будут выравниваться по левому краю а не правому
# точность - кол-во знаков после запятой
$total=3.1422;
echo printf("The total amount is %.4f<br>",$total);
echo printf("The total emount s zapolnitelem %'*10.3f",$total);
echo "<br>";
echo printf("Chislo v 16 richnim vide : %.X",$chislo);
echo "<br>";
echo printf("Chislo v desyatichnom vide %.d",$chislo);
echo "<br>";
echo "-------------Razlichue возведения букв в регистры---------------<br>";
$string="This is string of UPPER and lower";
if (!isset($name) && !isset($surname))
{
	echo "Нет таких переменных<br>";
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
#аналог в python str.capitalize() - где str - где str объект-строка
echo ucwords($string)."<br>";
#аналог в python str.titled() 
echo strtolower($string)."<br>";
#аналог в python str.lower()
echo strtoupper($string)."<br>";
#аналог в python str.upper()
#Есть еще в python другие полезніе вещи такие как
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
#Собирает строку из массива
$str=implode('@',$arr);


?>