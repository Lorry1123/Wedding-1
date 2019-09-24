
import React from 'react';

const LotteryPage = (props) => {
    return (
        <h1>
            hello world!
        </h1>
    )
}

const domContainer = document.querySelector('#react-root');
ReactDOM.render(<LotteryPage/>, domContainer);