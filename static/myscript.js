function pad(n, width, z) {
  z = z || '0';
  n = n + '';
  return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function getDecenas(value){
  unidades = (value % 10)
  return Math.floor(value/10);
}

function getUnidades(value){
  unidades = (value % 10)
  return (unidades == 0)? 1: unidades;
}

var output1 = document.getElementById("demo1");

output1.innerHTML = slider1.value;
var decenas = getDecenas(slider1.value)
var unidades = getUnidades(slider1.value)
slider1.oninput = function() {
  decenas = getDecenas(slider1.value)
  unidades = getUnidades(slider1.value)
  <!--output1.innerHTML = numberWithCommas(Math.pow(10,decenas)*unidades);-->
}

slider1.onmouseup = function () {
  document.getElementById("myform").submit();
}

var output2 = document.getElementById("demo2");

output2.innerHTML = slider2.value;
var decenas = getDecenas(slider2.value)
var unidades = getUnidades(slider2.value)
slider2.oninput = function() {
  decenas = getDecenas(slider2.value)
  unidades = getUnidades(slider2.value)
  <!--output2.innerHTML = numberWithCommas(Math.pow(10,decenas)*unidades);-->
}

slider2.onmouseup = function () {
  document.getElementById("myform").submit();
}


var output3 = document.getElementById("demo3");

output3.innerHTML = slider3.value;
var decenas = getDecenas(slider3.value)
var unidades = getUnidades(slider3.value)
slider3.oninput = function() {
  decenas = getDecenas(slider3.value)
  unidades = getUnidades(slider3.value)
  <!--output3.innerHTML = numberWithCommas(Math.pow(10,decenas)*unidades);-->
}

slider3.onmouseup = function () {
  document.getElementById("myform").submit();
}
