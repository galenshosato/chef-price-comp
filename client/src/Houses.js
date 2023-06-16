import Button from 'react-bootstrap/Button'
import ButtonGroup from 'react-bootstrap/ButtonGroup'


function Houses ({setHouse}) {

    const nhgHouses = ["The Dutch NYC", "Locanda Verde", "Joe's Pub", "Lafayette"]

    return (
        <ButtonGroup aria-label='Basic Example'>
            {nhgHouses.map((indHouse) => {
                return <Button key={indHouse} onClick={() => setHouse(indHouse)} variant='secondary'>
                    {indHouse}
                    </Button>
            })}
        </ButtonGroup>
    )
}

export default Houses