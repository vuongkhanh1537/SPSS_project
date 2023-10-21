import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/Login/Login';
import LoginWithHCMUT_SSO from './pages/LoginWithHCMUT_SSO/LoginWithHCMUT_SSO';
import ProtectedRoute from './pages/ProtectedRoute/ProtectedRoute';

function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route path='/*' element={<ProtectedRoute />} />
				<Route path="login" element={<Login />} />
				<Route path="login_SSO" element={<LoginWithHCMUT_SSO />} />
			</Routes>
		</BrowserRouter>
	);
}

export default App;
