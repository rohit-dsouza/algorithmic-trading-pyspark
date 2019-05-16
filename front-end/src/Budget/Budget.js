import React from 'react';
import './Budget.css'

const budget = (props) => {
    return (
        <div className='Budget'>
            <form>
                <p>Enter the total amount that is available for transactions</p>
                <br />
                <input type="text" id="amount" />
                <br />
                <button type="button" onClick={props.functionHandle}>Submit</button>
            </form>
        </div>
    )
};

export default budget;