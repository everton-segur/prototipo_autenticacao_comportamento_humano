import React from 'react';

import {Button, Container, makeStyles, TextField, Typography,} from "@material-ui/core";
import {useForm} from "react-hook-form";
import auth from "./service";

interface IFormInput {
    method: string;
    username: string;
    password: string;
    data: string;
    time: string;
}

const useStyles = makeStyles((theme) => ({
    heading: {
        textAlign: "center",
        margin: theme.spacing(1, 0, 4),
    },
    submitButton: {
        marginTop: theme.spacing(4),
    },
}));

const Login = () => {
    const {heading, submitButton} = useStyles();
    const {
        register,
        handleSubmit,
    } = useForm<IFormInput>();


    const onSubmit = async (formInput: IFormInput) => {
        const data = await auth(formInput.username,
            formInput.password,
            formInput.data,
            formInput.time,
            formInput.method,
        )

        if (data?.access_token !== undefined && data?.access_token !== null) {
            console.log("passou")
            localStorage.setItem("Token", data.access_token)
            window.location.href = "/success"
        } else {
            console.log("nao passou")
            window.location.href = "/failure"
        }
    };

    // @ts-ignore
    return (
        <Container maxWidth="xs">
            <Typography className={heading} variant="h3">
                Sign In Form
            </Typography>
            <form onSubmit={handleSubmit(onSubmit)} noValidate>
                <TextField
                    {...register("method")}
                    variant="outlined"
                    margin="normal"
                    label="Method"
                    helperText={"Tipos de metodos: decision-tree, gradient, naive-bayes, random-forests"}
                    fullWidth
                    required
                />
                <TextField
                    {...register("username")}
                    variant="outlined"
                    margin="normal"
                    label="Username"
                    fullWidth
                    required
                />
                <TextField
                    {...register("password")}
                    variant="outlined"
                    margin="normal"
                    label="Password"
                    type="password"
                    fullWidth
                    required
                />
                <TextField
                    {...register("data")}
                    variant="outlined"
                    margin="normal"
                    label="ImmutableData"
                    fullWidth
                    required
                />
                <TextField
                    {...register("time")}
                    variant="outlined"
                    margin="normal"
                    label="Login Time"
                    fullWidth
                    required
                />
                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    className={submitButton}
                >
                    Sign Up
                </Button>

            </form>
        </Container>
    );
}

export default Login;