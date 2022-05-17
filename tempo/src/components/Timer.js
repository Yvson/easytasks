import React from 'react';
import InputTimer from './Input_Timer';
import MyTimer from './models/MyTimer';
import worker_script from './workers/timer-worker';


const timerWorker = new Worker(worker_script);

export default class Timer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            date: new Date(0),
            time: '0000000',
            time_counter: 0,
            decrement: 100,
            status: 'OFF',
            marks: [],
        };
        this.inputTimerChange = this.inputTimerChange.bind(this);
        this.stopOnClick = this.stopOnClick.bind(this);
        this.padLeft = this.padLeft.bind(this);
        this.correctInputTime = this.correctInputTime.bind(this);
        this.start = this.start.bind(this);
        this.stop = this.stop.bind(this);
        this.marking = this.marking.bind(this);
        this.dateUTCToString = this.dateUTCToString.bind(this);
        this.differenceBetweenDates = this.differenceBetweenDates.bind(this);
        this.fromInputToDate = this.fromInputToDate.bind(this);
        this.fromDateToInput = this.fromDateToInput.bind(this);
        this.setFullscreen = this.setFullscreen.bind(this);
        this.fullscreenIcon = React.createRef();
        this.timeDisplay = React.createRef();
        this.alarmSound = document.getElementById('alarm-sound');

    }

    componentDidMount() {
        timerWorker.onmessage = (e) => {
            this.setState({
                date: new Date(e.data.date),
                time: String(this.fromDateToInput(e.data.date)),
                time_counter: e.data.time_counter,
                status: e.data.status,
            }, () => {
                if (this.state.marks.length === 0 && this.state.time !== '0000000') {
                    this.marking();
                }
                if (this.state.marks.length !== 0 && this.state.time === '0000000' && this.state.status === 'OFF') {
                    this.alarmSound.volume = 0.25;
                    this.alarmSound.play();
                }
            });
        };
    }

    inputTimerChange(data) {
        this.setState({
            time: data.time,
        });
    }

    stopOnClick(data) {
        let timer;
        this.setState({
            status: data.status,
            marks: [],
        }, () => {
            timer = new MyTimer(this.state.date, this.state.time_counter, this.state.decrement, this.state.status);
            timerWorker.postMessage(timer);
        });
    }

    start() {
        if (this.state.status === 'OFF') {
            let timer;
            this.setState({
                date: this.fromInputToDate(this.state.time),
                time_counter: this.fromInputToDate(this.state.time).getTime(),
                status: 'ON',
            }, () => {
                if (this.state.time_counter !== 0) {
                    timer = new MyTimer(this.state.date, this.state.time_counter, this.state.decrement, this.state.status);
                    timerWorker.postMessage(timer);
                }
            });
        }
    }

    stop() {
        if (this.state.status === 'ON') {
            let timer;
            this.setState({
                status: 'OFF',
            }, () => {
                timer = new MyTimer(this.state.date, this.state.time_counter, this.state.decrement, this.state.status);
                timerWorker.postMessage(timer);
            });
        }
    }

    marking() {
        if (this.state.status === 'ON' && this.state.time !== '0000000') {
            this.setState((state) => ({
                marks: [...state.marks, {id: state.marks.length, mark: state.date}],
            }));
        }
    }

    padLeft(n) {
        return n<10 ? '0'+n : n;
    };

    correctInputTime(inputData) {
        let input = inputData.split('');
        if (parseInt(input[2]) > 5) {
            input[2] = '5';
        }
        if (parseInt(input[4]) > 5) {
            input[4] = '5';
        }
        input = input.join('');
        return input;
    }


    dateUTCToString(date) {
        let finalDate;
        const days = Math.floor(new Date(this.state.date.getTime() - new Date(0)).getTime()/(1000*3600*24));
        const hours = this.padLeft(parseInt((date.getUTCHours())) + days*24);
        const minutes = this.padLeft(date.getUTCMinutes());
        const seconds = this.padLeft(date.getUTCSeconds());
        const milliseconds = date.getUTCMilliseconds();
        finalDate = hours+':'+minutes+':'+seconds+'.'+String(milliseconds)[0];
        return finalDate;
    }

    differenceBetweenDates(date1, date2) {
        
        const oldDate = date1.getTime() > date2.getTime() ? date2 : date1 ;
        const newDate = date1.getTime() > date2.getTime() ? date1 : date2 ;
        
        const diffDates = new Date(newDate.getTime() - oldDate.getTime());;
        
        const days = Math.floor(diffDates.getTime()/(1000*3600*24));
        const hours = this.padLeft(parseInt(diffDates.getUTCHours()) + days*24);
        const minutes = this.padLeft(diffDates.getUTCMinutes());
        const seconds = this.padLeft(diffDates.getUTCSeconds());
        const milliseconds = diffDates.getUTCMilliseconds();
        const finalDiff = hours+':'+minutes+':'+seconds+'.'+String(milliseconds)[0];
        return finalDiff;        
    }

    fromInputToDate(input) {
        input = this.correctInputTime(input);
        const ms = parseInt(input[6]);
        const sec = parseInt(input.substring(4,6));
        const min = parseInt(input.substring(2,4));
        const hour = parseInt(input.substring(0,2));
        const finalDate = new Date(hour*60*60*1000+min*60*1000+sec*1000+ms*100);
        return finalDate;
    }

    fromDateToInput(date) {
        const days = Math.floor((date - new Date(0))/(1000*3600*24));
        const hours = this.padLeft(parseInt(date.getUTCHours()) + days*24);
        const minutes = this.padLeft(date.getUTCMinutes());
        const seconds = this.padLeft(date.getUTCSeconds());
        const milliseconds = date.getUTCMilliseconds();
        const finalInput = `${hours}${minutes}${seconds}${String(milliseconds)[0]}`;
        return finalInput;
    }

    setFullscreen() {
        if (this.timeDisplay.current.classList.contains('time_fullscreen')) {
            this.timeDisplay.current.classList.remove('time_fullscreen');
            this.fullscreenIcon.current.innerText = 'fullscreen';
        } else {
            this.timeDisplay.current.classList.add('time_fullscreen');
            this.fullscreenIcon.current.innerText = 'fullscreen_exit';
        }
    }



    render() {
        const tableData = [];
        const marks = this.state.marks;

        for (let i = 0; i < marks.length; i++) {
            tableData.push(
                <tr className="timer-table-row-data">
                    <td className="num-data-table">{i}</td>
                    <td className="mark-data-table">{this.dateUTCToString(marks[i].mark)}</td>
                    <td className="duration-data-table">
                        { i > 0 ? 
                            this.differenceBetweenDates(new Date(marks[i].mark), new Date(marks[i-1].mark)) 
                            : 
                            '00:00:00.0'
                        }
                    </td>
                </tr>
            );
        }

        return (
            <div id="tempo-timer-grid-app">
                <div id="tempo-timer-grid-table">
                    <table id="tempo-timer-table">
                        <tr>
                            <th id="num-title-table">No.</th>
                            <th id="mark-title-table">Marcação</th>
                            <th id="duration-title-table">Duração</th>
                        </tr>

                        {tableData}

                    </table>
                </div>

                <div id="tempo-grid-timer" ref={this.timeDisplay}>
                    <div id="tempo-timer-display">
                        <InputTimer 
                            time={this.state.time}
                            status={this.state.status}
                            onChange={this.inputTimerChange}
                            onClick={this.stopOnClick}
                        />

                        <div id="timer-buttons">
                            <button id="timer-start-button" className="timer-button" onClick={this.start}>
                                Começar
                            </button>
                            <button id="timer-mark-button" className="timer-button" onClick={this.marking}>
                                Marcar
                            </button>
                            <button id="timer-restart-button" className="timer-button" onClick={this.stop}>
                                Parar
                            </button>
                        </div>
                    </div>
                    <div id="tempo-timer-bottom">
                        <i 
                            className="material-icons icon-dashboard-bottom"
                            id="icon-fullscreen-color"
                            ref={this.fullscreenIcon}
                            onClick={this.setFullscreen}
                            >fullscreen
                        </i>
                    </div>

                </div>
            </div>
        );
    }
}
