const fs = require('fs');

const names = fs.readFileSync('names.txt', 'ascii')
  .replace(/"/g, '')
  .split(',').sort();

function score(name) {
  const abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  return [...name]
    .map(c => abc.indexOf(c) + 1)
    .reduce((m, n) => m + n);
}

let result = Array.from(names.entries())
  .map(([i, name]) => (i + 1) * score(name))
  .reduce((m, n) => m + n);

console.log(result);
