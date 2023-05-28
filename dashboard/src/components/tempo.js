import React from "react";




export default class Tempo extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            date: new Date(0,0,0,0,0,0),
            timezone: 'America/Sao_Paulo',
            utc_offset: '-3:00'
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
        const hours = newDate.slice(12, 14);
        const minutes = newDate.slice(15, 17);
        const seconds = newDate.slice(18, 20);
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
            <div id="tempo" ref={this.timeDisplay}>
                <div id="tempo-top">
                    <i class="material-icons icon-dashboard-top" id="icon-tempo-color">query_builder</i>
                    <h3 id="tempo-icon-title">Tempo</h3>
                </div>
                <div id="tempo-frame">
                    <div id="tempo-display">
                        <div id="clock-display">
                            <h1 id="clock-display-time">
                                {this.padLeft(datenow.getHours())}
                                :{this.padLeft(datenow.getMinutes())}
                                :{this.padLeft(datenow.getSeconds())}
                            </h1>
                            <h3 id="clock-display-region">
                                Horário em {timezone} (UTC{this.state.utc_offset})
                            </h3>
                            <h3 id="clock-display-date">
                                {day_long_format}, {datenow.getDate()} de {month_long_format}, {datenow.getFullYear()}
                            </h3>
                        </div>
                    </div>
                </div>
                <div id="tempo-bottom">
                    <i 
                        class="material-icons icon-dashboard-bottom"
                        id="icon-fullscreen-color"
                        ref={this.fullscreenIcon}
                        onClick={this.setFullscreen}
                    >
                        fullscreen
                    </i>
                </div>
            </div>                
        );
    }
}