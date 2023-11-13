import React from 'react'
import PrevNextAction from '../../components/PrevNextAction/PrevNextAction'
import { PiClockCounterClockwise } from 'react-icons/pi'
import './PrintStatus.scss'

function PrintStatus() {
  return (
    <div className='print-status-page'>
        <h2>Tiến hành in</h2>
        <div className='content'>
          <PiClockCounterClockwise className='icon' />
          <p className='status'>Hệ thống đã nhận được yêu cầu!</p>
          <p className='estimate-time'>Thời gian hoàn thành dự kiến: 5p</p>
        </div>
    </div>
  )
}

export default PrintStatus