alert('Welcome to Val\'s project');
var fname = document.getElementById("fname").value;
var age = document.getElementById("age").value;
var height = document.getElementById("height").value;
var weight = document.getElementById("weight").value;
var gender = document.querySelector("#gender").value

// Form validation(all fileds must be filled)
function validateForm() {
  let name = document.forms["myForm"]["name"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
  let age = document.forms["myForm"]["age"].value;
  if (x == "") {
    alert("Age must be filled out");
    return false;
  }
  let weight = document.forms["myForm"]["weight"].value;
  if (x == "") {
    alert("Weight must be filled out");
    return false;
  }
  let height = document.forms["myForm"]["height"].value;
  if (x == "") {
    alert("Height must be filled out");
    return false;
  }
} 

// function dropList() {
//   var mylist = document.getElementById("myList");
//   document.getElementById("gender").value = mylist.options[mylist.selectedIndex].text;}

// // BMI (Body Mass Index)
// var bmi = weight / ((height/100)**2);
// BMI1 = round(BMI, 1)
//   alert("Your BMI is " + BMI1);
// if (BMI1 < 18.5) {
//   alert("You are underweight");
// }
// else if (BMI1 >= 18.5 && BMI1 < 25) {
//   alert("You are normal");
// } 
// else if (BMI1 >= 25 && BMI1 < 30) {
//   alert("You are overweight");
// }
// else if (BMI1 >= 30) {
//   alert("You are obese");
// }}
