

// Form validation(all fileds must be filled)
function validateForm() {
  let name = document.forms["myForm"]["name"].value;
  if (name == "") {
    alert("Name must be filled out");
    return false;
  }
  let age = document.forms["myForm"]["age"].value;
  if (age == "") {
    alert("Age must be filled out");
    return false;
  }
  let weight = document.forms["myForm"]["weight"].value;
  if (weight == "") {
    alert("Weight must be filled out");
    return false;
  }
  let height = document.forms["myForm"]["height"].value;
  if (height == "") {
    alert("Height must be filled out");
    return false;
  }
} 

// function dropList() {
//   var mylist = document.getElementById("myList");
//   document.getElementById("gender").value = mylist.options[mylist.selectedIndex].text;}

// BMI (Body Mass Index)
const  button = document.getElementById("btn");

button.addEventListener("click", () => {
  
  let height = parseInt(document.getElementById("height").value);
  let weight = parseInt(document.getElementById("weight").value);
  let results = document.getElementById("bmiResult");

  
  let bmi = weight / ((height * height)/10000);
  bmi = bmi.toFixed(2);

 document.getElementById('bmiResult').innerHTML = bmi;

 let status = "";

  if (bmi < 18.5) {
    status = "Underweight";
  }
  else if (bmi < 25) {
    status = "Normal";
  }
  else if (bmi < 30) {
    status = "Overweight";
  }
  else if (bmi>= 31) {
    status = "Obese";
  }
  else {
    status = "Wrong entry,try again please";
  }
  document.getElementById('status').innerHTML = status;
  
});


