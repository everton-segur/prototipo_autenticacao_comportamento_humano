import React from "react";
import {Button, Container, makeStyles, Typography} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    heading: {
        textAlign: "center",
        margin: theme.spacing(1, 0, 4),
    },
    submitButton: {
        marginTop: theme.spacing(4),
    },
}));

const Failed = () => {

    const {heading, submitButton} = useStyles();

    const onClick = () => {
        window.location.href = "/"
    };

    return (
        <Container maxWidth="xs">
            <Typography className={heading} variant="h3">
                Access Denied!
            </Typography>

            <Button
                type="submit"
                fullWidth
                variant="contained"
                color="secondary"
                className={submitButton}
                onClick={onClick}
            >
                Click to be redirected to login page
            </Button>
        </Container>
    );

}
export default Failed;