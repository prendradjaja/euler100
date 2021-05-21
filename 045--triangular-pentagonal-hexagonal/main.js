const t = n => n*(n + 1)/2;
const p = n => n*(3*n - 1)/2;
const h = n => n*(2*n - 1);
const fs = [t, p, h];

const qualities = {};

for (let i = 1; ; i++) {
  for (let f of fs) {
    const n = f(i);
    qualities[n] = qualities[n] || 0;
    qualities[n]++;
    if (qualities[n] === 3) {
      console.log(n, );
    }
  }
}
