import { useState } from 'react';
// import { useNavigate } from 'react-router-dom';
import { faker } from '@faker-js/faker';
import { DataGrid } from '@mui/x-data-grid';

import {
  Card,
  Button,
  Container,
  Stack,
  Typography,
  TableContainer,
  Table,
  TableBody,
  TableRow,
  TableCell,
  Checkbox,
  IconButton,
  useTheme,
  TablePagination,
  MenuItem,
  Popover,
  Chip,
} from '@mui/material';

import Iconify from '../../components/iconify/Iconify.js';
import Notification from '../../components/Notification/Notification.js';
import Popup from '../../components/PopUp/Popup.js';
import PrinterForm from './PrinterForm.js';
import { PiGenderIntersexDuotone } from 'react-icons/pi';
import ListHead from '../../components/ListHead/ListHead.js';
import { getComparator, stableSort } from '../../utils/sortEngine.js';


const initAddValue = {
  name: '',
  institution: '',
  building: '',
  floor: '',
  status: '',
  page_remaining: ''
};

// const columns = [
//   { field: 'id', headerName: 'ID', width: 70 },
//   { field: 'name', headerName: 'Name', width: 130 },
//   { field: 'address', headerName: 'Address', width: 130 },
//   { field: 'status', headerName: 'Status', width: 130 },
//   { field: 'page_remaining', headerName: 'Page Remain', width: 130 },
// ];


const TABLE_HEAD = [
  { id: 'id', label: 'ID', align: 'left' },
  { id: 'name', label: 'Name', align: 'left' },
  { id: 'institution', label: 'Institution', align: 'left' },
  { id: 'building', label: 'Building', align: 'left' },
  { id: 'floor', label: 'Floor', align: 'left' },
  { id: 'status', label: 'Status', align: 'left' },
  { id: 'page_remaining', label: 'Page Remaining', align: 'center' },
  { id: 'menu' }
];


const PRINTERS= [
    {
        id: '1',
        name: 'HP LaserJet',
        institution: 'CS2',
        building: 'H1',
        floor: '404',
        status: 'Active',
        page_remaining: 20
    },
    {     
        id: '2',
        name: 'HP LaserJet',
        institution: 'CS2',
        building: 'H2',
        floor: '505',
        status: 'Busy',
        page_remaining: 10
    },
    {
        id: '3',
        name: 'HP LaserJet',
        institution: 'CS2',
        building: 'H6',
        floor: '104',
        status: 'Active',
        page_remaining: 5
    },
    {
        id: '4',
        name: 'HP LaserJet',
        institution: 'CS2',
        building: 'H1',
        floor: '404',
        status: 'Active',
        page_remaining: 14
    },
    {
        id: '5',
        name: 'HP LaserJet',
        institution: 'CS2',
        building: 'H1',
        floor: '202',
        status: 'Active',
        page_remaining: 7
    },
    {
        id: '6',
        name: 'HP LaserJet',
        institution: 'CS2',
        building: 'H3',
        floor: '404',
        status: 'Active',
        page_remaining: 18
    },
];

