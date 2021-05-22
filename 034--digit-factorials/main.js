function main() {
  const maxN = 10 * 1000 * 1000; // See main.py
  let total = 0;
  for (let n = 10; n < maxN; n++) {
    if (n == curious_sum(n)) {
      total += n;
    }
  }
  console.log(total);
}

function factorial(n) {
  return n == 0 ? 1 : n * factorial(n - 1);
}

function curious_sum(n) {
  return [...n.toString()]
    .map(digit => factorial(+digit))
    .reduce((a, b) => a + b);
}

main();
