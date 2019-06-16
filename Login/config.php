<?php
/*inicio de una sesion*/
session_start();

/*configuracion de datos de la base de datos*/
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD', '');
define('DB_DATABASE', 'proyecto');
define("BASE_URL", "http://localhost/proyecto/"); 

function getDB() 
{
	/*asignacion de datos a la variables*/
$dbhost=DB_SERVER;
$dbuser=DB_USERNAME;
$dbpass=DB_PASSWORD;
$dbname=DB_DATABASE;
try {
/*conexion a la base de datos a traves de PDO*/	
$dbConnection = new PDO("mysql:host=$dbhost;dbname=$dbname", $dbuser, $dbpass); 
$dbConnection->exec("set names utf8");
$dbConnection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
return $dbConnection;
}
/*En caso de que no se conecte a la base de datos mostrar un fallo por pantalla*/
catch (PDOException $e) {
echo 'Conexion fallida: ' . $e->getMessage();
}

}
?>