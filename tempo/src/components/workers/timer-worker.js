const worker = () => {
    let interval;
    self.onmessage = (e) => {
        let timer = e.data;
        let date = timer.date;
        let time_counter = timer.time_counter;
        let decrement = timer.decrement;
        let status = timer.status;

        switch (status) {
            case 'ON':
                interval = setInterval(() => {
                    date = new Date(time_counter);
                    self.postMessage({date, time_counter, status});
                    time_counter = time_counter-decrement;
                    if (time_counter < 0) {
                        date = new Date(0);
                        time_counter = 0;
                        status = 'OFF';
                        self.postMessage({date, time_counter, status});
                        clearInterval(interval);
                    }
                }, decrement);
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


