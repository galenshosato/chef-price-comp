import { useState } from "react"
import Button from "react-bootstrap/esm/Button"
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup'

function Searchbar({house, setItems, houseObj}) {

    const vendorIds = houseObj[house]
    const [inputValue, setInputValue] = useState('')
    
    
    function onClick(e) {
    
        setItems([])

        Promise.all(
            vendorIds.map(id =>
              fetch(`/api/${id}/products/${inputValue}`)
                .then(resp => resp.json())
            )
        )
            .then(dataArray => {
                const newItems = dataArray[0]
                setItems(newItems)
            })
            .catch(error => {
                console.error('Error fetching data:', error)
            })
        
        
    }

    function onChange(e) {
        setInputValue(e.target.value)
    }



    return (
        <div>
            <InputGroup className="d-flex justify-content-center" style={{width: '500px'}}>
                <Form.Control 
                    placeholder = "Enter Item"
                    type='text'
                    value={inputValue}
                    onChange={onChange}
                />
                <Button variant="secondary" onClick={onClick}>
                    Submit
                </Button>
            </InputGroup>
        </div>
    )
}

export default Searchbar