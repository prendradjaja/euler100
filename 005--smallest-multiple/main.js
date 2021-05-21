function main() {
  let resultFactors = {};
  for (let n = 1; n <= 20; n++) {
    const nFactors = factorize(n);
    for (let f in nFactors) {
      resultFactors[f] = resultFactors[f] || 0;
      resultFactors[f] = Math.max(resultFactors[f], nFactors[f]);
    }
  }
  let result = 1;
  for (let f in resultFactors) {
    f = +f;
    for (let i = 0; i < resultFactors[f]; i++) {
      result *= f;
    }
  }
  console.log(result);
}

function factorize(n) {
  let factors = {};
  // Instead of iterating over the primes, we can just iterate over integers:
  // Any composite number will already have been factored out by the time we
  // reach it
  for (let f of counter(2)) {
    if (n === 1) {
      break;
    }
    while (n % f === 0) {
      n /= f;
      factors[f] = factors[f] || 0;
      factors[f]++;
    }
  }
  return factors;
}

function* counter(n) {
  while (true) {
    yield n++;
  }
}

main();
