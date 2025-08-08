let person = {
  name: "Hasan",
  age: 25,
  city: "Khulna",
};

for (let key in person) {
  document.write("<br>" + key + ":" + person[key]);
}

//.............................................automecly call this function
const api = (function () {
  const apiKey = "XXXOIJOIER665465SDD";
  return { apiKey };
})();
console.log("...................api..................");
console.log(api);
//.........................................................................

z = (x, y) => x * y;
console.log("...............short functoin............");
console.log(z(5, 10));

annonimas = function (a, b) {
  return a + b;
};
console.log("...................annonimas..................");
console.log(annonimas(5, 6));

function sum(a, b) {
  return a + b;
}
console.log("...................simple..................");
console.log(sum(2, 5));

//.................................................define functoin inside the own function

function factorial(n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log("...................recursive function.............");
console.log(factorial(5));

//...........................................same example for recursive function with loop
function factorial_loop(n) {
  var result = 1;
  for (i = 1; i <= n; i++) {
    result = result * i;
  }
  return result;
}
console.log(factorial_loop(5));
