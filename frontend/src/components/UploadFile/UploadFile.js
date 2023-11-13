import { useState } from "react";
import shortid from 'shortid';
import './UploadFile.scss';
import { FaCloudUploadAlt, FaTimes } from 'react-icons/fa'

const UploadFile = () => {
    const [selectedfile, SetSelectedFile] = useState([]);
    const [Files, SetFiles] = useState([]);


    const filesizes = (bytes, decimals = 2) => {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const dm = decimals < 0 ? 0 : decimals;
        const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    const InputChange = (e) => {
        // --For Multiple File Input
        let images = [];
        console.log('e.target.files', e.target.files)
        for (let i = 0; i < e.target.files.length; i++) {
            images.push((e.target.files[i]));
            let reader = new FileReader();
            let file = e.target.files[i];
            reader.onloadend = () => {
                SetSelectedFile((preValue) => {
                    return [
                        ...preValue,
                        {
                            id: shortid.generate(),
                            filename: e.target.files[i].name,
                            filetype: e.target.files[i].type,
                            fileimage: reader.result,
                            datetime: e.target.files[i].lastModifiedDate.toLocaleString('en-IN'),
                            filesize: filesizes(e.target.files[i].size)
                        }
                    ]
                });
            }
            if (e.target.files[i]) {
                reader.readAsDataURL(file);
            }
        }
    }


    const DeleteSelectFile = (id) => {
        if (window.confirm("Are you sure you want to delete this Image?")) {
            const result = selectedfile.filter((data) => data.id !== id);
            SetSelectedFile(result);
        } else {
            // alert('No');
        }

    }

    return (

        <div className="fileupload-view">
            <div className="row justify-content-center m-0">
                <div className="col">
                    <div className="card mt-2">
                        <div className="card-body">
                            <div className="kb-data-box">
                                <div className="kb-modal-data-title">
                                    <div className="kb-data-title">
                                        <h6>Multiple File Upload With Preview</h6>
                                    </div>
                                </div>
                                <form>
                                    <div className="kb-file-upload">
                                        <div className="file-upload-box">
                                            <input type="file" id="fileupload" className="file-upload-input" onChange={InputChange} multiple />
                                            <p> </p>
                                            <span><FaCloudUploadAlt className="cloud-icon" /></span>
                                            <span>Drag and drop or <span className="file-link">Choose your files</span></span>
                                        </div>
                                    </div>
                                    <div className="kb-attach-box mb-3">
                                        {
                                            selectedfile.map((data, index) => {
                                                const { id, filename, filetype, fileimage, datetime, filesize } = data;
                                                return (
                                                    <div className="file-atc-box" key={id}>
                                                        {
                                                            filename.match(/.(jpg|jpeg|png|gif|svg)$/i) ?
                                                                <div className="file-image"> <img src={fileimage} alt="" /></div> :
                                                                <div className="file-image"><i className="far fa-file-alt"></i></div>
                                                        }
                                                        <div className="file-detail">
                                                            <h6>{filename}</h6>
                                                            <p></p>
                                                            <p><samp>({filesize})</samp></p>
                                                        </div>
                                                        <div className="file-actions">
                                                            <button type="button" className="file-action-btn" onClick={() => DeleteSelectFile(id)}><FaTimes /></button>
                                                        </div>
                                                    </div>
                                                )
                                            })
                                        }
                                    </div>
                                </form>
                                {/* s */}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    );
}

export default UploadFile