const fs = require('fs');

function main() {
  const primes = fs.readFileSync('./primes', 'utf8')
    .trim()
    .split('\n')
    .map(x => +x)
    // .filter(x => x <= 1000);
  const primesSet = new Set(primes);
  const prefixSums = getPrefixSums(primes);
  const count = primes.length;
  let maxLength = 0;
  let result = 0;
  for (let stop = 0; stop <= count; stop++) {
    for (let start = 0; start < stop; start++) {
      const mySum = sumRange(prefixSums, start, stop);
      if (primesSet.has(mySum) && stop - start > maxLength) {
        maxLength = stop - start;
        result = mySum;
      }
    }
  }
  console.log(result);
}


function sumRange(prefixSums, start, stop) {
  return prefixSums[stop] - prefixSums[start];
}

function getPrefixSums(lst) {
  x = 0;
  result = [x];
  for (let n of lst) {
    x += n;
    result.push(x);
  }
  return result;
}

main();
