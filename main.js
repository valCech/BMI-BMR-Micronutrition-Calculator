//alert('Welcome to Val\'s project');
var fname = document.getElementById("fname").value;
var at = document.getElementById("name").value;
var age = document.getElementById("age").value;
var fname = document.getElementById("height").value;
var fname = document.getElementById("height").value;
submitOK = "true";

if (fname == "") {  
    alert("Please enter your first name");
    submitOK = "false";

if (isNaN(age) || age < 1 || age > 100) {
  alert("The age must be a number between 1 and 100");
  submitOK = "false";
}

if (at == -1) {
  // alert("Not a valid e-mail!");
  submitOK = "false";
}

if (submitOK == "false") {
  alert("Please fix the above errors and try again");
}}

function dropList() {
  var mylist = document.getElementById("myList");
  document.getElementById("gender").value = mylist.options[mylist.selectedIndex].text;}