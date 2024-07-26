import { Auth } from "@auth/core"
import type { OIDCConfig } from "@auth/core/providers"

export const { handlers, auth, signIn } = Auth({
  providers: [{
    id: "django",
    name: "Django Unchained",
    type: "oidc",
    clientId: process.env.OIDC_CLIENT_ID, // from the provider's dashboard
    clientSecret: process.env.OIDC_CLIENT_SECRET, // from the provider's dashboard
    wellKnown: "http://localhost:8000/oidc/.well-known/openid-configuration/",
    authorization: "http://localhost:8000/oidc/authorize",
    token: "http://localhost:8000/oidc/token",
    userinfo: "http://localhost:8000/oidc/userinfo",
    jwks_endpoint: "http://localhost:8000/oidc/jwks",
  } satisfies OIDCConfig],
  debug: true,
});
