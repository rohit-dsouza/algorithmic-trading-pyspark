import React from 'react';
import './Profit.css'

const profit = (props) => {
    let style1, val;
    if(props.value>0){
        style1 = {
            color:  'green'
        };
        val = props.value;
    }
    else{
        style1 = {
            color:  'red'
        };
        val = -props.value;
    }
    return (
    <div className='Profit'>
        <h4>Profit/Loss:</h4>
        <h1 style={style1}>${val}</h1>
    </div>
    )
};

export default profit;