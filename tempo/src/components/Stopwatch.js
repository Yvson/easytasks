import React from 'react';
import worker_script from "./workers/stopwatch-worker.js";
import MyStopwatch from './models/MyStopwatch.js';


const stopwatchWorker = new Worker(worker_script);

export default class Stopwatch extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            date: new Date(0),
            time_counter: 0,
            increment: 100,
            status: 'OFF',
            marks: [],
        };
        this.padLeft = this.padLeft.bind(this);
        this.start = this.start.bind(this);
        this.stop = this.stop.bind(this);
        this.reset = this.reset.bind(this);
        this.resetOrStop = this.resetOrStop.bind(this);
        this.marking = this.marking.bind(this);
        this.dateUTCToString = this.dateUTCToString.bind(this);
        this.differenceBetweenDates = this.differenceBetweenDates.bind(this);
        this.setFullscreen = this.setFullscreen.bind(this);
        this.resetStopButton = React.createRef();
        this.fullscreenIcon = React.createRef();
        this.timeDisplay = React.createRef();
    }

    componentDidMount() {
        stopwatchWorker.onmessage = (e) => {
            this.setState({
                date: new Date(e.data.date),
                time_counter: e.data.time_counter,
            });
        };
    };

    start() {
        if (this.state.status === 'OFF') {
            let stopwatch = new MyStopwatch(this.state.date, this.state.time_counter, this.state.increment, 'ON');
            this.setState({
                status: 'ON',
            });
            stopwatchWorker.postMessage(stopwatch);
            this.resetStopButton.current.innerText = 'Parar';
        }
    };

    stop() {
        if (this.state.status === 'ON') {
            let stopwatch = new MyStopwatch(this.state.date, this.state.time_counter, this.state.increment, 'OFF');
            this.setState({
                status: 'OFF',
            });
            stopwatchWorker.postMessage(stopwatch);
        }
    };

    reset() {
        this.setState(() => ({
            date: new Date(0),
            time_counter: 0,
            marks: [],
        }));
    }

    resetOrStop() {
        if (this.state.status === 'ON') {
            this.stop();
            this.resetStopButton.current.innerText = 'Reiniciar';
        } else {
            this.reset();
            this.resetStopButton.current.innerText = 'Parar';
        }     
    }

    marking() {
        if (this.state.status === 'ON') {
            this.setState((state) => ({
                marks: [...state.marks, {id: state.marks.length, mark: state.date}],
            }));
        }
    }

    padLeft(n) {
        return n<10 ? '0'+n : n;
    };

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
        const days = Math.floor(new Date(this.state.date.getTime() - new Date(0)).getTime()/(1000*3600*24));
        const hours = this.state.date.getUTCHours() + days*24;
        const minutes = this.state.date.getUTCMinutes();
        const seconds = this.state.date.getUTCSeconds();
        const milliseconds = String(this.state.date.getUTCMilliseconds())[0];
        const marks = this.state.marks;

        for (let i=0; i<marks.length; i++) {
            tableData.push(
                <tr className="stopwatch-table-row-data">
                    <td className="num-data-table">{marks[i].id}</td>
                    <td className="mark-data-table">{this.dateUTCToString(marks[i].mark)}</td>
                    <td className="duration-data-table"> { i > 0 ? this.differenceBetweenDates(new Date(marks[i].mark), new Date(marks[i-1].mark)) : this.differenceBetweenDates(new Date(marks[i].mark), new Date(0))}</td>
                </tr>
            );
        }

        return (
            
            <div id="tempo-stopwatch-grid-app">
                <div id="tempo-stopwatch-grid-table">
                    <table id="tempo-stopwatch-table">
                        <tr>
                            <th id="num-title-table">No.</th>
                            <th id="mark-title-table">Marcação</th>
                            <th id="duration-title-table">Duração</th>
                        </tr>
                        {/* Table data will be placed below */}
                        {tableData}

                    </table>
                </div>

                <div id="tempo-grid-stopwatch" ref={this.timeDisplay}>
                    <div id="tempo-stopwatch-display" >
                        <h1 id="tempo-stopwatch-display-time">
                            {this.padLeft(hours)}
                            :{this.padLeft(minutes)}
                            :{this.padLeft(seconds)}
                            .{milliseconds}s</h1>
                        <div id="stopwatch-buttons">
                            <button id="stopwatch-start-button" className="stopwatch-button" onClick={this.start}>
                                Começar
                            </button>
                            <button id="stopwatch-mark-button" className="stopwatch-button" onClick={this.marking}>
                                Marcar
                            </button>
                            <button id="stopwatch-resetOrStop-button" className="stopwatch-button" onClick={this.resetOrStop} ref={this.resetStopButton}>
                                Parar
                            </button>
                        </div>
                    </div>
                    <div id="tempo-stopwatch-bottom">
                        <i class="material-icons icon-dashboard-bottom"
                        id="icon-fullscreen-color"
                        ref={this.fullscreenIcon}
                        onClick={this.setFullscreen}
                        >
                            fullscreen
                        </i>
                    </div>

                </div>
            </div>
        );
    }
}

