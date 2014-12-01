<?php
	function dirTree($dir) {
    $d = dir($dir);
    while (false !== ($entry = $d->read())) {
        if($entry != '.' && $entry != '..' && is_dir($dir.$entry))
            $arDir[$entry] = dirTree($dir.$entry.'/');
    }
    $d->close();
    return $arDir;
}

function printTree($array, $level=0) {
    foreach($array as $key => $value) {
        echo "<div class='dir' style='width: ".($level*20)."px;'>&nbsp;</div>".$key."<br/>\n";
        if(is_array($value))
            printTree($value, $level+1);
    }
}

$dir = "/var/www/tasks";
$arDirTree = dirTree($dir);
printTree($arDirTree);
?>