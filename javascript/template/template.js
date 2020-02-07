// function Animal(name) {
// 	this.name = name
// 	console.log(this)
// }

// Animal.prototype = {
// 	get owner() {
// 		return 'richard'
// 	},

// 	set owner(ownerName) {
// 		this._owner = ownerName;
// 	}
// }

// someAnimal = new Animal('sekar');
// // someAnimal.owner = 'richard';
// console.log(someAnimal.constructor);
// console.log(someAnimal.owner);
// console.log(someAnimal.name);
// // console.log(someAnimal.owner);

// const Person = class {
// 	constructor(name, age=22) {
//     this.name = name;
//     this.age = age;
// 	}

//   display() {
//     console.log("The name is " + this.name);
//     console.log("The age is " + this.age);
//   }
// }

// class Circle {

// }

// let sekar = new Person('Sekardayu Hana Pradiani');
// console.log(Person);
// console.log(typeof Person);
// console.log(Animal)
// console.log(typeof Animal);
// sekar.display();
// console.log(sekar.name);

someList = [1, 2, 3, 4];
console.log(someList.map(el => el**2));
console.log(someList);