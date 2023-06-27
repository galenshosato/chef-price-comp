import Card from 'react-bootstrap/Card'

function LowPriceCard ({item}) {
    //Adds the unit to the price
    const ogPrice=item.prices[0].price
    const priceUnit = ogPrice.slice(-2)
    
    return (
        <>
            <Card style={{width: '425px',
                          position: 'fixed',
                          top: 5,
                          right: 10,
                          zIndex: 9999,}}
                          className='mb-3'>
                <Card.Header className = 'd-flex justify-content-center' style={{backgroundColor:'green'}}><strong>Cheapest Option</strong></Card.Header>
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
                </Card.Body>
            </Card>
        </>
    )
}

export default LowPriceCard