let person = {
  name: "Hasan",
  age: 25,
  city: "Khulna",
};



for (let key in person) {
  document.write("<br>" + key + ":" + person[key]);
}
