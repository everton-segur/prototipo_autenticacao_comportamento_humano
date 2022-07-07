package com.baeldung.auth.config;

import com.baeldung.auth.dto.IaAuthorizationDTO;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.keycloak.authentication.AuthenticationFlowContext;
import org.keycloak.authentication.AuthenticationFlowError;
import org.keycloak.authentication.Authenticator;
import org.keycloak.models.KeycloakSession;
import org.keycloak.models.RealmModel;
import org.keycloak.models.UserModel;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

import javax.ws.rs.core.Response;
import java.util.Objects;

@AllArgsConstructor
@Slf4j
public class IAAuthenticator implements Authenticator {

    private static final String IP_BASED_OTP_CONDITIONAL_USER_ATTRIBUTE = "ip_based_otp_conditional";

    @Override
    public void authenticate(AuthenticationFlowContext context) {

        var path = context.getHttpRequest().getFormParameters().getFirst("ia_method_authorization");
        var data = context.getHttpRequest().getFormParameters().getFirst("data");
        var timestamp = context.getHttpRequest().getDecodedFormParameters().getFirst("timestamp");

        WebClient client = WebClient.builder().baseUrl("http://ia-authenticator:5000/" + path)
                .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_FORM_URLENCODED_VALUE)
                .build();

        WebClient.RequestHeadersSpec<?> body = client.post()
                .body(BodyInserters.fromFormData("data", data)
                        .with("timestamp", timestamp));

        var result = body.retrieve();
        IaAuthorizationDTO resultDto = null;
        try {
            resultDto = new ObjectMapper().readValue(result.bodyToMono(String.class).block(), IaAuthorizationDTO.class);
        } catch (JsonProcessingException e) {
            log.error("processing error:", e);
        }

        log.info(result.bodyToMono(String.class).toString());

        if (resultDto != null) {
            log.info(resultDto.toString());
        }

        if (Objects.requireNonNull(resultDto).isAuthorized()) {
            log.info("Deu sucesso");
            context.success();
        } else {
            log.error("Deu falha");
            context.failure(AuthenticationFlowError.INVALID_CREDENTIALS, Response.status(Response.Status.UNAUTHORIZED).build());
        }

    }

    @Override
    public void action(AuthenticationFlowContext context) {
    }

    @Override
    public boolean requiresUser() {
        return true;
    }

    @Override
    public boolean configuredFor(KeycloakSession session, RealmModel realm, UserModel user) {
        return true;
    }

    @Override
    public void setRequiredActions(KeycloakSession session, RealmModel realm, UserModel user) {
    }

    @Override
    public void close() {
    }

}
