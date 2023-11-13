import React from 'react'
import { Route, Routes } from 'react-router'
import PrintDocument from '../PrintDocument/PrintDocument'
import Printers from '../Printers/Printers'
import PrintStatus from '../PrintStatus/PrintStatus'

function AuthorizeRoutes() {
  return (
    <Routes>
      <Route index element={<PrintDocument />}></Route>
      <Route path='printers' element={<Printers />} ></Route>
      <Route path='print-status' element={<PrintStatus />} ></Route>
    </Routes>
  )
}

export default AuthorizeRoutes