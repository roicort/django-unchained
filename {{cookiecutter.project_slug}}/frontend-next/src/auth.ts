import NextAuth from "next-auth";
import type { OIDCConfig } from "@auth/core/providers";
import axios from "axios";

// Get the OIDC configuration from the well-known endpoint

export const getOIDCConfig = async () => {
  try {
    const response = await axios.get(process.env.WELL_KNOWN_OIDC);
    return response.data;
  } catch (error) {
    console.error("Error fetching OIDC configuration:", error);
  }
};

const oidcConfig = await getOIDCConfig();

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    {
      id: "django",
      name: "Django Unchained",
      type: "oidc",
      issuer: oidcConfig.issuer, 
      clientId: process.env.OIDC_CLIENT_ID, // from the provider's dashboard
      clientSecret: process.env.OIDC_CLIENT_SECRET, // from the provider's dashboard
    } satisfies OIDCConfig,
  ],
  callbacks: {
    async jwt({ token, user, account, profile, isNewUser }) {
      if (user) {
        token.user = user;
      }
      if (profile) {
        token.profile = profile;
      }
      if (account) {
        token.account = account;
        try {
          const response = await axios.get(
            oidcConfig.userinfo_endpoint,
            {
              headers: {
                Authorization: `Bearer ${account.access_token}`,
              },
            },
          );
          token.profile.email = response.data.email;
          token.profile.given_name = response.data.given_name;
          token.profile.family_name = response.data.family_name;
        } catch (error) {
          console.error("Error fetching userinfo:", error);
        }
      }
      return token;
    },
    async session({ session, token }) {
      session.user = token.user;
      session.profile = token.profile;
      session.account = token.account;
      return session;
    },
  },
  debug: true,
});
