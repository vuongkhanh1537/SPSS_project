import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/Login/Login';
import LoginWithHCMUT_SSO from './pages/LoginWithHCMUT_SSO/LoginWithHCMUT_SSO';
import ProtectedRoute from './pages/ProtectedRoute/ProtectedRoute';
import Sidebar from './components/Sidebar/Sidebar';
import AuthorizeRoutes from './pages/AuthorizeRoutes/AuthorizeRoutes';
import Navbar from './components/Navbar/Navbar';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
	return (
		<div className='App'>
			<BrowserRouter>
				<Routes>
					<Route 
						path='/*' 
						element={
							<ProtectedRoute>
								<Sidebar />
								<div style={{paddingLeft: '60px', paddingRight: '60px'}}>
									<Navbar />
									<AuthorizeRoutes />
								</div>
							</ProtectedRoute>
						} 
					/>
					<Route path="login" element={<Login />} />
					<Route path="login_SSO" element={<LoginWithHCMUT_SSO />} />
				</Routes>
			</BrowserRouter>
			<ToastContainer position='top-right' />
		</div>
	);
}

export default App;
