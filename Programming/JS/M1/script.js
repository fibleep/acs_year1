console.log("debil debil");
let name = "Ilya";

console.log( `hello ${1}` ); // 1

console.log( `hello ${"name"}` ); // name

console.log( `hello ${name}` ); // Ilya

for(let i = 0; i<=7; i++){
console.log("#".repeat(i));
}
for(let i = 1; i < 100;i++){
    if(i%3==0 && i%5==0){
        console.log("FizzBuzz");
        continue;
    }
    if(i%3==0){
        console.log("Fizz");
        continue;
    }
    if(i%5==0){
        console.log("Buzz");
        continue;
    }
}

function chessboard(size){
    let result="";
for(let i = 0;i<size;i++){
    let iter = i;
    for(let a = 0;a<size;a++){
            if(iter%2==0){
                if(a%2==0){
                    result+=" ";
                }
                else{
                    result+="#";
                }
            }
            else{
                if(a%2==0){
                    result+="#";
                }
                else{
                    result+=" ";
                }
            }
    }
    result+="\n"; 
}
console.log(result);
}

chessboard(8);

//   const ask = (question,yes,no) =>{
//       if(confirm(question)) yes();
//       else no();
//   }
//   ask(
//     "Do you agree?",
//     function() { alert("You agreed."); },
//     function() { alert("You canceled the execution."); }
//   );

  function isEven(nr){
      if(nr%2==0){
          return true;
      }
      else{
          return false;
      }
  }
  console.log(isEven(50));
  console.log(isEven(75));
  console.log(isEven(-1));

function reverseArray(arr){
      const newArr=[];
      for(let i = arr.length;i>0;i--){
          newArr.push(arr[i-1]);
          console.log(arr[i-1] + " " + i-1);
      }
      console.log(newArr);
  }
  reverseArray(['1','4','6','5']);

// function camelize(str){
//     let arr = str.split("-");
//     for(let i = 0; i<arr.size-1;i++){
//             let txt= arr[i];
//             arr[i].charAt(0).toUpperCase();
//             console.log(arr[i])
//     }
//     console.log(arr);
//     return arr.join("");
// }

function camelize(str) {
    return str
      .split('-') // splits 'my-long-word' into array ['my', 'long', 'word']
      .map(
        // capitalizes first letters of all array items except the first one
        // converts ['my', 'long', 'word'] into ['my', 'Long', 'Word']
        (word, index) => index == 0 ? word : word[0].toUpperCase() + word.slice(1)
      )
      .join(''); // joins ['my', 'Long', 'Word'] into 'myLongWord'
  }

console.log(camelize("-sussy-baka"));

