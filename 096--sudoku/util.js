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

// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
function isSuperset(set, subset) {
  for (let elem of subset) {
    if (!set.has(elem)) {
      return false
    }
  }
  return true
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

// box-and-index to row-and-column
// boxRow, boxCol: The row and col of the top left corner of the given box
// TODO explain index (English reading order indexing)
function biToRc(boxRow, boxCol, index) {
  const r = boxRow + Math.floor(index / 3);
  const c = boxCol + index % 3;
  return [r, c];
}

function indicesInRow(r) {
  return {
    0: new Set([0, 1, 2]),
    1: new Set([3, 4, 5]),
    2: new Set([6, 7, 8]),
  }[r];
}

function indicesInCol(c) {
  return {
    0: new Set([0, 3, 6]),
    1: new Set([1, 4, 7]),
    2: new Set([2, 5, 8]),
  }[c];
}
