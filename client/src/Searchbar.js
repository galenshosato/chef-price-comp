import { useState } from "react"
import Button from "react-bootstrap/esm/Button"
import Form from 'react-bootstrap/Form'
import InputGroup from 'react-bootstrap/InputGroup'

function Searchbar({house, setItems, houseObj, setLowPrice, setNoProduct}) {

    const vendorIds = houseObj[house]
    const [inputValue, setInputValue] = useState('')
    
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
    
    
    function onClick(e) {
    
        setItems([])

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