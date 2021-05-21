function ok(n) {
  for (let i = 1; i <= 20; i++) {
    if (n % i !== 0) {
      return false;
    }
  }
  return true;
}

for (let n = 1; ; n++) {
  if (ok(n)) {
    console.log(n);
    break;
  }
}
