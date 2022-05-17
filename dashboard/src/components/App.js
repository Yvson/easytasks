import React from 'react';
import ReactDOM from 'react-dom';
import Cotacoes from './cotacoes';
import Tempo from './tempo';



export default class App extends React.Component {
    constructor(props) {
        super(props);
    }

    
    render() {

        return (
            <div id="menu">
                <a href={this.props.hrefConversor}>
                    <div id="conversor">
                            <div class="icon-and-title">
                                <i class="material-icons icon-dashboard" id="icon-conversor-color">autorenew</i>
                                <h2 class="icon-title"> Conversor de Unidades </h2>
                            </div>
                    </div>
                </a>

                <a href={this.props.hrefGerador}>
                    <div id="gerador">
                            <div class="icon-and-title">
                                <i class="material-icons icon-dashboard" id="icon-gerador-color">calculate</i>
                                <h2 class="icon-title"> Gerador </h2>
                            </div>
                    </div>
                </a>        

                <a href={this.props.hrefTexto}>
                    <div id="texto">
                            <div class="icon-and-title">
                                <i class="material-icons icon-dashboard" id="icon-texto-color">text_format</i>
                                <h2 class="icon-title"> Texto </h2>
                            </div>
                    </div>
                </a>

                <a href={this.props.hrefCores}>
                    <div id="cores">
                            <div class="icon-and-title">
                                <i class="material-icons icon-dashboard" id="icon-cores-color">palette</i>
                                <h2 class="icon-title"> Cores </h2>
                            </div>
                    </div>
                </a>

                <Tempo />        

                <Cotacoes 
                    currenciesAPI={this.props.currenciesAPI}
                    cryptocurrenciesAPI={this.props.cryptocurrenciesAPI}
                    hrefCotacoes={this.props.hrefCotacoes}
                />


            </div>
        );
    }
}



ReactDOM.render(
    <App 
    currenciesAPI={window.currenciesAPI}
    cryptocurrenciesAPI={window.cryptocurrenciesAPI}
    hrefCotacoes={window.hrefCotacoes}
    hrefConversor={window.hrefConversor}
    hrefGerador={window.hrefGerador}
    hrefTexto={window.hrefTexto}
    hrefCores={window.hrefCores}
    />,
    window.react_mount
);













//<div id="tempo-menu">
//    <div class="tempo-menu-rect-clock tempo-menu-text">
//        Relógio
//    </div>
//    <div class="tempo-menu-rect-timer tempo-menu-text">                
//        Cronômetro
//    </div>            
//    <div class="tempo-menu-rect-stopwatch tempo-menu-text">
//        Temporizador
//    </div>                
//</div>    
