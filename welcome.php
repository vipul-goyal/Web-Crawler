<?php
$uname = "vipul"; // db username
$pass = "vipul";  // db pass
$dbName = "news";// db name

$uri =  "mongodb://".$uname.":".$pass."@ds135812.mlab.com:35812/news";
$collection = "newsdata";

// create connection to mongodb
$conn = new MongoClient($uri);

$db = $conn->selectDB($dbName);

$col = new MongoCollection($db,$collection); //1st param id db,2nd param is collection

$cur = $col->find(); 

foreach ($cur as $doc) {
	echo 'url :';
	echo ($doc['url']);
	echo  nl2br ("\n");
	echo 'Text :';
	echo ($doc['All_text']);
	echo  nl2br ("\n");
	echo  nl2br ("\n");
	} 
?>