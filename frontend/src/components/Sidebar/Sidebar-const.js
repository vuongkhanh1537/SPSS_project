import { GrDocument } from 'react-icons/gr'
import { FiPrinter, FiCreditCard } from 'react-icons/fi'
import { BsActivity } from 'react-icons/bs'
import { IoDocumentOutline } from 'react-icons/io5'
import { HiOutlineDocument } from 'react-icons/hi2'

export const studentRoutes = [
    {
        id: 1,
        title: 'Tài liệu',
        icon: <HiOutlineDocument />,
        url: '/'
    },
    {
        id: 2,
        title: 'Máy in',
        icon: <FiPrinter />,
        url: '/printers'
    },
    {
        id: 3,
        title: 'Tình trạng in',
        icon: <FiPrinter />,
        url: '/print-status'
    },
    {
        id: 4,
        title: 'Thanh toán',
        icon: <FiCreditCard />,
        url: '/payment'
    },
    {
        id: 5,
        title: 'Lịch sử hoạt động',
        icon: <BsActivity />,
        url: '/history'
    },
]