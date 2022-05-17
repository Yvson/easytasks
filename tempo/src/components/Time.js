import React from 'react';

export default class Time extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            date: new Date(0,0,0,0,0,0),
            timezone: 'America/Sao_Paulo',
        };
        this.changeTimezone = this.changeTimezone.bind(this);
        this.setTimezone = this.setTimezone.bind(this);
        this.padLeft = this.padLeft.bind(this);
        this.setFullscreen = this.setFullscreen.bind(this);
        this.fullscreenIcon = React.createRef();
        this.timeDisplay = React.createRef();
    }

    changeTimezone(UTCnow, timezone) {
        const date = new Date(UTCnow);
        const newDate = date.toLocaleString("pt-BR", {timeZone: timezone});
        const day = newDate.slice(0, 2);
        const monthIndex = String(parseInt(newDate.slice(3, 5))-1);
        const year = newDate.slice(6, 10);
        const hours = newDate.slice(11, 13);
        const minutes = newDate.slice(14, 16);
        const seconds = newDate.slice(17, 19);
        const finalDate = new Date(year, monthIndex, day, hours, minutes, seconds);
        return finalDate;
    }

    setTimezone(newTimezone) {
        this.setState({
            date: this.changeTimezone(new Date(), newTimezone),
            timezone: newTimezone,
        });
    }

    tickSecond() {
        this.setState(state => ({
            date: this.changeTimezone(new Date(), state.timezone),
        }));
    }
    
    padLeft(n) {
        return n<10 ? '0'+n : n;
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

    componentDidMount() {
        this.setState(state => ({
            date: this.changeTimezone(new Date(), state.timezone),
        }));
        this.interval = setInterval(() => this.tickSecond(), 1000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        const tableData = [];
        for (let tz in this.props.timezones) {
            tableData.push(
                <tr className="time-table-row-data" onClick={() => this.setTimezone(this.props.timezones[tz].timezone)}>
                    <td className="region-data-table">{this.props.timezones[tz].timezone}</td>
                    <td className="timezone-data-table">UTC{this.props.timezones[tz].UTCoffset}</td>
                </tr>
            );
        }

        let datenow = this.state.date;
        let timezone = this.state.timezone;
        
        let day_long_format = this.state.date.toLocaleString('pt-BR', { weekday: 'long' });
        day_long_format = day_long_format.charAt(0).toUpperCase() + day_long_format.slice(1)
        
        let month_long_format = this.state.date.toLocaleString('pt-BR', { month: 'long' });
        month_long_format = month_long_format.charAt(0).toUpperCase() + month_long_format.slice(1)        
        
        const utc_offset = (tz_name) => {
            for (let tz in this.props.timezones) {
                if (this.props.timezones[tz].timezone === tz_name)
                    return this.props.timezones[tz].UTCoffset;
            }
            
        }

        return (
            <div id="tempo-time-grid-app">
                <div id="tempo-time-grid-table">
                    <table id="tempo-time-table">
                        <thead>
                            <tr>
                                <th id="region-title-table">Região</th>
                                <th id="timezone-title-table">Fuso Horário</th>
                            </tr>
                        </thead>
                        {/* Table data will be placed below */}
                        <tbody>
                            {tableData}
                        </tbody>


                    </table>
                </div>

                <div id="tempo-grid-time" ref={this.timeDisplay}>
                    <div id="tempo-time-display">
                        <h1 id="tempo-time-display-time">
                            {this.padLeft(datenow.getHours())}
                            :{this.padLeft(datenow.getMinutes())}
                            :{this.padLeft(datenow.getSeconds())}
                        </h1>
                        <h3 id="tempo-time-display-region">
                            Horário em {timezone} (UTC{utc_offset(timezone)})
                        </h3>
                        <h3 id="tempo-time-display-date">
                            {day_long_format}, {datenow.getDate()} de {month_long_format}, {datenow.getFullYear()}
                        </h3>
                    </div>
                    <div id="tempo-time-bottom">
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
