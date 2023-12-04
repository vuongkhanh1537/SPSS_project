import React, { useState, Component, useEffect } from 'react'
import React, { useEffect, useState } from 'react'
import PrinterIntro from '../../assests/images/printer-intro.png'
import LogoHCMUT from '../../assests/images/LogoHCMUT.png'
import './login.scss'
import { Link, useNavigate } from 'react-router-dom'
import LoginWithHCMUT_SSO from '../LoginWithHCMUT_SSO/LoginWithHCMUT_SSO'
import { useDispatch, useSelector } from 'react-redux'
import { login } from '../../features/actions/auth-actions'
import { toast } from 'react-toastify'
import axiosInstance from "../axiosApi";


function Login() {
    const [formData, setFormData] = useState({ username: '', password: '' });
    const dispatch = useDispatch();
    const { user } = useSelector((state) => state.auth);
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleSubmit = () => {
        if (!formData.username || !formData.password) {
            toast.warning('Vui lòng điền đầy đủ thông tin')
        } else {
            dispatch(login(formData.username, formData.password))
        }
    }

    useEffect(() => {
		if (user) {
            setTimeout(() => {
                navigate('/');
            }, 2000);
		}
	}, [user]);

    return (
        <div className='login'>
            <div className="login-content">
                <div className='mb-5 title'>
                    <h2>
                        <img src={LogoHCMUT} />
                        <span>Smart Printing Service</span>
                    </h2>
                    <p className='desc'>Chào mừng bạn đến với dịch vụ in thông minh dành cho sinh viên</p>
                </div>
                <div className='form'>
                    <div className="mb-3">
                        <label for="username" className="form-label">Tên đăng nhập</label>
                        <input type="text" className="form-control" id="username" name='username' placeholder="" onChange={handleChange} />
                    </div>
                    <div className="mb-3">
                        <label for="password" className="form-label">Mật khẩu</label>
                        <input type="password" className="form-control" name='password' id="password" onChange={handleChange} />
                    </div>
                    <div className='mb-5 d-flex justify-content-between'>
                        <div className="form-check">
                            <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"/>
                            <label className="form-check-label" for="flexCheckDefault">
                                Lưu đăng nhập
                            </label>
                        </div>
                        <span style={{color: '#4B9CFC'}}>Quên mật khẩu</span>
                    </div>
                    <div className="d-grid gap-2">
                        <button className="btn btn-primary login-btn-1" type="button" onClick={handleSubmit}>Đăng nhập</button>
                        <Link className='d-block' to='/login_SSO'>
                            <button className="btn btn-primary login-btn-2" type="button">
                                <img src={LogoHCMUT} />
                                <span>Xác thực với HCMUT_SSO</span>
                            </button>
                        </Link>
                    </div>
                </div>
            </div>
            <div className="login-img">
                <img src={PrinterIntro} />
            </div>
        </div>
    )
}

export default Login