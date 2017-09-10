
$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('nav').addClass('scroll');

  } else {
    $('nav').removeClass('scroll');
    $('#no-active').removeClass('active');
 }
});


function minname(){
    var value=$("#usr").val();
     var pass2 = document.getElementById('usr');
    var message = document.getElementById('confirmMessage2');
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    if(value.length>=3){

                pass2.style.backgroundColor=goodColor;
        message.innerHTML="Verified!";
         message.style.color = goodColor;
    }
    else if(value.length<3){
        pass2.style.backgroundColor=badColor;
        message.innerHTML="Enter Min. 3 Alphabets!";
         message.style.color = badColor;
    }
}
          
          function minpass(){
    var value=$("#pwd").val();
     var pass2 = document.getElementById('pwd');
    var message = document.getElementById('confirmMessage3');
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    if(value.length>=6){

                pass2.style.backgroundColor=goodColor;
        message.innerHTML="Verified!";
         message.style.color = goodColor;
    }
    else if(value.length<3){
        pass2.style.backgroundColor=badColor;
        message.innerHTML="Enter Min. 6 Alphabets!";
         message.style.color = badColor;
    }
}
      	
function checkPass()
{
    //Store the password field objects into variables ...
    var pass1 = document.getElementById('pwd');
    var pass2 = document.getElementById('pwd2');
    //Store the Confimation Message Object ...
    var message = document.getElementById('confirmMessage');
    //Set the colors we will be using ...
    var goodColor = "#66cc66";
    var badColor = "#ff6666";
    //Compare the values in the password field 
    //and the confirmation field
    if(pass1.value == pass2.value){
        //The passwords match. 
        //Set the color to the good color and inform
        //the user that they have entered the correct password 
        pass2.style.backgroundColor = goodColor;
        message.style.color = goodColor;
        message.innerHTML = "Passwords Match!"
    }else{
        //The passwords do not match.
        //Set the color to the bad color and
        //notify the user.
        pass2.style.backgroundColor = badColor;
        message.style.color = badColor;
        message.innerHTML = "Passwords Do Not Match!"
    }
}  

