import React from 'react'
import PrinterIntro from '../../assests/images/printer-intro.png'
import LogoHCMUT from '../../assests/images/LogoHCMUT.png'
import './login.scss'
import { Link } from 'react-router-dom'
import LoginWithHCMUT_SSO from '../LoginWithHCMUT_SSO/LoginWithHCMUT_SSO'

function Login() {
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
                        <input type="text" className="form-control" id="username" name='username' placeholder="" />
                    </div>
                    <div className="mb-3">
                        <label for="password" className="form-label">Mật khẩu</label>
                        <input type="password" className="form-control" name='password' id="password" />
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
                        <button className="btn btn-primary login-btn-1" type="button">Đăng nhập</button>
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