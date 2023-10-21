import { getUserFromLocalStorage } from "../../utils/localStorage"

const initialState = {
    user: getUserFromLocalStorage(),
    loading: false
}

const authReducer = (state = initialState, action) => {
    switch(action.type) {
        case 'LOGIN_SUCCESS': { 
            return { ...state, user: 'abc' }
        }
        default: 
            return state;
    }
}

export default authReducer