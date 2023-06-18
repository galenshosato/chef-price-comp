import Card from 'react-bootstrap/Card'

function PriceCard ({item}) {

    // Build Card

    return (
        <>
            <Card>
                <Card.Body>
                    <Card.Title>Title of Item</Card.Title>
                    <Card.Subtitle>Title of Vendor</Card.Subtitle>
                    <Card.Body>Price</Card.Body>
                    <Card.Body>Price Per Unit</Card.Body>
                    <Card.Footer>Updated At:</Card.Footer>
                </Card.Body>
            </Card>
        </>
    )
}

export default PriceCard