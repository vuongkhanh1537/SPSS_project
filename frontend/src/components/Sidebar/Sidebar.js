import React from 'react'
import LogoHCMUT from '../../assests/images/LogoHCMUT.png'
import { studentRoutes } from './Sidebar-const';
import { Link } from 'react-router-dom';
import './Sidebar.scss';
import { useSelector } from 'react-redux';

function Siderbar() {
	// const { isSidebarOpen } = useSelector((state) => state.user);

	return (
		<div className='sidebar'>
			<div className='sidebar-container'>
				<header>
					<img src={LogoHCMUT} />
					<span>SPSS</span>
				</header>
				<div className='links'>
					{studentRoutes.map((link) =>
						<Link key={link.id} to={link.url} className='link-item'>
							<span className='link-icon'>{link.icon}</span>
							{link.title}
						</Link>
					)}
				</div>
			</div>
		</div>
	)
}

export default Siderbar