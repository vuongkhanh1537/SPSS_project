import React, { useState } from 'react'
import PrevNextAction from '../../components/PrevNextAction/PrevNextAction'
import './Printers.scss'
import Printer from '../../assests/images/printer.png'
import { MdLocationOn } from 'react-icons/md'
import { HiQueueList } from 'react-icons/hi2'
import { FaClock, FaSearch } from 'react-icons/fa'
import { useDispatch } from 'react-redux'
import { removePrintingProperties } from '../../features/actions/printing-actions'

const printers = [
  {
    id: '1',
    name: 'HP LaserJet',
    address: 'CS2, H1, 404',
    status: 'ready',
    queue: []
  },
  {     
    id: '2',
    name: 'HP LaserJet',
    address: 'CS2, H1, 404',
    status: 'printing',
    queue: []
  },
  {
    id: '3',
    name: 'HP LaserJet',
    address: 'CS2, H1, 404',
    status: 'ready',
    queue: []
  },
  {
    id: '4',
    name: 'HP LaserJet',
    address: 'CS2, H1, 404',
    status: 'ready',
    queue: []
  },
  {
    id: '5',
    name: 'HP LaserJet',
    address: 'CS2, H1, 404',
    status: 'ready',
    queue: []
  },
  {
    id: '6',
    name: 'HP LaserJet',
    address: 'CS2, H1, 404',
    status: 'ready',
    queue: []
  },
]

function Printers() {
  const [selectedPrinterId, setSelectedPrinterId] = useState(printers[0].id);
  const dispatch = useDispatch();

  return (
    <div className='printers-page'>
      <h2>Chọn máy in</h2>
      <div className='search-box'>
        <FaSearch className='search-icon' />
        <input className='form-control' type='text' placeholder='Tìm kiếm' />
      </div>
      <div className='printer-list'>
        {
          printers.map((printer) => {
            const { id, name, address, status, queue } = printer;
            return (
              <div className={id === selectedPrinterId ? 'printer-item printer-item--active' : 'printer-item'} key={id}>
                <input type='radio' id={`printer-${id}`} className='printer-option' value={id} onChange={(e) => setSelectedPrinterId(e.target.value)} name='printer' />
                <label for={`printer-${id}`}>
                  <div className='printer-item--top'>
                    <h4>{ name }</h4>
                    <span className={status === 'ready' ? 'ready' : 'printing'}>{ status }</span>
                  </div>
                  <div className='printer-item--bottom'>
                    <img src={Printer} />
                    <div>
                      <div className='info-item'>
                        <MdLocationOn />
                        <span>{ address }</span>
                      </div>
                      <div className='info-item'>
                        <HiQueueList />
                        <span>Queue: </span>
                      </div>
                      {
                        status === 'printing' &&
                        <div className='info-item'>
                          <FaClock />
                          <span>1m59s/44m1s</span>
                        </div>
                      }
                    </div>
                  </div>
                </label>
              </div>
            )
          })
        }
      </div>
      <PrevNextAction prevLink='/' prevText='Tài liệu' nextLink='/print-status' nextText='Tiến hành in' nextAction={() => dispatch(removePrintingProperties())} />
    </div>
  )
}

export default Printers