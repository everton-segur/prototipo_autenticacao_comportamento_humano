import { useState } from "react";

// useForm functional component
export const useForm = (callback: any, initialState = {}) => {
    const [values, setValues] = useState(initialState);

}