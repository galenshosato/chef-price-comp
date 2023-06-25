import React from 'react'
import { useState } from 'react';

import './App.css'
import Header from './Header';
import Houses from './Houses';
import Searchbar from './Searchbar';
import PriceDisplay from './PriceDisplay';
import LowPrice from './LowPrice';




function App() {

  const houseObj = {
    "The Dutch NYC": [1,2],
    "Locanda Verde": [1],
    "Lafayette": [2],
  }

  const [items, setItems] = useState([])
  const [house, setHouse] = useState()


  return (
    <>
      <Header />
      <LowPrice />
      <br></br>
      <br></br>
      <Houses setHouse={setHouse} />
      <br></br>
      <br></br>
      <Searchbar house={house} houseObj={houseObj} setItems={setItems} items={items}/>
      <br></br>
      <PriceDisplay items={items} />
    </> 
  )
}

export default App;
