const fs = require('fs');

function main() {
  const primes = fs.readFileSync('./primes', 'utf8')
    .trim()
    .split('\n')
    .map(x => +x)
    .filter(x => x <= 1000000);
  const primesSet = new Set(primes);
  const prefixSums = getPrefixSums(primes);
  const count = primes.length;
  let maxLength = 0;
  let result = 0;
  for (let length = 1; length <= count; length++) {
    const maxStart = count - length; // does not inlining this matter
    for (let start = 0; start <= maxStart; start++) {
      stop = start + length
      const mySum = sumRange(prefixSums, start, stop);
      if (primesSet.has(mySum)) {
        maxLength = length;
        result = mySum;
        console.log(maxLength, result);
        break;
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
