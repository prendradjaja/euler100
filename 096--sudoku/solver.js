function solve() {
  let found;
  found = findNakedSingle();
  while (found = findNakedSingle()) {
    grid.setCellValue(found.r, found.c, found.value);
  }
  // TODO check if full, check if solved correctly
}

const ALL_VALUES = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);

// Without pencil marks
function findNakedSingle() {
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

solve();
