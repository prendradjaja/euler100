const $ = s => document.querySelector(s);

function drawGrid() {
  const grid = $('#grid');
  let html = '';
  for (let r = 0; r < 9; r++) {
    html += `<tr>`;
    for (let c = 0; c < 9; c++) {
      const given = Math.random() > 0.9 ? 'given' : '';
      html += `<td id="cell-${r}-${c}" class="${given}">9</td>`;
    }
    html += `</tr>`;
  }
  grid.innerHTML = html;
}

drawGrid();
