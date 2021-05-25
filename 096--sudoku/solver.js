const ALL_VALUES = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
const ALL_CELL_INDICES = new Set([0, 1, 2, 3, 4, 5, 6, 7, 8]);

function solve() {
  let found;
  while (found = step()) {
    grid.setCellValue(found.r, found.c, found.value);
  }
  const solved = grid.isSolved();
  if (!solved && grid.isFull()) {
    error('grid is full but not solved correctly');
  }
  // TODO for unsolved grids, we still don't have any checks to see if there
  // are clear mistakes (e.g. two 5s in the same row)
  return solved;
}

function step() {
  let result;
  result = checkEachCell();
  if (result) return result;
  result = checkLocationsInEachBox();
  if (result) return result;
}

// (based just on filled-in digits, not pencil marks)
// for each cell:
//   what values could go in this cell?
//   if exactly one value, return that
function checkEachCell() {
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      if (grid.values[r][c] !== 0) {
        continue;
      }
      let disallowed = new Set();
      disallowed = union(disallowed, grid.getRowValues(r));
      disallowed = union(disallowed, grid.getColValues(c));
      disallowed = union(disallowed, grid.getBoxValues(r, c));
      if (disallowed.size === 8) {
        const value = one(difference(ALL_VALUES, disallowed));
        return { r, c, value };
      }
    }
  }
}

// (based just on filled-in digits, not pencil marks)
// for each box:
//   for each 1..9:
//     which cells in this box could this number go in?
//     if exactly one location, return that
function checkLocationsInEachBox() {
  // for each box
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      // for each 1..9
      for (let value = 1; value <= 9; value++) {
        if (grid.getBoxValues(i, j).has(value)) {
          continue;
        }
        const candidates = whichCellsInThisBoxCanBe(i, j, value);
        if (candidates.size === 1) {
          const [r, c] = biToRc(i, j, one(candidates));
          return { r, c, value };
        }
      }
    }
  }
}

function whichCellsInThisBoxCanBe(boxRow, boxCol, value) {
  let candidates = new Set(ALL_CELL_INDICES);
  for (let i of candidates) {
    if (grid.getCellValue(...biToRc(boxRow, boxCol, i))) {
      candidates.delete(i);
    }
  }
  for (let i = 0; i < 3; i++) {
    const r = boxRow + i;
    if (grid.getRowValues(r).has(value)) {
      candidates = difference(candidates, indicesInRow(i));
    }
  }
  for (let i = 0; i < 3; i++) {
    const c = boxCol + i;
    if (grid.getColValues(c).has(value)) {
      candidates = difference(candidates, indicesInCol(i));
    }
  }
  return candidates;
}
