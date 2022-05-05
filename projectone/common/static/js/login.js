function vallogin(){
    var name = document.login.name.value;
    var password = document.login.password.value;
    if(name==null || name==""){
        alert("this field can't be blank")
        return false
    }
    
        else if(password==null || password==""){
        alert("this field can't be blank")
        return false
    }

    
}