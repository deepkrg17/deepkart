function openNav() {
  document.getElementById("sideNav").style.width = "250px";
}

function closeNav() {
  document.getElementById("sideNav").style.width = "0";
}

function toProd(a){
    window.location.assign(`/prodview/33375278${a}`);
}