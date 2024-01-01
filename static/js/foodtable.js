const table = document.getElementById('foodtable');
let calories = 0;
    for (let i =1; i< table.rows.length -1; i++){
        calories += parseFloat(table.rows[i].cells[1].innerHTML);
    }

    