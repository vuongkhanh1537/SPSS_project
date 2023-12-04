import React, { useState } from 'react'
import { IoNotificationsOutline } from 'react-icons/io5'
import { HiOutlineUserCircle } from 'react-icons/hi2'
import './Navbar.scss'
import { useDispatch } from 'react-redux';
import { FaCaretDown, FaUserCircle } from 'react-icons/fa';
import { logout } from '../../features/actions/auth-actions';

function Navbar() {
  const [showLogout, setShowLogout] = useState(false);
  const dispatch = useDispatch();

  return (
    <div className='navbar'>
        <div></div>
        <div className='nav-actions'>
            <IoNotificationsOutline className='icon' />
            <div className='btn-container'>
              <button onClick={() => setShowLogout(!showLogout)} className='user-btn bttn'>
                <FaUserCircle />
                Student
                <FaCaretDown />
              </button>
              <div className={showLogout ? 'logout show-logout' : 'logout'} >
                <button onClick={() => dispatch(logout())} className='bttn'>
                  Logout
                </button>
              </div>
            </div>
        </div>
    </div>
  )
}

export default Navbar