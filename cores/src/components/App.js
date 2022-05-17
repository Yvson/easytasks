import React from 'react';
import ReactDOM from 'react-dom';
import { SketchPicker, BlockPicker } from 'react-color';
import ColorMath from './colorMath';


export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            color: {
                hex: '#000000',
                rgb: {
                    r: String(Math.floor(Math.random() * 256)),
                    g: String(Math.floor(Math.random() * 256)),
                    b: String(Math.floor(Math.random() * 256)),
                    a: '1',
                },
                hsl: {
                    h: Math.floor(Math.random() * 360),
                    s: Math.random(),
                    l: Math.random(),
                    a: 1,
                },
            },
            presetColorsSketch: [
                '#345E82', '#4D7C8A', '#668C90', '#7F9C96', '#87A58F', '#8FAD88', '#ADC68C', '#CBDF90', '#C3C3E6', '#CAC6E4', '#D1C8E1', '#BBA0CA', '#B788BD', '#B370B0', '#9D4B86', '#87255B', '#92396A', '#CACAAA', '#DCC897', '#E5C78E', '#EEC584', '#DBB884', '#C8AB83', '#8F9988', '#55868C', '#6A757D', '#7F636E', '#DBCDC6', '#E3D2CC', '#E7D5CF', '#EAD7D1', '#E4B8C6', '#DD99BB', '#AC7595', '#7B506F', '#1F1A38', '#FBAF00', '#FDC31D', '#FFD639', '#FFBD74', '#FFA3AF', '#8090B7', '#007CBE', '#00AF54', '#17B664', '#C52233', '#B51F32', '#A51C30', '#A62838', '#A7333F', '#8E232E', '#74121D', '#660F1E', '#580C1F', '#672233', '#252323', '#4B4E58', '#5E6472', '#70798C', '#F5F1ED', '#E8E2D5', '#DAD2BC', '#C2B6A1', '#A99985', '#FCAA67', '#D67653', '#B0413E', '#D8A083', '#FFFFC7', '#AAC3A7', '#548687', '#4E5D5E', '#473335', '#584647', '#98CE00', '#57D75F', '#16E0BD', '#47D2DC', '#78C3FB', '#81B5FB', '#89A6FB', '#9195C5', '#98838F', '#A18E99', '#293132', '#38393B', '#474044', '#4B4955', '#4F5165', '#526685', '#547AA5', '#52A9BE', '#50D8D7', '#BFACAA', '#61575A', '#02020A', '#04112A', '#05204A', '#5D5C90', '#B497D6', '#CBBDE3', '#E1E2EF', '#E4E5F0', '#F45B69', '#F5A2AA', '#F6E8EA', '#8C8083', '#22181C', '#3E0C0F', '#5A0001', '#A61819', '#F13030', '#F24343', '#00072D', '#001241', '#001C55', '#052064', '#0A2472', '#0C488D', '#0E6BA8', '#5AA6D1', '#A6E1FA', '#AEE4FA', '#B5E6FA',
                '#000000', '#FFFFFF'
            ],
            presetColorsBlock: [
                '#FF0A22', '#0FFF00', '#0013FF', '#FFF300',
            ],
            savedColors: props.colors.map((item) => item.fields.color),
            savedColorsIds: props.colors.map((item) => item.pk),

        }
        this.handleChange = this.handleChange.bind(this);
        this.generateColor = this.generateColor.bind(this);
        this.saveColor = this.saveColor.bind(this);
        this.deleteColors = this.deleteColors.bind(this);

    }

    handleChange(color) {
        this.setState({
            color: color
        });
    }

    handleChangeComplete = (color) => {
        this.setState({
            color: color
        });
    };

    generateColor() {
        this.setState({
            color: {
                hsl: {
                    h: Math.floor(Math.random() * 360),
                    s: Math.random(),
                    l: Math.random(),
                    a: Math.random(),
                }
            }
        });
    }

    saveColor() {
        this.props.saveColor(ColorMath.HSLToHex(this.state.color.hsl.h, 100 * this.state.color.hsl.s, 100 * this.state.color.hsl.l));
    }


    deleteColors() {
        this.props.deleteColors(this.state.savedColorsIds);
    }

    render() {
        let section;
        const analogous = [
            { h: ColorMath.loopHue(this.state.color.hsl.h - 60), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h - 30), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h + 30), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h + 60), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
        ];
        const monochromatic = [
            { h: ColorMath.loopHue(this.state.color.hsl.h), s: this.state.color.hsl.s - 0.50, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h), s: this.state.color.hsl.s - 0.35, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h), s: this.state.color.hsl.s - 0.25, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h), s: this.state.color.hsl.s - 0.15, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
        ];
        const triadic = [
            { h: ColorMath.loopHue(this.state.color.hsl.h - 120), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h + 120), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
        ];
        const complementary = [
            { h: ColorMath.loopHue(this.state.color.hsl.h + 180), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
        ];
        const tetradic = [
            { h: ColorMath.loopHue(this.state.color.hsl.h + 60), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h + 180), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
            { h: ColorMath.loopHue(this.state.color.hsl.h + 240), s: this.state.color.hsl.s, l: this.state.color.hsl.l, a: this.state.color.hsl.a },
        ];


        switch (this.props.section) {
            case 'analogo':
                section = [...analogous];
                break;
            case 'monocromatico':
                section = [...monochromatic];
                break;
            case 'triade':
                section = [...triadic];
                break;
            case 'complementar':
                section = [...complementary];
                break;
            case 'quadrado':
                section = [...tetradic];
                break;

        }

        const systemColors = [];
        for (let i = 0; i < section.length; i++) {
            systemColors.push(
                <BlockPicker
                    color={section[i]}
                    onChange={this.handleChange}
                    triangle='hide'
                    width='inherit'
                    colors={this.state.presetColorsBlock}
                />
            );
        };
        const someColors = ['#7B506F', '#1F1A38', '#FBAF00', '#FDC31D'];

        let savedColors = [];

        let bulk = [];
        for (let item in this.state.savedColors) {
            bulk.push(
                <BlockPicker
                    color={this.state.savedColors[item]}
                    onChange={this.handleChange}
                    triangle='hide'
                    width='inherit'
                    colors={[]}
                />
            );

            if ((parseInt(item) + 1) % 6 === 0 || ((parseInt(item) + 1) === this.state.savedColors.length)) {
                savedColors.push(bulk);
                bulk = [];

            }
        }


        const displaySavedColors = savedColors.map((colorItem) =>
            <div className="cores-grid-6-pack">
                {colorItem}
            </div>
        );

        return (
            <div id="cores-grid-app">
                <div id="cores-grid-color-picker">
                    <div id="color-sketch-picker">
                        <SketchPicker
                            color={this.state.color.hsl}
                            onChange={this.handleChange}
                            width='inherit'
                            presetColors={this.state.presetColorsSketch}
                        />
                    </div>
                    <div id="cores-grid-buttons">
                        <div id="cores-grid-one-button">
                            <button onClick={this.generateColor} id="cores-grid-generate-button">Gerar Cor</button>
                        </div>
                        <div id="cores-grid-two-buttons">
                            <button onClick={this.saveColor} id="cores-grid-save-button">Salvar Cor</button>
                            <button onClick={this.deleteColors} id="cores-grid-delete-button">Deletar Cores</button>
                        </div>
                    </div>
                </div>

                <div id="cores-grid-color-system">
                    {systemColors}
                </div>

                <div id="cores-grid-saved-colors">
                    <div id="saved-colors-title">
                        <h2>Cores Salvas</h2>
                        <hr></hr>
                        <p>Limite Máximo: 18 itens</p>
                    </div>
                    
                    <div id="saved-colors-items">
                        {displaySavedColors}
                    </div>
                </div>

            </div>
        );
    }
}


ReactDOM.render(
    <App
        section={window.section}
        colors={window.colors}
        saveColor={window.saveColor}
        deleteColors={window.deleteColors}
    />,
    window.react_mount
);

