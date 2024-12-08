let person = {
  name: "Hasan",
  age: 24,
  city: "Khulna",
};

for (let key in person) {
  document.write("<br>" + key + ":" + person[key]);
}
