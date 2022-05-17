import React, { createRef } from 'react';

export default class InputTimer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            time: this.props.time,
            status: this.props.status,
        };
        this.timerDisplay = React.createRef();
        this.inputElement = React.createRef();
        this.firstHour = React.createRef();
        this.secondHour = React.createRef();
        this.firstMinute = React.createRef();
        this.secondMinute = React.createRef();
        this.firstSecond = React.createRef();
        this.secondSecond = React.createRef();
        this.firstMSecond = React.createRef();
               
        // Event Functions
        this.clickDiv = this.clickDiv.bind(this);
        this.addTextCursor = this.addTextCursor.bind(this);
        this.inputBlur = this.inputBlur.bind(this);
        this.mask = this.mask.bind(this);
        this.onKeydown = this.onKeydown.bind(this);
        this.onKeyup = this.onKeyup.bind(this);

        // Functional Functions
        this.removeTextCursor = this.removeTextCursor.bind(this);
        this.addTextCursor = this.addTextCursor.bind(this);
        this.correctInputTime = this.correctInputTime.bind(this);
        this.removeAllTextCursor = this.removeAllTextCursor.bind(this);
        this.updateSpans = this.updateSpans.bind(this);
        this.checkAllowedChars = this.checkAllowedChars.bind(this);
        this.limitSize = this.limitSize.bind(this);
        this.controlSize = this.controlSize.bind(this);

    }
    
    clickDiv() {
        this.inputElement.current.setSelectionRange(7,7);
        this.inputElement.current.focus();
        this.setState({
            status: 'OFF',
        }, () => {
            this.props.onClick(this.state);
        });
    }

    removeTextCursor(selectionStart) {
        switch(selectionStart) {
            case 0:
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
            case 6:
            case 7:
                this.firstHour.current.classList.remove('text-cursor-left');
                this.firstHour.current.classList.remove('text-cursor-right');
                this.secondHour.current.classList.remove('text-cursor-right');
                this.firstMinute.current.classList.remove('text-cursor-right');
                this.secondMinute.current.classList.remove('text-cursor-right');
                this.firstSecond.current.classList.remove('text-cursor-right');
                this.secondSecond.current.classList.remove('text-cursor-right');
                this.firstMSecond.current.classList.remove('text-cursor-right');
                break;
        }
    }
    
    addTextCursor() {
        switch(this.inputElement.current.selectionStart) {
            case 0:
                this.firstHour.current.classList.add('text-cursor-left');
                break;
            case 1:
                this.firstHour.current.classList.add('text-cursor-right');
                break;
            case 2:
                this.secondHour.current.classList.add('text-cursor-right');
                break;
            case 3:
                this.firstMinute.current.classList.add('text-cursor-right');
                break;
            case 4:
                this.secondMinute.current.classList.add('text-cursor-right');
                break;
            case 5:
                this.firstSecond.current.classList.add('text-cursor-right');
                break;
            case 6:
                this.secondSecond.current.classList.add('text-cursor-right');
                break;
            case 7:
                this.firstMSecond.current.classList.add('text-cursor-right');
                break;
                
        }
    }

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
    
    removeAllTextCursor() {
        this.firstHour.current.classList.remove('text-cursor-left');
        this.firstHour.current.classList.remove('text-cursor-right');
        this.secondHour.current.classList.remove('text-cursor-right');
        this.firstMinute.current.classList.remove('text-cursor-right');
        this.secondMinute.current.classList.remove('text-cursor-right');
        this.firstSecond.current.classList.remove('text-cursor-right');
        this.secondSecond.current.classList.remove('text-cursor-right');
        this.firstMSecond.current.classList.remove('text-cursor-right');
    }    

    updateSpans(input) {
        this.firstHour.current.innerHTML = input[0];
        this.secondHour.current.innerHTML = input[1];
        this.firstMinute.current.innerHTML = input[2];
        this.secondMinute.current.innerHTML = input[3];
        this.firstSecond.current.innerHTML = input[4];
        this.secondSecond.current.innerHTML = input[5];
        this.firstMSecond.current.innerHTML = input[6];
    }
    
    inputBlur() {
        this.removeAllTextCursor();
    }

    // Verify new input data type and allow only
    checkAllowedChars(input, allowedChar) {
        input = input.match(allowedChar) || [];
        return input;
    }
    
    // Limit the size for new input values
    limitSize(input, maxSize) {
        if (input.length > maxSize) {
            input.shift();
        }
        return input;
    }
    
    // If length of the array is changed, this function recovers the last state
    controlSize(input) {
        if (input.length != this.inputElement.current.size) {
            input = this.state.time.split('');
        }
        return input;
    }

    mask() {
        const inputElement = this.inputElement;
        const size = inputElement.current.size;
        const startPos = inputElement.current.selectionStart;
        const endPos = inputElement.current.selectionEnd;
        const allowedChar = /\d/g;
        const notAllowedChar = /\D/g;
        
        let input;
        input = String(inputElement.current.value);
        input = this.checkAllowedChars(input, allowedChar);
        input = this.limitSize(input, size);
        input = this.controlSize(input);
        this.updateSpans(input);
        
        this.inputElement.current.value = input.join('');
        this.inputElement.current.selectionEnd = endPos-1;

        this.setState({
            time: input.join(''),            
        }, () => {
            this.props.onChange(this.state);
            
        });
        
    }

    onKeydown(event) {
        switch(event.key) {
            case 'Home':
            case 'End':
            case 'ArrowLeft':
            case 'ArrowRight':
                this.removeTextCursor(this.inputElement.current.selectionStart);
            break;
            case 'Backspace':
                let inputElem = this.inputElement.current.value.split('');
                let barPosition = this.inputElement.current.selectionEnd;
                if (inputElem.length <= this.inputElement.current.size && barPosition != 0) {
                    inputElem.splice(barPosition-1, 0, '0');
                    this.inputElement.current.value = inputElem.join('');
                    this.inputElement.current.selectionEnd = barPosition+1;
                }
                this.removeAllTextCursor();
                // this.removeTextCursor(this.inputElement.current.selectionStart);
                break;
            case 'Delete':
                if (!event.ctrlKey && !event.shiftKey) {
                    let inElem = this.inputElement.current.value.split('');
                    let barStartPos = this.inputElement.current.selectionEnd;
                    let barEndPos = this.inputElement.current.selectionEnd;
                    let selectionRange = Math.abs(this.inputElement.current.selectionStart - this.inputElement.current.selectionEnd);
                    if (inElem.length <= this.inputElement.current.size && barStartPos != this.inputElement.current.size) {
                        const qtyOfZeros = Array(selectionRange).fill('0');
                        inElem.splice(barEndPos, 0, '0');
                        this.inputElement.current.value = inElem.join('');
                        this.inputElement.current.selectionEnd = barEndPos+1;
                        break;
                }         
                } else {
                    this.inputElement.current.value = this.state.time;
                }
        }        
    }

    onKeyup(event) {
        switch(event.key) {
            case 'Home':
            case 'End':
            case 'ArrowLeft':
            case 'ArrowRight':
            case 'Backspace':
                this.addTextCursor(this.inputElement.current.selectionStart);
            break;
        };
    }


    componentDidMount() {
        this.inputElement.current.value = this.state.time;
    }

    componentWillReceiveProps(nextProps) {
        this.setState({
            time: nextProps.time,
            status: nextProps.status,
        }, () => {
            this.inputElement.current.value = this.state.time;
        });
    }

    render() {
        

        return (
            <div id="timer-display" ref={this.timerDisplay} onClick={this.clickDiv}>
                <div className="timer">
                    <span id='1-hour' className="hour-span text" ref={this.firstHour}>{this.state.time[0]}</span>
                    <span id='2-hour' className="hour-span text" ref={this.secondHour}>{this.state.time[1]}</span>
                    <span class="colon-span text">:</span>
                    <span id='1-minute' className="minute-span text" ref={this.firstMinute}>{this.state.time[2]}</span>
                    <span id='2-minute' className="minute-span text" ref={this.secondMinute}>{this.state.time[3]}</span>
                    <span class="colon-span text">:</span>
                    <span id='1-second' className="seconds-span text" ref={this.firstSecond}>{this.state.time[4]}</span>
                    <span id='2-second' className="seconds-span text" ref={this.secondSecond}>{this.state.time[5]}</span>
                    <span class="period-span text">.</span>
                    <span id='1-msecond' className="miliseconds-span text" ref={this.firstMSecond}>{this.state.time[6]}</span>
                    <span className="seconds-symbol-span text">s</span>
                </div>
                <input id="input-tempo-timer-display-time"
                        type="text"
                        placeholder={this.state.time}
                        size="7"
                        ref={this.inputElement}
                        onFocus={this.addTextCursor}
                        onBlur={this.inputBlur}
                        onInput={this.mask}
                        onKeyDown={this.onKeydown}
                        onKeyUp={this.onKeyup}
                />

            </div>                
        );
    }

}