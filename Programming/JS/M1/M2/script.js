// // let john = { name: "John", age: 25 };
// // let pete = { name: "Pete", age: 30 };
// // let mary = { name: "Mary", age: 28 };

// // let users = [john, pete, mary];

// // let names = users.map(user => user.name);

// // console.log(names); // John, Pete, 

// let john = { name: "John", surname: "Smith", id: 1 };
// let pete = { name: "Pete", surname: "Hunt", id: 2 };
// let mary = { name: "Mary", surname: "Key", id: 3 };

// let users = [john, pete, mary];

// let usersMapped = users.map(user => {
//     let fullName = user.name + " " + user.surname;
//     let id = user.id;
//     return { fullName, id };
// })

// /*
// usersMapped = [
//   { fullName: "John Smith", id: 1 },
//   { fullName: "Pete Hunt", id: 2 },
//   { fullName: "Mary Key", id: 3 }
// ]
// */

// console.log(usersMapped[0].id) // 1
// console.log(usersMapped[0].fullName) // John Smith
let john = { name: "John", age: 25 };
let pete = { name: "Pete", age: 30 };
let mary = { name: "Mary", age: 28 };
let arr = [pete, john, mary];
function sortByAge(arr) {
    return arr.sort((a, b) => a.age > b.age ? 1 : -1);
}
console.log(sortByAge(arr));
function getAverageAge(arr) {
    return arr.reduce((sum, user) => sum + user.age, 0) / arr.length;
}
console.log(getAverageAge(arr));

function makeCounter() {
    let count = 0;

    return function () {
        return count++;
    };
}

let counter = makeCounter();
let counter2 = makeCounter();

console.log(counter()); // 0
console.log(counter()); // 1

console.log(counter2()); // ?
console.log(counter2());

function sum(a) {
    return function (b) {
        return a + b;
    }
}
console.log(sum(1)(2));

function makeArmy() {
    let shooters = [];

    let i = 0;
    let j = 0;
    while (i < 10) {
        let shooter = function () { // create a shooter function,

            console.log(j); // that should show its number
            j++;
        };
        shooters.push(shooter); // and add it to the array
        i++;
    }

    // ...and return the array of shooters
    return shooters;
}

let army = makeArmy();

// all shooters show 10 instead of their numbers 0, 1, 2, 3...
army[0](); // 10 from the shooter number 0
army[1](); // 10 from the shooter number 1
army[2](); // 10 ...and so on.