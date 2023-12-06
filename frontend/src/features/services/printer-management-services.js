import axios from 'axios';
import { API_SERVER_URL } from '../../config';

export const fetchPrinters = () => {
    return axios.get(`${API_SERVER_URL}/api/printers/list`);
}

export const updatePageRemains = (id) => {
    return axios.patch(`${API_SERVER_URL}/api/printers/${id}/update-page`);
}

export const addPrinter = (data) => {
    return axios.post(`${API_SERVER_URL}/api/printers/create/printer/`, data);
}

export const fetchLocation = () => {
    return axios.get(`${API_SERVER_URL}/api/printers/category`);
}

