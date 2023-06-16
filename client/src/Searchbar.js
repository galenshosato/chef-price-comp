import Button from "react-bootstrap/esm/Button"
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup'

function Searchbar({house, setItems, houseObj}) {

    const vendorIds = houseObj[house]
    
    function onSubmit(e) {
        // Clear setItems
        // Build fetch in a loop around vendorIds
        // "/api/{vendorId}/products/{searchTerm}"
        // Append to setItems
    }



    return (
        <>
            <InputGroup className="mb-3">
                <Form.Control 
                    placeholder = "Enter Items"
                />
                <Button variant="secondary">
                    Submit
                </Button>
            </InputGroup>
        </>
    )
}

export default Searchbar