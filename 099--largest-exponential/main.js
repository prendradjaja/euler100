const fs = require('fs');

function main() {
  const pairs = read_and_parse();
  let [result, _] = maxBy(
    pairs.entries(),
    ([i, [base, exp]]) => exp * Math.log(base)
  );
  result += 1;
  console.log(result);
}

function read_and_parse() {
  return fs.readFileSync('base_exp.txt', 'utf8')
    .trim()
    .split('\n')
    .map(line => line.split(',') .map(n => +n));
}

function maxBy(seq, iteratee) {
  return Array.from(seq).reduce((a, b) => iteratee(a) > iteratee(b) ? a : b);
}

main();
