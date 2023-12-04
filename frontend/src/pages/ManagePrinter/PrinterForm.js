import PropTypes from "prop-types";
import { styled } from "@mui/material/styles";
import {
  Grid,
  Button,
  TextField,
  Box,
  FormControl,
  InputLabel,
  Input,
  FormHelperText,
  Select,
  MenuItem,
} from "@mui/material";


const StyledRoot = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
}));

const StyledFields = styled(Box)(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  justifyContent: "flex-start",
  padding: theme.spacing(1, 1, 2, 1),
}));

const StyledButtonContainer = styled(Box)(({ theme }) => ({
  maxWidth: 400,
  display: "flex",
  flexDirection: "row",
  gap: 20,
  padding: theme.spacing(1, 1, 2, 1),
}));

PrinterForm.propTypes = {
  values: PropTypes.object,
  onValues: PropTypes.func,
  onConfirmForm: PropTypes.func,
  onResetForm: PropTypes.func,
};

export default function PrinterForm({
  values,
  onValues,
  onConfirmForm,
  onResetForm,
}) {
  return (
    <StyledRoot>
      <StyledFields>
        <Grid container spacing={3}>
          <Grid item xs={6}>
            <Box
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "stretch",
                gap: "20px",
              }}
            >
              <FormControl fullWidth>
                <InputLabel id="add-name-label">Name</InputLabel>
                <Input 
                    id="my-input" 
                    aria-describedby="my-helper-text" 
                    value={values.name}
                    onChange={(e) => onValues("name", e.target.value)}
                /> 
              </FormControl>

              <FormControl fullWidth>
                <InputLabel id="add-status-select-label">Status</InputLabel>
                <Select
                  labelId="add-status-select-label"
                  label="Status"
                  value={values.status}
                  onChange={(e) => onValues("status", e.target.value)}
                >
                  <MenuItem value="Active">Active</MenuItem>
                  <MenuItem value="Offline">Offline</MenuItem>
                  <MenuItem value="Error">Error</MenuItem>
                  <MenuItem value="Busy">Busy</MenuItem>
                  <MenuItem value="Maintenance">Maintenance</MenuItem>
                </Select>
              </FormControl>

              <FormControl fullWidth>
                <InputLabel id="add-page-label">Page Remaining</InputLabel>
                <Input 
                    id="my-input" 
                    aria-describedby="my-helper-text" 
                    value={values.page_remaining}
                    onChange={(e) => onValues("page_remaining", e.target.value)}
                /> 
              </FormControl>

            </Box>
          </Grid>
          <Grid item xs={6}>
            <Box
              sx={{
                display: "flex",
                flexDirection: "column",
                alignItems: "stretch",
                gap: "20px",
              }}
            >
              <FormControl fullWidth>
                <InputLabel id="add-ins-select-label">Institution</InputLabel>
                <Select
                  labelId="add-ins-select-label"
                  label="Institution"
                  value={values.institution}
                  onChange={(e) => onValues("institution", e.target.value)}
                >
                  <MenuItem value="CS1">Cơ sở 1</MenuItem>
                  <MenuItem value="CS2">Cơ sở 2</MenuItem>
                </Select>
              </FormControl>

              <FormControl fullWidth>
                <InputLabel id="add-building-label">Building</InputLabel>
                <Input 
                    id="my-input" 
                    aria-describedby="my-helper-text" 
                    value={values.building}
                    onChange={(e) => onValues("building", e.target.value)}
                /> 
              </FormControl>

              <FormControl fullWidth>
                <InputLabel id="add-floor-label">Floor</InputLabel>
                <Input 
                    id="my-input" 
                    aria-describedby="my-helper-text" 
                    value={values.floor}
                    onChange={(e) => onValues("floor", e.target.value)}
                /> 
              </FormControl>

            </Box>
          </Grid>
        </Grid>
      </StyledFields>

      <StyledButtonContainer>
        <Button variant="contained" onClick={onConfirmForm}>
          Xác nhận
        </Button>
        <Button variant="outlined" color="error" onClick={onResetForm}>
          Đặt lại
        </Button>
      </StyledButtonContainer>

    </StyledRoot>
  );
}