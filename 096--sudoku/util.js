// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
function union(setA, setB) {
  let _union = new Set(setA)
  for (let elem of setB) {
    _union.add(elem)
  }
  return _union
}

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
function difference(setA, setB) {
  let _difference = new Set(setA)
  for (let elem of setB) {
    _difference.delete(elem)
  }
  return _difference
}

function one(set) {
  if (set.size !== 1) {
    error('set.size !== 1');
  }
  return Array.from(set)[0];
}

// TODO Probably change to assert or failIf
function error(message, ...other) {
  window.alert('ERROR ' + message);
  console.error('ERROR', message, ...other);
  throw new Error(); // This error is just used to stop execution
}
