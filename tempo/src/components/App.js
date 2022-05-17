import React from 'react';
import ReactDOM from 'react-dom';
import Time from './Time';
import Timer from './Timer';
import Stopwatch from './Stopwatch';


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            app: this.props.appName,
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({

        });
    }

    render() {
        let appToMount;
        switch (this.state.app) {
            case 'relogio':
                return appToMount = <Time timezones={this.props.timezones}/>;
            case 'temporizador':
                return appToMount = <Timer />;
            case 'cronometro':
                return appToMount = <Stopwatch />;
        }
        return (
            <div id="tempo-app">
                {appToMount}
            </div>
        );
    }
}

ReactDOM.render(
    <App
        appName={window.mountingInfo.appName}
        timezones={window.mountingInfo.timezones}
    />,
    window.mountingInfo.component
);