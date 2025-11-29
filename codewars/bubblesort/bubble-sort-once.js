function bubbleSortOnce(a) {
  let res = [...a];

  for (let i = 0; i < res.length - 1; i++){
    if (res[i] > res[i + 1]) {
      // straight swap with no need for temp variable 
      // 'destructuring assignment' for swapping
      [res[i], res[i + 1]] = [res[i + 1], res[i]]
    }
  }
  return res;
}

const myArray = [9, 7, 5, 3, 1, 2, 4, 6, 8];
console.log(bubbleSortOnce(myArray));