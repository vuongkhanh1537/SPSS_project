import React from 'react'
import { Route, Routes } from 'react-router'
import PrintDocument from '../PrintDocument/PrintDocument'
import Printers from '../Printers/Printers'
import PrintStatus from '../PrintStatus/PrintStatus'
import PrinterMangement from '../PrinterManagement/PrinterMangement'
import AddPrinter from '../AddPrinter/AddPrinter'
import EditPrinter from '../EditPrinter/EditPrinter'
import PrintingHistory from '../PrintingHistory/PrintingHistory'
import Payment from '../Payment/Payment'

function AuthorizeRoutes() {
  return (
    <Routes>
      <Route index element={<PrintDocument />}></Route>
      <Route path='printers' element={<Printers />} ></Route>
      <Route path='print-status' element={<PrintStatus />} ></Route>
      <Route path='payment' element={<Payment />} ></Route>
      <Route path='printing-history' element={<PrintingHistory />} ></Route>
      <Route path='printer-management' element={<PrinterMangement />} ></Route>
      <Route path='add-printer' element={<AddPrinter />} ></Route>
      <Route path='edit-printer' element={<EditPrinter />} ></Route>
    </Routes>
  )
}

export default AuthorizeRoutes