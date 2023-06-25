import Alert from 'react-bootstrap/Alert'
import LowPriceCard from './LowPriceCard'

function LowPrice ({ lowPrice }) {


    return (
        <>
            {lowPrice ? <LowPriceCard item={lowPrice} /> : null } 
        </>
    )
}

export default LowPrice