import React, { useState } from 'react'
import UploadFile from '../../components/UploadFile/UploadFile'
import './PrintDocument.scss'
import { FiArrowRight } from 'react-icons/fi'
import { Link } from 'react-router-dom';
import PrevNextAction from '../../components/PrevNextAction/PrevNextAction';
import { useDispatch, useSelector } from 'react-redux';
import { savePrintingProperties } from '../../features/actions/printing-actions';

function PrintDocument() {
  const { copies, sideOption, pageOption, page, selectedfile } = useSelector((state) => state.printing);
  const dispatch = useDispatch();

  const handleChange = (e) => {
    dispatch(savePrintingProperties(e.target.name, e.target.value))
  }

  const setSelectedFile = (value) => {
    console.log('file', value)
    dispatch(savePrintingProperties('selectedfile', value))
  }

  return (
    <div className='print-document'>
      <UploadFile selectedfile={selectedfile} setSelectedFile={setSelectedFile} />
      <div className='print-setting'>
        <h6>Cài đặt in</h6>
        <div className='print-properties'>
          <div>
            <div class="mb-3 row">
              <label for="inputNumOfPage" class="col-sm-2 col-form-label">Bản copies:</label>
              <div class="col-sm-10">
                <input type="number" class="form-control" style={{width: '90px'}} id="inputNumOfPage" name='copies' value={copies} onChange={handleChange} />
              </div>
            </div>
          </div>
          <div>
            <p>Xử lý in</p>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="sideOption" id="printOneSide" value="one-side" onChange={handleChange} checked={sideOption === 'one-side'} />
              <label class="form-check-label" for="printOneSide">
                In một mặt
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="sideOption" id="printTwoSide" value="two-side" onChange={handleChange} checked={sideOption === 'two-side'} />
              <label class="form-check-label" for="printTwoSide">
                In hai mặt
              </label>
            </div>
          </div>
          <div>
            <p>Phạm vi in</p>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="pageOption" id="printAll" value="all" onChange={handleChange} checked={pageOption === 'all'} />
              <label class="form-check-label" for="printAll">
                Toàn bộ trang
              </label>
            </div>
            <div class="form-check d-flex align-items-center gap-2">
              <input class="form-check-input" type="radio" name="pageOption" id="printSomePages" value="page" onChange={handleChange} checked={pageOption === 'page'} />
              <label class="form-check-label" for="printSomePages">
                Trang
              </label>
              <input type='text' placeholder='1,3,5-8' className='form-control' name="page" style={{width: '150px'}} value={page} onChange={handleChange} disabled={pageOption !== 'page'} />
            </div>
          </div>
        </div>
      </div>
      <PrevNextAction nextLink='/printers' nextText='Chọn máy in' />
    </div>
  )
}

export default PrintDocument