function main() {
  for (let xs of consecutives(counter(1), 4)) {
    if (xs.every(x => 4 === countDistinctPrimeFactors(x))) {
      console.log(xs[0]);
      break;
    }
  }
}

function countDistinctPrimeFactors(n) {
  let factors = new Set();
  // Instead of iterating over the primes, we can just iterate over integers:
  // Any composite number will already have been factored out by the time we
  // reach it
  for (let f of counter(2)) {
    if (n === 1) {
      break;
    }
    while (n % f === 0) {
      n /= f;
      factors.add(f);
    }
  }
  return factors.size;
}

function* counter(n) {
  while (true) {
    yield n++;
  }
}

function* consecutives(seq, n) {
  prevs = []
  for (let item of seq) {
    prevs.push(item);
    if (prevs.length === n) {
      yield [...prevs];
      prevs.shift();
    }
  }
}

main();
