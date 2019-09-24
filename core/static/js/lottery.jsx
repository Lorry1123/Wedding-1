const { useState } = React;

const LotteryPage = (props) => {
    return (
        <h1>
            hello world!
        </h1>
    )
}

const domContainer = document.querySelector('#react-root');
ReactDOM.render(<LotteryPage/>, domContainer);