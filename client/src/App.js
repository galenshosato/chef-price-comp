import React from 'react'
import { useState } from 'react';

import './App.css'
import Header from './Header';
import Houses from './Houses';
import Searchbar from './Searchbar';
import PriceDisplay from './PriceDisplay';




function App() {

  const [items, setItems] = useState([])
  const [house, setHouse] = useState()

  return (
    <>
      <Header />
      <Houses house={house} setHouse={setHouse} />
      <Searchbar house={house} setItems={setItems}/>
      <PriceDisplay items={items} />
    </> 
  )
}

export default App;
