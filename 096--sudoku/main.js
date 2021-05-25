const $ = s => document.querySelector(s);

// TODO namespace inside an object called classes
const GIVEN = 'given';
const LAST_FILLED = 'last-filled';

class grid {
  values;
  lastFilled; // which cell did we last setCellValue()

  populateFromString(s) {
    const rootElement = $('#grid');
    let html = '';
    for (let r = 0; r < 9; r++) {
      html += `<tr>`;
      for (let c = 0; c < 9; c++) {
        html += `<td id="${this.getCellId(r, c)}"></td>`;
      }
      html += `</tr>`;
    }
    rootElement.innerHTML = html;

    this.values = [];
    for (let [r, row] of s.trim().split('\n').entries()) {
      const rowValues = [];
      this.values.push(rowValues);
      for (let [c, value] of [...row].entries()) {
        value = +value;
        rowValues.push(value);
        if (value) {
          this.setCellValue(r, c, value);
          this.getCell(r, c).classList.add(GIVEN);
        }
      }
    }
  }

  isFull() {
    return this.countFilled() === 81;
  }

  countFilled() {
    let zeroes = 0;
    for (let row of this.values) {
      for (let value of row) {
        if (value === 0) {
          zeroes++;
        }
      }
    }
    return 81 - zeroes;
  }

  isSolved() {
    if (!this.isFull()) {
      return false;
    }
    for (let r = 0; r < 9; r++) {
      if (this.getRowValues(r).size !== 9) {
        return false;
      }
    }
    for (let c = 0; c < 9; c++) {
      if (this.getColValues(c).size !== 9) {
        return false;
      }
    }
    for (let r = 0; r < 9; r += 3) {
      for (let c = 0; c < 9; c += 3) {
        if (this.getBoxValues(r, c).size !== 9) {
          return false;
        }
      }
    }
    return true;
  }

  getCellId(r, c) {
    return `cell-${r}-${c}`;
  }

  getCell(r, c) {
    return $('#'+this.getCellId(r, c));
  }

  getCellValue(r, c) {
    return this.values[r][c];
  }

  setCellValue(r, c, value) {
    if (this.lastFilled) {
      this.lastFilled.classList.remove(LAST_FILLED);
    }
    this.values[r][c] = value;
    const cell = this.getCell(r, c);
    cell.innerHTML = value;
    cell.classList.add(LAST_FILLED);
    this.lastFilled = cell;
  }

  getRowValues(r) {
    const result = new Set(this.values[r]);
    result.delete(0);
    return result;
  }

  getColValues(c) {
    const result = new Set();
    for (let row of this.values) {
      result.add(row[c]);
    }
    result.delete(0);
    return result;
  }

  getBoxValues(r, c) {
    r -= r % 3;
    c -= c % 3;
    const result = new Set();
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        result.add(this.values[r+i][c+j]);
      }
    }
    result.delete(0);
    return result;
  }
}

grid = new grid();
let successCount = 0;
// // puzzles = [puzzles[1]];
// for (let [i, puzzle] of puzzles.entries()) {
//   grid.populateFromString(puzzle);
//   const pre = grid.countFilled();
//   const success = solve();
//   const post = grid.countFilled();
//   successCount += success;
//   let failDetails = '';
//   if (!success) {
//     failDetails = `${pre} -> ${post}`
//   }
//   console.log(i, success, failDetails);
// }
// console.log('# of successes:', successCount);

grid.populateFromString(puzzles[3]);
solve();
