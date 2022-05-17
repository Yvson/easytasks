import React from "react";



export default class Cotacoes extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currencies: [],
            cryptocurrencies: [],
            isCurrenciesLoaded: false,
            isCryptocurrenciesLoaded: false,
            currenciesSource: '',
            cryptocurrenciesSource: '',
            lastUpdate: '',
            error: null,
        }
    }

    getCurrencyData() {
        fetch(this.props.currenciesAPI)
            .then(res => res.json())
            .then((result) => {
                this.setState({
                    isCurrenciesLoaded: true,
                    currencies: result,
                    currenciesSource: result[0].source,
                    lastUpdate: result[0].date,

                });
              }, 
              (error) => {
                  this.setState({
                        isCurrenciesLoaded: true,
                        error: error,
                    });
              }
            );
    }

    getCryptocurrencyData() {
        fetch(this.props.cryptocurrenciesAPI)
            .then(res => res.json())
            .then(
              (result) => {
                this.setState({
                    isCryptocurrenciesLoaded: true,
                    cryptocurrencies: result,
                    cryptocurrenciesSource: result[0].source,
                    lastUpdate: result[0].date,
                });
              },
              (error) => {
                this.setState({
                    isCryptocurrenciesLoaded: true,
                    error: error,
                });
              }
            );
    }

    updatePrices() {
        this.getCurrencyData();
        this.getCryptocurrencyData();
    }

    
    componentDidMount() {
        this.updatePrices();
        this.interval = setInterval(() => this.updatePrices(), 30000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        const currencies_rows = this.state.currencies.map((e) => 
            (
                <tr>
                    <td class="cotacoes-table-avatar">{e.from_country_region}</td>
                    <td>{e.name}</td>
                    <td>{e.from_currency_code}</td>
                    <td class="cotacoes-table-price">R$ {parseFloat(e.value).toLocaleString('pt-BR', {maximumFractionDigits: 4})}</td>
                </tr>
            )
        );
        
        const cryptocurrencies_rows = this.state.cryptocurrencies.map((e) => 
            (
                <tr>
                    <td class="cotacoes-table-avatar">-</td>
                    <td>{e.name}</td>
                    <td>{e.symbol.toUpperCase()}</td>
                    <td class="cotacoes-table-price">R$ {parseFloat(e.value).toLocaleString('pt-BR', {minimumFractionDigits: 2, maximumFractionDigits: 2})}</td>
                </tr>
            )
        );

        const optionsDate = { year: 'numeric', month: 'numeric', day: 'numeric' };
        const date = new Date(this.state.lastUpdate).toLocaleDateString('pt-BR', optionsDate);
        const optionsTime = { hour: '2-digit', minute: '2-digit'};
        const time = new Date(this.state.lastUpdate).toLocaleTimeString('pt-BR', optionsTime);
        const sourceCurrencies = this.state.currenciesSource;
        const sourceCryptocurrencies = this.state.cryptocurrenciesSource;
        

        return (
            <div id="cotacoes">
                <div id="cotacoes-top">
                    <div id="cotacoes-top-left">
                        <i class="material-icons icon-dashboard-top" id="icon-cotacoes-color">monetization_on</i>
                        <h3 id="cotacoes-icon-title">Cotações</h3>
                    </div>
                    <div id="cotacoes-top-right">
                        <p id="cotacoes-top-right-update">
                            Atualizado em
                            <span class="cotacoes-top-date"> {date}</span> as 
                            <span class="cotacoes-top-date"> {time} (UTC-03:00)</span>
                        </p>
                    </div>
                </div>

                <div id="cotacoes-table">
                    <table id="cotacoes-table-tag">
                        <thead>
                            <tr>
                                <th id="cotacoes-table-ID">País/Região</th>
                                <th id="cotacoes-table-Moeda">Moeda</th>
                                <th id="cotacoes-table-Simbolo">Símbolo</th>
                                <th id="cotacoes-table-Valor">Valor</th>
                            </tr>
                        </thead>
                        <tbody>
                            {this.state.isCurrenciesLoaded === true ?
                                currencies_rows :
                                this.state.error}
                            {this.state.isCryptocurrenciesLoaded === true ?
                                cryptocurrencies_rows :
                                this.state.error}
                        </tbody>
                    </table>
                </div>

                <div id="cotacoes-bottom">
                    <p id="cotacoes-bottom-sources">Fontes: {sourceCurrencies} e {sourceCryptocurrencies}</p>
                    <a href={this.props.hrefCotacoes}>
                        <h2 id="cotacoes-bottom-more">Ver todas</h2>
                    </a>
                </div>
            </div>            
        );
    }
}