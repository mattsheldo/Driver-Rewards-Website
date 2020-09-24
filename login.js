const registerFun = function(){
  // Link to registration page
  window.location.href = "create/";
};

const init = function(){
  console.log("init");

  let registerBut = document.getElementById("register");
  registerBut.onclick = registerFun;
};

window.addEventListener("load", init);