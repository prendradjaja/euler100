// Could be DRYed with uniquePrimeFactors by adding primeFactorts like so:
//   function* primeFactors(n) { ... }
//   uniquePrimeFactors = n => uniq(primeFactors(n))
//   primeFactorization = n => pythonCounter(primeFactors(n))
// But this has a slight cost to readability and a large cost to "how do I
// remember which one to use?"
function primeFactorization(n) {
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
exports.primeFactorization = primeFactorization;

function* uniquePrimeFactors(n) {
  let factors = {};
  // Instead of iterating over the primes, we can just iterate over integers:
  // Any composite number will already have been factored out by the time we
  // reach it
  for (let f of counter(2)) {
    if (n === 1) {
      break;
    }
    let first = true;
    while (n % f === 0) {
      n /= f;
      if (first) {
        yield f;
        first = false;
      }
    }
  }
}
exports.uniquePrimeFactors = uniquePrimeFactors;

function* head(seq, n) {
  n = n || 10;
  for (let item of seq) {
    yield item;
    n--;
    if (n <= 0) {
      break;
    }
  }
}
exports.head = head;

function* counter(n) {
  while (true) {
    yield n++;
  }
}
exports.counter = counter;

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
exports.consecutives = consecutives;
