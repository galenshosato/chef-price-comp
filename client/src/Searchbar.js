import { useState } from "react"
import Button from "react-bootstrap/esm/Button"
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup'

function Searchbar({house, setItems, houseObj}) {

    const vendorIds = houseObj[house]
    const [inputValue, setInputValue] = useState('')
    
    function onClick(e) {
        // Clear setItems
        // Build fetch in a loop around vendorIds
        // "/api/{vendorId}/products/{searchTerm}"
        // Append to setItems

        setItems([])

        fetch(`/api/1/products/${inputValue}`)
        .then(resp => resp.json())
        .then(data => setItems(data))
    }

    function onChange(e) {
        setInputValue(e.target.value)
    }



    return (
        <>
            <InputGroup className="mb-3">
                <Form.Control 
                    placeholder = "Enter Items"
                    type='text'
                    value={inputValue}
                    onChange={onChange}
                />
                <Button variant="secondary" onClick={onClick}>
                    Submit
                </Button>
            </InputGroup>
        </>
    )
}

export default Searchbar