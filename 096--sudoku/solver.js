const ALL_VALUES = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
const ALL_CELL_INDICES = new Set([0, 1, 2, 3, 4, 5, 6, 7, 8]);
const ALL_BOX_INDICES = new Set([0, 3, 6]);

function solve() {
  let found;
  const snyderPairs = new SnyderPairs();
  const state = { snyderPairs }; // any extra state (beyond the grid itself) used by the solver
  while (found = step(state)) {
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

function step(state) {
  let result;
  result = checkEachCell();
  if (result) return result;
  result = checkLocationsInEachBox(state);
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

// (based on filled-in digits and snyder pairs)
// for each box:
//   for each 1..9:
//     which cells in this box could this number go in?
//     if exactly one location, return that
function checkLocationsInEachBox(state) {
  const { snyderPairs } = state;
  // for each box
  for (let i = 0; i < 9; i += 3) {
    for (let j = 0; j < 9; j += 3) {
      // for each 1..9
      for (let value = 1; value <= 9; value++) {
        if (grid.getBoxValues(i, j).has(value)) {
          continue;
        }
        const candidates = whichCellsInThisBoxCanBe(i, j, value, state);
        if (candidates.size === 1) {
          const [r, c] = biToRc(i, j, one(candidates));
          return { r, c, value };
        } else if (candidates.size === 2) {
          snyderPairs.set(i, j, value, candidates);
        } else if (candidates.size === 0) {
          error(`no possible location for ${value} in box ${i}-${j}`);
        }
      }
    }
  }
}

function whichCellsInThisBoxCanBe(boxRow, boxCol, value, state) {
  const { snyderPairs } = state;
  let candidates = new Set(ALL_CELL_INDICES);
  for (let i of candidates) {
    if (grid.getCellValue(...biToRc(boxRow, boxCol, i))) {
      candidates.delete(i);
    }
  }
  for (let i = 0; i < 3; i++) {
    const r = boxRow + i;
    if (grid.getRowValues(r).has(value) || snyderPairs.rowHas(r, value, boxRow, boxCol)) {
      candidates = difference(candidates, indicesInRow(i));
    }
  }
  for (let i = 0; i < 3; i++) {
    const c = boxCol + i;
    if (grid.getColValues(c).has(value) || snyderPairs.colHas(c, value, boxRow, boxCol)) {
      candidates = difference(candidates, indicesInCol(i));
    }
  }
  return candidates;
}

class SnyderPairs {
  // boxrow,boxcol,value -> Set { index1, index2 }
  _pairs = {};

  // maybe in the future will need to include a check to see if this box-value already only has a single index
  // currently not needed because pairs are only ever added, not deleted
  set(i, j, value, candidates) {
    this._pairs[`${i},${j},${value}`] = new Set(candidates);
  }

  // does one of the OTHER boxes have a pair (of this value) in this row
  rowHas(r, value, boxRow, boxCol) {
    const otherBoxCols = new Set(ALL_BOX_INDICES);
    otherBoxCols.delete(boxCol);
    for (let otherBoxCol of otherBoxCols) {
      const indices = this._pairs[`${boxRow},${otherBoxCol},${value}`];
      if (indices && isSuperset(indicesInRow(r - boxRow), indices)) {
        // console.log('rowHas', {r, value, boxRow, boxCol});
        return true;
      }
    }
    return false;
  }

  // does one of the OTHER boxes have a pair (of this value) in this column
  colHas(c, value, boxRow, boxCol) {
    const otherBoxRows = new Set(ALL_BOX_INDICES);
    otherBoxRows.delete(boxRow);
    for (let otherBoxRow of otherBoxRows) {
      const indices = this._pairs[`${otherBoxRow},${boxCol},${value}`];
      if (indices && isSuperset(indicesInCol(c - boxCol), indices)) {
        // console.log('colHas', {c, value, boxCol, boxRow});
        return true;
      }
    }
    return false;
  }
}