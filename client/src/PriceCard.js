import Card from 'react-bootstrap/Card'

function PriceCard ({item}) {
    //Adds the unit to the price
    const ogPrice=item.prices[0].price
    const priceUnit = ogPrice.slice(-2)
    



    //This sets the date in a easier to read time
    const datestring = item.prices[0].updated_at
    const date = new Date(datestring)
    const options = {
        month: '2-digit',
        day: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }
    const formattedDate = date.toLocaleString('en-US', options)
    const [datePart, timePart] = formattedDate.split(', ')

    return (
        <>
            <Card style={{width: '425px'}} className='mb-3'>
                <Card.Body>
                    <Card.Title className = 'd-flex justify-content-center'>{item.name}</Card.Title>
                    <Card.Subtitle className='d-flex justify-content-center'>{item.vendor}</Card.Subtitle>
                    <Card.Subtitle className='d-flex justify-content-center'>{item.unique_id}</Card.Subtitle>
                    <Card.Body>
                        <div className='d-flex justify-content-center'>
                            {item.prices[0].price}<br />
                        </div>
                        <div className='d-flex justify-content-center'>
                            ${item.prices[0].price_per_unit} per {priceUnit}
                        </div>
                    </Card.Body>
                    <Card.Footer className='d-flex justify-content-center'>Price Changed: {timePart} on {datePart}</Card.Footer>
                </Card.Body>
            </Card>
        </>
    )
}

export default PriceCard