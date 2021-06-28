const { union, difference } = require('./util');

const ALL_VALUES = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
const ALL_CELL_INDICES = new Set([0, 1, 2, 3, 4, 5, 6, 7, 8]);
const ALL_BOX_INDICES = new Set([0, 3, 6]);

// 030050040
// 008010500
// 460000012
// 070502080
// 000603000
// 040109030
// 250000098
// 001020600
// 080060020


function solve(grid) {
  const slots = getSlots(grid);
  dfs({grid, slots, nextSlotIndex: 0});
}

function dfs(args) {
  const {grid, slots, nextSlotIndex} = args;
  if (nextSlotIndex === slots.length) {
    console.log('Solved?', grid.isSolved(), grid.values[0].slice(0, 3).join(''));
    return;
  }
  for (let child of children(args)) {
    const {r, c, value} = child.placement;
    grid.setCellValue(r, c, value);
    dfs(child.args);
    grid.setCellValue(r, c, 0);
  }
}

function* children(args) {
  const {grid, slots, nextSlotIndex} = args;
  const nextSlot = slots[nextSlotIndex];
  const { r, c } = nextSlot;

  // let disallowed = new Set();
  // disallowed = union(disallowed, grid.getRowValues(r));
  // disallowed = union(disallowed, grid.getColValues(c));
  // disallowed = union(disallowed, grid.getBoxValues(r, c));

  let allowed = ALL_VALUES; // not copying, but it's ok bc we're not mutating it
  allowed = difference(allowed, grid.getRowValues(r));
  allowed = difference(allowed, grid.getColValues(c));
  allowed = difference(allowed, grid.getBoxValues(r, c));
  // console.log(allowed);
  for (let value of allowed) {
    yield {
      placement: { r, c, value },
      args: { ...args, nextSlotIndex: nextSlotIndex + 1 },
    };
  }
}

function getSlots(grid) {
  const result = [];
  for (let [r, row] of grid.values.entries()) {
    for (let [c, value] of row.entries()) {
      if (value === 0) {
        result.push({ r, c });
      }
    }
  }
  return result;
}

exports.solve = solve;
