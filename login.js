const loginFun = function(){
  // Retrieve username and password from HTML form
  let username = document.querySelector("#login_page [name='username']").value;
  let openPassword = document.querySelector("#login_page [name='password']").value;

  // let xhr = new XMLHttpRequest();
  // let url = "backend.py";

  // // Open connection to server
  // xhr.open("POST", url, true, username, openPassword);
  // // Set header
  // xhr.setRequestHeader("Content-Type", "application/json");
};

const registerFun = function(){
  // TODO: Link to registration page
  window.location.href = "https://www.google.com";
};

const init = function(){
  console.log("init");

  let loginBut = document.getElementById("login");
  loginBut.onclick = loginFun;

  let registerBut = document.getElementById("register");
  registerBut.onclick = registerFun;
};

window.addEventListener("load", init);