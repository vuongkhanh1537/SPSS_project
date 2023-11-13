import React from 'react'
import { FiArrowLeft, FiArrowRight } from 'react-icons/fi'
import './PrevNextAction.scss'
import { Link } from 'react-router-dom'

function PrevNextAction({prevText, prevLink, nextText, nextLink }) {
  return (
    <div className='prev-next-action'>
        <div>
            {
                prevLink && prevText &&
                <Link to={prevLink} className='action'>
                    <FiArrowLeft />
                    <span> { prevText } </span>
                </Link>
            }
        </div>
        <div>
            {
                nextLink && nextText &&
                <Link to={nextLink} className='action'>
                    <span> { nextText } </span>
                    <FiArrowRight />
                </Link>
            }
        </div>
    </div>
  )
}

export default PrevNextAction