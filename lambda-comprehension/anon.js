// let times_two = function(num) {
//   return num * 2
// }

// let times_two = (num) => {
//   // no additional logic
//   return num * 2
// }

// One liner fat-arrow function
// let times_two = num => num * 2
// console.log(times_two(7))

let arr_of_nums = [1,53,6,3,6,643,4,6,73,4,7,86,34,45,7,4,5]
let odd_num_list = arr_of_nums.filter(num => num % 2 !== 0)
let even_num_list = arr_of_nums.filter(num => num % 2 === 0)
console.log(odd_num_list)
console.log(even_num_list)
