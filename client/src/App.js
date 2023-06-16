import React from 'react'
import { useState } from 'react';

import './App.css'
import Header from './Header';
import Houses from './Houses';
import Searchbar from './Searchbar';
import PriceDisplay from './PriceDisplay';




function App() {

  const houseObj = {
    "The Dutch NYC": [1,2,3],
    "Locanda Verde": [2,3],
    "Joe's Pub": [3],
    "Lafayette": [1,3],
  }

  const [items, setItems] = useState([])
  const [house, setHouse] = useState()


  return (
    <>
      <Header />
      <br></br>
      <br></br>
      <Houses setHouse={setHouse} />
      <br></br>
      <br></br>
      <Searchbar house={house} houseObj={houseObj} setItems={setItems}/>
      <PriceDisplay items={items} />
    </> 
  )
}

export default App;
