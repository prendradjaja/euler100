function period(n) {
  const seen = { 10: 0 };
  let x = 10;
  let i = 0;
  while (x) {
    x = 10 * (x % n);
    i++;
    if (seen[x]) {
      return i - seen[x];
    }
    seen[x] = i;
  }
  return -1;
}

// Not strictly necessary, but this is the simpler function that period() is based on
function* digits(n) {
  let x = 10;
  while (x) {
    yield Math.floor(x / n);
    x = 10 * (x % n);
  }
}

function string(n) {
  let i = 0;
  let s = '0.';
  for (let digit of digits(n)) {
    i++;
    s += digit;
    if (i > 15) {
      s += '...';
      break;
    }
  }
  return s;
}

let maxPeriod = 0;
let result = -1;
for (let n = 2; n < 1000; n++) {
  const nPeriod = period(n);
  if (nPeriod > maxPeriod) {
    maxPeriod = nPeriod;
    result = n;
  }
}

console.log('Answer:', result);
console.log('Period:', maxPeriod);
console.log('Reciprocal:', string(result));
