import React from 'react'
import { useSelector } from 'react-redux'
import { Navigate } from 'react-router-dom';
import './protectedRoute.scss'

function ProtectedRoute({ children }) {
	const { user } = useSelector((state) => state.auth);

	if (!user) {
		return <Navigate to='/login' />
	}
	return (
		<div className='app-container'>
			{ children }
		</div>
	)
}

export default ProtectedRoute