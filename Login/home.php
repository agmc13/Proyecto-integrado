<?php
include('config.php');
include('session.php');
$userDetails=$userClass->userDetails($session_uid);
?>

<h1>Bienvenido <?php echo $userDetails->name; ?></h1>
<h4><a href="<?php echo BASE_URL; ?>logout.php">Logout</a></h4>

<?php
exec('C:\Python37\python.exe C:\Users\Alfonso\Desktop\proyecto_integrado\proyecto.py');
?>