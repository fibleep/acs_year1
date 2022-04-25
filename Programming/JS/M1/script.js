// console.log("debil debil");
// let name = "Ilya";

// console.log( `hello ${1}` ); // 1

// console.log( `hello ${"name"}` ); // name

// console.log( `hello ${name}` ); // Ilya

// for(let i = 0; i<=7; i++){
// console.log("#".repeat(i));
// }
// for(let i = 1; i < 100;i++){
//     if(i%3==0 && i%5==0){
//         console.log("FizzBuzz");
//         continue;
//     }
//     if(i%3==0){
//         console.log("Fizz");
//         continue;
//     }
//     if(i%5==0){
//         console.log("Buzz");
//         continue;
//     }
// }

// function chessboard(size){
//     let result="";
// for(let i = 0;i<size;i++){
//     let iter = i;
//     for(let a = 0;a<size;a++){
//             if(iter%2==0){
//                 if(a%2==0){
//                     result+=" ";
//                 }
//                 else{
//                     result+="#";
//                 }
//             }
//             else{
//                 if(a%2==0){
//                     result+="#";
//                 }
//                 else{
//                     result+=" ";
//                 }
//             }
//     }
//     result+="\n"; 
// }
// console.log(result);
// }

// chessboard(8);

// function ask(question, yes, no) {
//     if (confirm(question)) yes();
//     else no();
//   }
  

//   const ask = (question,yes,no) =>{
//       if(confirm(question)) yes();
//       else no();
//   }
//   ask(
//     "Do you agree?",
//     function() { alert("You agreed."); },
//     function() { alert("You canceled the execution."); }
//   );

//   function isEven(nr){
//       if(nr%2==0){
//           return true;
//       }
//       else{
//           return false;
//       }
//   }
//   console.log(isEven(50));
//   console.log(isEven(75));
//   console.log(isEven(-1));

function reverseArray(arr){
      const newArr=[];
      for(let i = 4;i=>0;i--){
          newArr.push(arr[i]);
          console.log(arr[i] + " " + i);
      }
      console.log(newArr);
  }
  reverseArray(['1','4','6','5']);