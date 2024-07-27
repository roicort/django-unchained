import NextAuth from "next-auth";
import type { OIDCConfig } from "@auth/core/providers"

export const { handlers, auth, signIn } = NextAuth({
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
    issuer: "http://localhost:8000/oidc",
  } satisfies OIDCConfig],
  callbacks: {
    jwt({ token, user, account, profile }) {
      if (user) { // User is available during sign-in
        token.id = user.id
      }
      return token
    },
    session({ session, token }) {
      session.user.id = token.id
      return session
    },
  },
  debug: true,
});