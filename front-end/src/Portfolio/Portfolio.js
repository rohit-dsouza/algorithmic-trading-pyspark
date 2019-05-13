import React from 'react';
import './Portfolio.css'
import TabRow from './TabRow/TabRow'

const portfolio = () => {
    return (
    <div className='Portfolio'>
        <table>
            <tr className="Headings"><td>Stockname</td><td>Number of Stocks</td><td>Buy Value</td><td>Sell Value</td><td>Current Market Value</td><td>Sentiment Value</td></tr>
            <TabRow/>
        </table>
    </div>
    )
};

export default portfolio;