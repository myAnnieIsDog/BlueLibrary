// let rand = Math.floor(Math.random() * 10) + 1
// console.log(rand)

function dateWindow(){
    // Define the start and end dates for datepicker.

    function formatDate(input){
        const week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        const day = week[input.getDay()];
        const month = String(input.getMonth() + 1).padStart(2, 0); 
        const date = String(input.getDate()).padStart(2, 0);
        const year = String(input.getFullYear());
        const calc = `${year}-${month}-${date}`;
        const display = `${month}/${date}/${year} ${day}` ;
        return [calc, display];
    }
    // Get the current date, check for 2:00 p.m. cutoff, calc first day to check.
    var today = new Date();
    if (today.getHours() <= 14) {n = 1} else {n = 2};
    let day = 86400000;//milliseconds = 1 day = 1000-ms * 60-s * 60-min * 24-hrs
    let i = n;
    let r = 1;
    while (r < 8){
        var holidays = [
            "2023-11-10",
            "2023-11-23",
            "2023-11-24",
            "2023-12-24",
            "2023-12-25",
            "2023-12-26",
            "2023-12-27",
            "2023-12-28",
            "2023-12-29",
            "2023-12-30",
            "2023-12-31",
         
            "2024-01-01",
            "2024-01-15",
            "2024-02-19",
            "2024-04-01",
            "2024-05-27",
            "2024-06-19",
            "2024-07-04",
            "2024-09-02",
            "2024-11-11",
            "2024-11-28",
            "2024-11-29",
            "2024-12-24",
            "2024-12-25",
            "2024-12-26",
            "2024-12-27",
            "2024-12-28",
            "2024-12-29",
            "2024-12-30",
            "2024-12-31",
        ];
        let date2check = new Date(+new Date() + i * day);
        const calc = formatDate(date2check)[0];
        const display = formatDate(date2check)[1];
        i++;
        if (date2check.getDay() == 0 || date2check.getDay() == 6 || holidays.includes(calc)) {
            continue;
        } else {
            console.log(`${calc}  - -  ${display}`);
            const radio = document.getElementById(`date${r}`);
            const label = document.getElementById(`date${r}Lbl`);
            radio.setAttribute("value", calc);
            label.innerHTML = display;
            r++;
            }
        }
    }

// Call functions.
dates = dateWindow();
