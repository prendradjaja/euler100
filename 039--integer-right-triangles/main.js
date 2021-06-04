function* triangles(n) {
  for (let a = 1; a <= n - 2; a++) {
    for (let b = 1; b <=a; b++) {
      const c = n - a - b;
      if (c > 0) {
        yield [a, b, c];
      } else {
        break;
      }
    }
  }
}

// https://youmightnotneed.com/lodash/#maxBy
const maxBy = (arr, func) => {
  const max = Math.max(...arr.map(func))
  return arr.find(item => func(item) === max)
}

const solutionCounts = [];
for (let p = 5; p <= 1000; p++) {
  let numberOfSolutions = 0;
  for (let [a, b, c] of triangles(p)) {
    if (a*a + b*b === c*c) {
      numberOfSolutions++;
    }
  }
  solutionCounts.push({ p, numberOfSolutions });
}

console.log(maxBy(solutionCounts, x => x.numberOfSolutions).p);
