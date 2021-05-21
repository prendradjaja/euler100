function largestPrimeFactor(n) {
  let result;
  // Instead of iterating over the primes, we can just iterate over integers:
  // Any composite number will already have been factored out by the time we
  // reach it
  for (let factor of counter(2)) {
    if (n === 1) {
      break;
    }
    while (n % factor === 0) {
      n /= factor;
      result = factor;
    }
  }
  return result;
}

function* counter(n) {
  while (true) {
    yield n++;
  }
}

console.log(largestPrimeFactor(600851475143));
