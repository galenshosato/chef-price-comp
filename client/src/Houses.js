import { useState } from 'react'
import ToggleButton from 'react-bootstrap/ToggleButton'
import ButtonGroup from 'react-bootstrap/ButtonGroup'


function Houses ({setHouse}) {
    const [radioValue, setRadioValue] = useState('')

    const nhgHouses = [
        { name: "The Dutch NYC", value: '1' },
        { name: "Locanda Verde", value: '2'},
        { name: "Lafayette", value: '3'},
    ]


    return (
        <ButtonGroup aria-label='Basic Example'>
            {nhgHouses.map((house, idx) => {
                return <ToggleButton 
                          key={idx}
                          id={`radio-${idx}`}
                          type='radio' 
                          onClick={() => setHouse(house.name)} 
                          variant='outline-secondary'
                          name='radio'
                          value={house.value}
                          checked={radioValue === house.value}
                          onChange={(e) => setRadioValue(e.currentTarget.value)}>
                    {house.name}
                    </ToggleButton>
            })}
        </ButtonGroup>
    )
}

export default Houses