import React from 'react';

import {Button, Container, makeStyles, Typography} from "@material-ui/core";
import Failed from "./Failed";

const useStyles = makeStyles((theme) => ({
    heading: {
        textAlign: "center",
        margin: theme.spacing(1, 0, 4),
    },
    submitButton: {
        marginTop: theme.spacing(4),
    },
}));

const Success = () => {
    const {heading, submitButton} = useStyles();

    if (localStorage.getItem("Token") !== null) {
        return (
            <Container maxWidth="xs">
                <Typography className={heading} variant="h3">
                    You're logged id
                </Typography>

                <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    className={submitButton}
                    onClick={() => {
                        localStorage.removeItem("Token");
                        window.location.href = "/"
                    }}
                >
                    Click to logout
                </Button>
            </Container>
        )
    } else {
        return (<Failed/>)
    }

}

export default Success;