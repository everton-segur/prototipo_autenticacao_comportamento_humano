package com.baeldung.auth.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class IaAuthorizationDTO {
    @JsonProperty("isAuthorized")
    private boolean isAuthorized;
}
