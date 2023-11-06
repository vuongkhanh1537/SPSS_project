import React, {Component} from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/Login/Login';
import Hello from './pages/hello';
import LoginWithHCMUT_SSO from './pages/LoginWithHCMUT_SSO/LoginWithHCMUT_SSO';
import ProtectedRoute from './pages/ProtectedRoute/ProtectedRoute';
import axiosInstance from "./pages/axiosApi";

class App extends Component {

    constructor() {
        super();
        this.handleLogout = this.handleLogout.bind(this);
    }

    async handleLogout() {
        try {
            const response = await axiosInstance.post('/blacklist/', {
                "refresh_token": localStorage.getItem("refresh_token")
            });
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            axiosInstance.defaults.headers['Authorization'] = null;
            return response;
        }
        catch (e) {
            console.log(e);
        }
    };
	render(){
		return (
			<BrowserRouter>
				<Routes>
					<Route path='/*' element={<ProtectedRoute />} />
					<Route path="login" element={<Login />} />
					<Route path="hello" element={<Hello/>}/>
					<Route path="login_SSO" element={<LoginWithHCMUT_SSO />} />
				</Routes>
			</BrowserRouter>
		);
	}
}

export default App;
