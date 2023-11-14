import React from 'react'
import { IoNotificationsOutline } from 'react-icons/io5'
import { HiOutlineUserCircle } from 'react-icons/hi2'
import './Navbar.scss'

function Navbar() {
  return (
    <div className='navbar'>
        <div></div>
        <div className='nav-actions'>
            <IoNotificationsOutline className='icon' />
            <div className='user'>
                <HiOutlineUserCircle className='icon' />
                <span>Student</span>
            </div>
        </div>
    </div>
  )
}

export default Navbar