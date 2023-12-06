import React, { useState,useEffect } from 'react';
import { Button, Form, Col, Row } from 'react-bootstrap';
import { Box } from '@mui/material';
import { addPrinter, fetchLocation } from '../../features/services/printer-management-services';

function AddPrinter() {

    const [detail, setDetail] = useState(
        {
            "pages_remaining": 200,
            "ink_status": true,
            "status": 1,
            "model_name": "HP - 254",
            "created_by": 1,
            "model" : 1,
            "floor": 1
        }
    );
    const [locations, setLocations] = useState([]);

    useEffect(() => {
        getLocations();
      }, [])

    const getLocations = async () => {
        let res = await fetchLocation();
        if (res && res.data) {
            setLocations(res.data);
        }
    }

    const handleChange = (e) => {
        let name = e.target.name;
        let value = e.target.value;

        if (name === "status" || name === "floor") {
            value = parseInt(value);
        }

        if (name === "ink_status") {
            value = e.target.checked;
        }

        setDetail((prev) => {
                return {...prev, [name] : value}
        })
    }

    const handleClick = async () => {
        console.log(detail)
        try {
            let res = await addPrinter(detail);
            console.log(res);
        } catch (err) {
            console.log(err);
        }
    }

  return (<>
    <h2>Thêm máy in</h2>
    <Box 
        ml = "20px"
        sx={{ height: "fit-content", width: '90%'}}>
    <Form>
        <Row className="mb-3">
            <Form.Group as={Col} >
            <Form.Label>Tên máy in</Form.Label>
            <Form.Control 
                type="text" 
                placeholder="Nhập tên sản phẩm" 
                name="model_name" 
                onChange={handleChange}/>
            </Form.Group>

            <Form.Group as={Col}>
            <Form.Label>Mã máy in</Form.Label>
            <Form.Control 
                type="text" 
                placeholder="Mã sản phẩm" 
                disabled />
            </Form.Group>
        </Row>

        <Row className="mb-3">
            <Form.Group as={Col} >
                <Form.Label>Trạng thái</Form.Label>
                <Form.Select 
                    defaultValue="Chọn trạng thái" 
                    name="status" 
                    onChange={handleChange}>
                        <option value={1}>Đang hoạt động</option>
                        <option value={2}>Bảo trì</option>
                        <option value={3}>Ngưng hoạt động</option>
                        <option value={4}>Gặp sự cố</option>
                        <option value={5}>Bận</option>
                </Form.Select>
            </Form.Group>
        
            <Form.Group as={Col} >
                <Form.Label>Vị trí</Form.Label>
                <Form.Select 
                    defaultValue="Chọn vị trí" 
                    name="floor" 
                    onChange={handleChange}>
                    <option disabled>Chọn vị trí</option>
                    {
                        locations.map((option, index) => (
                            <option key={index} value={index + 1}>
                                Cơ sở {option.building_code.inst} - Toà {option.building_code.building} - Tầng {option.floor_code}
                            </option>
                        ))
                    }
                </Form.Select>
            </Form.Group>
        </Row>

        <Row className="mb-3">
            <Form.Group as={Col} >
            <Form.Label>Số lượng giấy</Form.Label>
            <Form.Control 
                type="number"
                placeholder="Nhập số giấy" 
                name="page_remaining" 
                onChange={handleChange}/>
            </Form.Group>

        </Row>
        <Form.Group as={Col} >
            <Form.Check
                label="Tình trạng mực"
                type="checkbox"
                name='ink_status'
                onChange={handleChange}
            />
        </Form.Group>
        <Button variant="primary float-end" onClick={handleClick}>
            Lưu
        </Button>
    </Form>
    </Box>
  </>)
}

export default AddPrinter