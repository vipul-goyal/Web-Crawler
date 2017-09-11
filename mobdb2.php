<?php
if(isset($_POST['username']) && isset($_POST['password'])){

    $uname = "vipul"; // db username
$pass = "vipul";  // db pass
$dbName = "news";// db name
    $username = ($_POST['username']);
    $password = ($_POST['password']);
    $con = new MongoClient("mongodb://".$uname.":".$pass."@ds135812.mlab.com:35812/news");
    echo $con; 
    // Select Database
    if($con){
        $db = $con->selectDB($dbName);
        echo $db;
        // Select Collection
        $collection = $db->loginDetails;   // you may use 'admin' instead of 'Admin'
        $qry = array("username" => $username, "password" => $password);
        $result = $collection->findOne($qry);

        if(!empty($result)){
            header("Location:welcome.php");
            exit;
        }else{
            echo "Wrong combination of username and password";
        }
    }
    else{
        die("Mongo DB not connected!");
    }
}
?>

<html>
<head>
<title> Login</title>
</head>
<body>
<form action="" method="POST">
User Name:
 <input type="text" id="username" name="username" required />
 Password:
  <input type="password" id="password" name="password" required/>
<input name="submit" id="submit" type="submit" value="Login" />
</form>
</body>
</html>