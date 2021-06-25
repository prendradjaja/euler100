'use strict';

function main() {
  const amicables = new Set();
  for (let n = 2; n < 10000; n++) {
    if (n === sumProperDivisors(sumProperDivisors(n))
        && n !== sumProperDivisors(n)
    ) {
      amicables.add(n);
      amicables.add(sumProperDivisors(n));
    }
  }
  console.log(sum(Array.from(amicables)));
}

function sumProperDivisors(n) {
  return sum(Array.from(getProperDivisorsUnordered(n)));
}

function* getProperDivisorsUnordered(n) {
  if (n > 1) {
    yield 1;
  }
  let factor = 2;
  while (factor * factor < n) {
    if (n % factor === 0) {
      yield factor;
      yield n / factor;
    }
    factor++;
  }
  if (factor * factor === n && n % factor === 0) {
    yield factor;
  }
}

function sum(array) {
  return array.reduce((a, b) => a + b, 0);
}

main();
