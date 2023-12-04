import React from 'react'
function PrintingHistory() {
  return (
    <div>
      <h2>Lịch sử in</h2>
      <br></br>
      <br></br>
      <br></br>
      <table className="table table-striped">
        <tbody>
          <tr>
            <th>STT</th>
            <th>Tên tài liệu</th>
            <th>Số lượng trang</th>
            <th>Thời gian in</th>
            <th>Ghi chú</th>
          </tr>
          <tr>
            <td>1</td>
            <td>Giải tích</td>
            <td>10</td>
            <td>01/11/2023</td>
            <td></td>
          </tr>
          <tr>
            <td>2</td>
            <td>Bài tập Hóa</td>
            <td>12</td>
            <td>05/11/2023</td>
            <td></td>
          </tr>
          <tr>
            <td>3</td>
            <td>Công nghệ phần mềm</td>
            <td>50</td>
            <td>15/11/2023</td>
            <td></td>
          </tr>
          <tr>
            <td>4</td>
            <td>Bài tập về nhà</td>
            <td>13</td>
            <td>17/11/2023</td>
            <td></td>
          </tr>
          <tr>
            <td>5</td>
            <td>Bài tập</td>
            <td>17</td>
            <td>26/11/2023</td>
            <td></td>
          </tr>
        </tbody>
      </table>
    </div>
  )
}

export default PrintingHistory