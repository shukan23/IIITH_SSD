function ValidateEmail() 
{
    email1 = document.getElementById("email").value;

 if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email1))
  {
    return (true);
  }
    alert("Invalid Email")
    return (false);
}

function clickHandler(event){
    if(ValidateEmail()){
        name1 = document.getElementById("mname").value;
        email1 = document.getElementById("email").value;
        uname1 = document.getElementById("uname").value;
        lname1 = document.getElementById("leader").value;

        alert(
            "Name: "+name1+
            "Email : " +email1+
            "Username" + uname1 +
            "Team Lead:" +  lname1 +
            "Team Members:"
        );
    }
    else{
        alert("Invalid Email");
    }
}
function nameHandler(){
    name1 = document.getElementById("uname").value;
    // console.log(name1);
   if(/[A-Z]/.test(name1)){
    if(/[1-9]/.test(name1)){
        document.getElementById("errorMessage").innerHTML ="";
    }
    else{
        document.getElementById("errorMessage").innerHTML = "Invalid Name";

    }
    }
    else{
        document.getElementById("errorMessage").innerHTML = "Invalid Name";

    }

}
function pwHandler(){
    pw1 = document.getElementById("ppw").value;
    pw2 = document.getElementById("cpw").value;
    if(pw1 == pw2){
        document.getElementById("pwmsg").innerHTML = "";
    }
    else{
        document.getElementById("pwmsg").innerHTML = "Not Matching";
    }
}