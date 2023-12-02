import axios from 'axios';
import { API_SERVER_URL } from '../../config';

export const fetchPrinters = () => {
    return axios.get(`${API_SERVER_URL}/api/printers/list`);
}

