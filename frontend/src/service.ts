import axios, {AxiosRequestConfig} from "axios";
import qs from "qs";

const auth = async (user: string, passwd: string, data: string, time: string, method: string) => {

    const body =
        {
            "client_id": 'account',
            "client_secret": '**********',
            "grant_type": 'password',
            "username": user,
            "password": passwd,
            "ia_method_authorization": method,
            "data": data,
            "timestamp": time
        }

    const config = {
        baseURL: "http://localhost:8083",
        url: "/auth/realms/baeldung/protocol/openid-connect/token",
        method: 'POST',
        data: qs.stringify(body)
    }

    try {
        const response = (await axios(config as AxiosRequestConfig))
        if (response.data !== undefined) {
            return response.data
        }
    } catch (e) {
        console.log("Error:", e)
    }
    return {}

}

export default auth;