<?php
include("config.php");
include('class/userClass.php');
$userClass = new userClass();

$errorMsgReg='';
$errorMsgLogin='';
/* Login Form */
if (!empty($_POST['loginSubmit'])) 
{
$usernameEmail=$_POST['usernameEmail'];
$password=$_POST['password'];
if(strlen(trim($usernameEmail))>1 && strlen(trim($password))>1 )
{
$uid=$userClass->userLogin($usernameEmail,$password);
if($uid)
{
$url=BASE_URL.'home.php';
header("Location: $url"); // redireccion a la pagina home.php
}
else
{
$errorMsgLogin="usuario o contraseña incorrecto.";
}
}
}

?>
<link rel="stylesheet" type="text/css" href="style/style.css">
<script src="js/form.js"></script>
<form method="post" action="" name="login">
<div class="login-form">
     <h1>detencion de personas</h1>
     <div class="form-group ">
       <input type="text" class="form-control" name="usernameEmail" placeholder="Usuario" autocomplete="off" id="UserName"/>
       <i class="fa fa-user"></i>
     </div>
     <div class="form-group log-status">
       <input type="password" class="form-control" placeholder="Password" id="Passwod" name="password" autocomplete="off"/>
       <i class="fa fa-lock"></i>
     </div>
      <div class="errorMsg"><?php echo $errorMsgLogin; ?></div>
      <a class="link" href="registro.php">registrate</a>
     <input type="submit" class="log-btn" name="loginSubmit" value="Login">
   </div>
</form>


