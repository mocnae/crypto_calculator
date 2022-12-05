import React, {useEffect, useState} from "react";

function List(){
    const [list, setList] = useState([]);
    const [base, setBase] = useState('USDT');
    const [quote, setQuote] = useState('BTC');
    const [res, setRes] = useState(0);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/currencys/')
            .then((response) => response.json())
            .then(({data}) => {
                setList(data);
                console.log(data);
            });
    }, [])

    const handleSubmit = (event) => {
        event.preventDefault()
        const baseItem = list.filter(obj => obj.name == base)[0]
        const quoteItem = list.filter(obj => obj.name == quote)[0]
        setRes(+(baseItem.quote_usdt) / +(quoteItem.quote_usdt))
        console.log(baseItem.quote_usdt)
        console.log(quoteItem.quoteItem)
    }

    return (
        <form onSubmit={handleSubmit} className="form">
            <p>{base}</p>
            <p>{quote}</p>
            <label>
                Choose pair:
                <select value={base} onChange={(event) => setBase(event.target.value)}>
                    {
                        list.map(obj => {
                            return <option value={obj.name} key={obj.pk}>{obj.name}</option>
                        })
                    }
                </select>

                <select value={quote} onChange={(event) => setQuote(event.target.value)}>
                    {
                        list.map(obj => {
                            return <option value={obj.name} key={obj.pk}>{obj.name}</option>
                        })
                    }
                </select>
            </label>
            <input type="submit" value="Посчитать" />
            <p>{res}</p>
        </form>
      );
}

export default List;