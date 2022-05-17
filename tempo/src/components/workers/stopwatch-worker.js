const worker = () => {
    let interval;
    self.onmessage = (e) => {
        let stopwatch = e.data;
        let date = stopwatch.date;
        let time_counter = stopwatch.time_counter;
        let increment = stopwatch.increment;
        let status = stopwatch.status;

        switch (status) {
            case 'ON':
                interval = setInterval(() => {
                    date = new Date(time_counter);
                    self.postMessage({date, time_counter});
                    time_counter = time_counter+increment;
                }, increment);
                break;

            case 'OFF':
                clearInterval(interval);
                break;
    
            default:
                break;
        }
    };
};

let raw_code = worker.toString();
raw_code = raw_code.substring(raw_code.indexOf("{") + 1, raw_code.lastIndexOf("}"));

const blob = new Blob([raw_code], { type: "application/javascript" });
const worker_script = URL.createObjectURL(blob);

export default worker_script;


