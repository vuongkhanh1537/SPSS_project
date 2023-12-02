import React, { useEffect, useState } from 'react';
import { Box, Button, Stack } from '@mui/material';
import {DataGrid} from '@mui/x-data-grid'; 
import { fetchPrinters } from '../../features/services/printer-management-services';
function PrinterMangement() {
  const status = ["Đang hoạt động", "Bảo trì", , "Ngưng hoạt động", "Gặp sự cố", "Bận"];
  const columns = [
    { field: 'id', headerName: 'ID', width: 90, },
    {
      field: 'model_name',
      headerName: 'Model',
      width: 100,
      flex: 1,
      headerAlign: "center",
      align: "center"
    },
    { 
      field: 'pages_remaining',
      headerName: 'Lượng giấy còn lại',
      width: 100,
      flex: 1,
      headerAlign: "center",
      align: "center"
    },
    {
      field: 'floor_description',
      headerName: 'Vị trí',
      width: 100,
      flex: 1,
      headerAlign: "center",
      align: "center"
    },{
      field: 'status',
      headerName: 'Tình trạng',
      width: 100,
      flex: 1,
      headerAlign: "center",
      align: "center",
      valueGetter: (params) => {
        return status[params.row.status - 1];
      }
  },
  ];
  const [rows, setRows] = useState([]);


  useEffect(() => {
    getPrinters();
  }, [])

  const getPrinters = async () => {
    let res = await fetchPrinters();
    console.log(res.data);
    if (res && res.data) {
      setRows(res.data);
    }
  }
  const [selectionModel, setSelectionModel] = useState([]); 

  const handleAddClick= () => {

  }  

  const handleDeleteClick = () => {

  }

  const handleStatusToggleClick = () => {

  }

  const handleRowClick = () => {

  }

  return (<>
    <h2>Quản lý máy in</h2>
    <div className='printer-management'>
    <Box
      m = "20px 20px"
      sx={{ height: "fit-content", width: '90%'}}>   
      <Box
        m = "0 20px 20px 0"
      >
        <Stack direction="row" spacing={2}>
          <Button 
            variant='outlined'
            onClick={handleAddClick}
          >Thêm máy in</Button>
          <Button 
            variant="outlined" 
            color="error"
            disabled = {selectionModel.length === 0}  
            onClick={handleDeleteClick}
          >Xoá máy in</Button>
          <Button 
            variant="outlined" 
            color="warning"
            disabled={selectionModel.length === 0}
            onClick={handleStatusToggleClick}
          >Bật / Tắt</Button>
        </Stack>
      </Box>
      <DataGrid 
        getRowId={(row) => row.id}
        rows={rows}
        columns={columns}
        onRowClick={handleRowClick}
        initialState={{
        pagination: {
            paginationModel: {
            pageSize: 10,
            },
        },
        }} 
        pageSizeOptions={[10]}
        checkboxSelection
        disableRowSelectionOnClick
        onRowSelectionModelChange={(newSelection) => {
            setSelectionModel(newSelection);
        }}
        selectionModel={selectionModel}
        sx={{
            boxShadow: 2,
            borderRadius: 3,
            '& .MuiDataGrid-cell:hover': {
              color: 'primary.main',
            },
        }}
      />
    </Box>
    </div>
  </>);
}

export default PrinterMangement