import { useState } from "react"
import Button from "react-bootstrap/esm/Button"
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup'

function Searchbar({house, setItems, houseObj, setLowPrice, setNoProduct}) {

    const vendorIds = houseObj[house]
    const [inputValue, setInputValue] = useState('')
    const [isChecked, setIsChecked] = useState(false)
    
    function getLowestItem (arr) {
        let lowest = 100000
        let minItem = {}
    
        for (const item of arr) {
          let price = item.prices[0].price_per_unit
          
          if (price < lowest) {
            lowest = price
            minItem = item
          }
        }
        return minItem
      }

    function handleCheckboxChange(e) {
        setIsChecked(prevState => !prevState)
    }
    
    function onClick(e) {
    
        setItems([])

        if (isChecked === true) {
            console.log("This is the exact product")
        }

        else {
            Promise.all(
                vendorIds.map(id =>
                fetch(`/api/${id}/products/${inputValue}`)
                    .then(resp => resp.json())
                )
            )
                .then(dataArray => {
                    let newItems = []

                    for (let i = 0; i < dataArray.length; i++) {
                        if (dataArray[i]['Error'] === 'No products match that query') {
                            continue
                        }
                        newItems = newItems.concat(dataArray[i])
                    }

                    if (newItems.length === 0) {
                        setNoProduct(true)
                        setLowPrice(false)
                        return
                    }
                    else {
                        setNoProduct(false)
                        setItems(newItems)
                        return newItems }
                })
                .then(data => {
                    const minItem = getLowestItem(data)
                    setLowPrice(minItem)
                })
                .catch(error => {
                    console.error('Error fetching data:', error)
                })}
    }

    function onChange(e) {
        setInputValue(e.target.value)
    }



    return (
        <div style={{ display: 'flex', alignItems: 'center' }}>
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
            <div style={{ marginLeft: '100px', transform: 'scale(1.3)' }}>
                <label>
                    <input 
                        type='checkbox'
                        checked={isChecked}
                        onChange={handleCheckboxChange}
                    />
                    <span style={{ marginLeft: '5px' }}>Exact product</span>
                </label>
            </div>
        </div>
    )
}

export default Searchbar