export default function ManagePrinter(){

  const [PrinterList, setPrinterList] = useState(PRINTERS);
  const [openPopup, setOpenPopup] = useState(false);
  const [selectedPrinter, setSelectedPrinter] = useState({});

  //-----------------------------------------------------------
  const [openNoti, setOpenNoti] = useState(false);

  const [actStatus, setActStatus] = useState(false);

  const handleCloseNoti = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpenNoti(false);
  };

  //-------------------------ADD FORM----------------------------------
  const [addValues, setAddValues] = useState(initAddValue);

  const handleChangeAddValues = (name, newValue) => {
    setAddValues({ ...addValues, [name]: newValue });
  };

  const onResetAddForm = () => {
    setAddValues(initAddValue);
  };

  const onConfirmAddForm = () => {
    if (
      addValues.name !== '' &&
      addValues.institution !== '' &&
      addValues.building !== '' &&
      addValues.floor !== '' &&
      addValues.status !== '' &&
      addValues.page_remaining !== ''
    ) {
      let newPrinter = {
        id: faker.datatype.uuid(),
        name: addValues.name,
        institution: addValues.institution,
        floor: addValues.floor,
        building: addValues.building,
        status: addValues.status,
        page_remaining: addValues.page_remaining
      };
      setPrinterList([newPrinter, ...PrinterList]);
      setAddValues(initAddValue);
      setActStatus(true);
    } else {
      setActStatus(false);
    }
    setOpenPopup(false);
    setOpenNoti(true);
  };
  // ---------------------------------EDIT------------------------------
  const [editValues, setEditValues] = useState(initAddValue);
  const [openEditPopup, setOpenEditPopup] = useState(false);

  const handleOpenEditPopup = () => {

    setEditValues({
      ...editValues,
      id: selectedPrinter.id,
      name: selectedPrinter.name,
      institution: selectedPrinter.institution,
      building: selectedPrinter.building,
      floor: selectedPrinter.floor,
      status: selectedPrinter.status,
      page_remaining: selectedPrinter.page_remaining
    });

    setOpenEditPopup(true);
    handleCloseMenu();
  };
  
  const handleChangeEditValues = (name, newValue) => {
    setEditValues({ ...editValues, [name]: newValue });
  };

  const onResetEditForm = () => {
    setEditValues(initAddValue);
  };

  const onConfirmEditForm = () => {
    if (
      editValues.id !== null &&
      editValues.name !== '' &&
      editValues.institution !== '' &&
      editValues.building !== '' &&
      editValues.floor !== '' &&
      editValues.status !== '' &&
      editValues.page_remaining !== null
    ) {
      let idx = PrinterList.findIndex((Printer) => {
        return Printer.id === selectedPrinter.id;
      });

      let editedList = PrinterList;
      editedList[idx].id = editValues.id;
      editedList[idx].name = editValues.name;
      editedList[idx].institution = editValues.institution;
      editedList[idx].building = editValues.building;
      editedList[idx].floor = editValues.floor;
      editedList[idx].status = editValues.status;
      editedList[idx].page_remaining = editValues.page_remaining;

      setPrinterList(editedList);
      setActStatus(true);
    } else {
      setActStatus(false);
    }
    setOpenEditPopup(false);
    setOpenNoti(true);
  };

  //--------------------------VIEW-----------------------
  const handleOpenViewPopup = () => {};

  //---------------------------------------------------
  const [openConfirm, setOpenConfirm] = useState(false);

  const handleOpenConfirm = () => {
    handleCloseMenu();
    setOpenConfirm(true);
  };

  const onConfirmDelete = (id) => {
    let idx = PrinterList.findIndex((Printer) => {
      return Printer.id === id;
    });

    let deletedPrinterList = PrinterList;
    deletedPrinterList.splice(idx, 1);
    setPrinterList(deletedPrinterList);
    setOpenConfirm(false);
    setActStatus(true);
    setOpenNoti(true);
  };

  //---------------------------------------------------
  const [open, setOpen] = useState(null);

  const handleOpenMenu = (event) => {
    setOpen(event.currentTarget);
  };

  const handleCloseMenu = () => {
    setOpen(null);
  };

  //----------------------------------------
  const [page, setPage] = useState(0);

  const [rowsPerPage, setRowsPerPage] = useState(10);

  const emptyRows =
    page > 0 ? Math.max(0, (1 + page) * rowsPerPage - PRINTERS.length) : 0;

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setPage(0);
    setRowsPerPage(parseInt(event.target.value, 10));
  };

  //------------------------------------------
  const [selected, setSelected] = useState([]);

  const handleSelectAllClick = (event) => {
    if (event.target.checked) {
      const newSelecteds = PrinterList.map((Printer) => Printer.id);
      setSelected(newSelecteds);
      return;
    }
    setSelected([]);
  };

  const handleClick = (event, id) => {
    const selectedIndex = selected.indexOf(id);
    let newSelected = [];
    if (selectedIndex === -1) {
      newSelected = newSelected.concat(selected, id);
    } else if (selectedIndex === 0) {
      newSelected = newSelected.concat(selected.slice(1));
    } else if (selectedIndex === selected.length - 1) {
      newSelected = newSelected.concat(selected.slice(0, -1));
    } else if (selectedIndex > 0) {
      newSelected = newSelected.concat(
        selected.slice(0, selectedIndex),
        selected.slice(selectedIndex + 1)
      );
    }
    setSelected(newSelected);
  };

  //--------------------------------
  const [order, setOrder] = useState('asc');

  const [orderBy, setOrderBy] = useState('name');

  const handleRequestSort = (event, property) => {
    const isAsc = orderBy === property && order === 'asc';
    setOrder(isAsc ? 'desc' : 'asc');
    setOrderBy(property);
  };

  //-------------------------------
  return (
    <>
      <Container>
        <Stack
          direction="row"
          alignItems="center"
          justifyContent="space-between"
          mb={4}>
          <Typography variant="h4" gutterBottom>
            Danh sách máy in
          </Typography>
          <Button
            variant="contained"
            startIcon={<Iconify icon="eva:plus-fill" />}
            onClick={() => setOpenPopup(true)}>
              Thêm máy in 
          </Button>
        </Stack>

        <Card>
        <TableContainer sx={{ minWidth: 900 }} style={{ padding: '30px' }}>
              <Table>
                <ListHead
                  order={order}
                  orderBy={orderBy}
                  onRequestSort={handleRequestSort}
                  headLabel={TABLE_HEAD}
                  rowCount={PrinterList.length}
                  numSelected={selected.length}
                  onSelectAllClick={handleSelectAllClick}
                />
                <TableBody>
                  {stableSort(PrinterList, getComparator(order, orderBy))
                    .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                    .map((Printer, idx) => {
                      const {
                        id,
                        name,
                        institution,
                        building,
                        floor,
                        status,
                        page_remaining
                      } = Printer;

                      const selectedPrinter = selected.indexOf(id) !== -1;

                      return (
                        <TableRow
                          hover
                          key={id}
                          tabIndex={-1}
                          // role="checkbox"
                          selected={selectedPrinter}>
                          {/* <TableCell padding="checkbox">
                            <Checkbox
                              checked={selectedPrinter}
                              onChange={(event) => handleClick(event, id)}
                            />
                          </TableCell> */}
                          <TableCell align="left">{id}</TableCell>

                          <TableCell align="left">{name}</TableCell>

                          <TableCell align="left">{institution}</TableCell>

                          <TableCell align="left">{building}</TableCell>

                          <TableCell align="left">{floor}</TableCell>
                          
                          <TableCell align="left">{status}
                            {/* <Chip label={status} color={statusColor(status)} /> */}
                          </TableCell>

                          <TableCell align="center">{page_remaining}</TableCell>

                          <TableCell align="right">
                            <IconButton
                              size="large"
                              color="inherit"
                              onClick={(event) => {
                                handleOpenMenu(event);
                                setSelectedPrinter(Printer);
                              }}>
                              <Iconify icon={'eva:more-vertical-fill'} />
                            </IconButton>
                          </TableCell>
                        </TableRow>
                      );
                    })}
                  {emptyRows > 0 && (
                    <TableRow style={{ height: 53 * emptyRows }}>
                      <TableCell colSpan={6} />
                    </TableRow>
                  )}
                </TableBody>
              </Table>
            </TableContainer>
            <TablePagination
              rowsPerPageOptions={[5, 10, 25]}
              component="div"
              count={PRINTERS.length}
              rowsPerPage={rowsPerPage}
              page={page}
              onPageChange={handleChangePage}
              onRowsPerPageChange={handleChangeRowsPerPage}
          />
        </Card>
      </Container>

      <Popover
        open={Boolean(open)}
        anchorEl={open}
        onClose={handleCloseMenu}
        anchorOrigin={{ vertical: 'top', horizontal: 'left' }}
        transformOrigin={{ vertical: 'top', horizontal: 'right' }}
        PaperProps={{
          sx: {
            p: 1,
            width: 140,
            '& .MuiMenuItem-root': {
              px: 1,
              typography: 'body2',
              borderRadius: 0.75,
            },
          },
        }}>

        <MenuItem onClick={handleOpenViewPopup}>
          <Iconify icon={'eva:edit-fill'} sx={{ mr: 2 }} />
            Xem chi tiết
        </MenuItem>

        <MenuItem onClick={handleOpenEditPopup}>
          <Iconify icon={'eva:edit-fill'} sx={{ mr: 2 }} />
            Chỉnh sửa
        </MenuItem>

        {/* <MenuItem sx={{ color: 'error.main' }} onClick={handleOpenConfirm}>
          <Iconify icon={'eva:trash-2-outline'} sx={{ mr: 3 }} />
            Xóa ca
        </MenuItem> */}

      </Popover>
      <Popup
        title="Thêm máy in"
        openPopup={openPopup}
        setOpenPopup={setOpenPopup}>
        <PrinterForm
          values={addValues}
          onValues={handleChangeAddValues}
          onConfirmForm={onConfirmAddForm}
          onResetForm={onResetAddForm}
      />
      </Popup>

      <Popup
        title="Chỉnh sửa máy in"
        openPopup={openEditPopup}
        setOpenPopup={setOpenEditPopup}>
        <PrinterForm
          values={editValues}
          onValues={handleChangeEditValues}
          onConfirmForm={onConfirmEditForm}
          onResetForm={onResetEditForm}
        />
      </Popup>

      {/* <Popup
        title="Xem chi tiết"
        openPopup={openViewPopup}
        setOpenPopup={setOpenViewPopup}>
        <ViewPrinterForm
          values={viewValues}
        />
      </Popup> */}

      <Notification
        open={openNoti}
        handleClose={handleCloseNoti}
        status={actStatus}
      />
    </>
  );
}
