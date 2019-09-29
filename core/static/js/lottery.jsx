const { useState, useEffect } = React;

const LotteryPage = (props) => {
    // const [users, setUsers] = useState([]);
    // const [winner, setWinner] = useState({nick: '???', avatar: ''});
    const [disable, setDisable] = useState(false);
    const [flash_user, setFlashUser] = useState({nick: '???', avatar: ''});

    // let winner = {nick: '???', avatar: ''};

    // useEffect(() => {
    //     getWinners();
    // }, []);

    const getWinners = () => {
        if (disable) {
            return;
        }

        setDisable(true);

        $.post('/wedding/users', {}, (res) => {
            console.log(res);
            // setUsers(res.users);
            // setWinner(res.winner);
            // winner = res.winner;
            
            start_flash_user(0, res.users, res.winner);
        });
    }

    const start_flash_user = (cnt, users, winner) => {
        if (cnt >= 20) {
            setDisable(false);
            setFlashUser(winner);
            return;
        }

        const rand = Math.floor(Math.random() * users.length);
        console.log(rand, users.length, );
        setFlashUser(users[rand]);

        setTimeout(() => {
            start_flash_user(cnt + 1, users, winner);
        }, 100);
    }

    return (
        <div style={{width: '100%', height: 0, paddingTop: '75%', position: 'static', background: "url('https://wedding-1257884187.cos.ap-chengdu.myqcloud.com/00015.jpg')",
             backgroundSize: 'cover'}}>
        
            <div className="panel panel-default" style={{maxWidth: '300px', width: '20%', textAlign: 'center', position: 'absolute', top: '15%', right: '15%', opacity: '30%'}}>
                <div className="panel-heading">幸运抽奖</div>
                <div className="panel-body">
                    <div>
                        <span style={{display: 'block', marginBottom: '10px'}}>
                            {flash_user.nick}
                        </span>
                        <img src={flash_user.avatar} style={{maxWidth: '70%'}}/>
                    </div>
                    <div style={{marginTop: '10px'}}>
                        <button className="btn btn-default" disable={disable} onClick={getWinners}>抽奖</button>
                    </div>
                </div>
            </div>
            
        </div>
    )
}

const domContainer = document.querySelector('#react-root');
ReactDOM.render(<LotteryPage />, domContainer);