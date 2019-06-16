<?php
include("config.php");
include('class/userClass.php');
$userClass = new userClass();

$errorMsgReg='';
$errorMsgLogin='';

/* formulario de registro */
if (!empty($_POST['signupSubmit'])) 
{
$username=$_POST['usernameReg'];
$email=$_POST['emailReg'];
$password=$_POST['passwordReg'];
$name=$_POST['nameReg'];
// Regular expression check 
$username_check = preg_match('~^[A-Za-z0-9_]{3,20}$~i', $username);
$email_check = preg_match('~^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+.([a-zA-Z]{2,4})$~i', $email);
$password_check = preg_match('~^[A-Za-z0-9!@#$%^&*()_]{6,20}$~i', $password);

if($username_check && $email_check && $password_check && strlen(trim($name))>0) 
{
$uid=$userClass->userRegistration($username,$password,$email,$name);
if($uid)
{
$url=BASE_URL.'index.php';
header("Location: $url"); // redirigiendo a home.php
}
else
{
$errorMsgReg="El usuario ya existe.";
}
}
}
?>
<link rel="stylesheet" type="text/css" href="style/style.css">
<script src="js/form.js"></script>

<form method="post" action="" name="signup">
<div class="login-form">
     <h1>registrate</h1>
     <div class="form-group ">
       <input type="text" class="form-control" name="nameReg" placeholder="nombre" autocomplete="off" id="UserName" />
       <i class="fa fa-user"></i>
     </div>
     <div class="form-group ">
       <input type="text" class="form-control" name="emailReg" placeholder="correo" autocomplete="off" id="UserName" />
       <i class="fa fa-user"></i>
     </div>
     <div class="form-group ">
       <input type="text" class="form-control" name="usernameReg" placeholder="Usuario" autocomplete="off" id="UserName"/>
       <i class="fa fa-user"></i>
     </div>
     <div class="form-group log-status">
       <input type="password" class="form-control" name="passwordReg" placeholder="password" id="Password"  autocomplete="off"/>
       <i class="fa fa-lock"></i>
     </div>
      <div class="errorMsg"><?php echo $errorMsgReg; ?></div>
	 <input type="submit" class="log-btn" name="signupSubmit" value="Signup">
   </div>
 </form>