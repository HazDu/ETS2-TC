document.addEventListener("DOMContentLoaded", () => {
    const site = document.body.dataset.site;
    const input_min = document.getElementById("input_min");
    const input_hrs = document.getElementById("input_hrs");
    const output_str = document.getElementById("result_text");
    console.log("Variables initialized!");

    function calculate() {
        if (isNaN(input_min.value) && input_min.value.trim() !== "") {
            input_min.value = input_min.value.slice(0, -1);
        }
        if (isNaN(input_hrs.value) && input_hrs.value.trim() !== "") {
            input_hrs.value = input_hrs.value.slice(0, -1);
        }
        if (input_min.value.length > 8) {
            input_min.value = input_min.value.slice(0, 8);
        }
        if (input_hrs.value.length > 8) {
            input_hrs.value = input_hrs.value.slice(0, 8);
        }
        let min = parseFloat(input_min.value);
        let hrs = parseFloat(input_hrs.value);

        if (!isNaN(min) || !isNaN(hrs)) {
            if(isNaN(min)) {
                min = 0;
            }
            if(isNaN(hrs)) {
                hrs = 0;
            }

            if (site === "ets_to_irl") {
                const total_minutes = (min + (hrs * 60)) / 19;
                const result_hrs = Math.floor(total_minutes / 60);
                const result_min = Math.round(total_minutes % 60);
                output_str.textContent = `That's ${result_hrs} hours and ${result_min} minutes in real time.`;
            }
            else if (site === "irl_to_ets") {
                const total_minutes = (min + (hrs * 60)) * 19;
                const result_hrs = Math.floor(total_minutes / 60);
                const result_min = Math.round(total_minutes % 60);
                output_str.textContent = `That's ${result_hrs} hours and ${result_min} minutes in Euro Truck Simulator 2.`;
            }
        }
        else {
            output_str.textContent = ``;
        }
    }

    input_min.addEventListener("input", calculate);
    input_hrs.addEventListener("input", calculate);
})
