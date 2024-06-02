# Turbo - Django & Next.js boilerplate

## Features <!-- omit from toc -->

- **Microsites**: supports several front ends connected to API backend
- **API typesafety**: exported types from backend stored in shared front end package
- **Server actions**: handling form submissions in server part of Next project
- **Tailwind CSS**: built-in support for all front end packages and sites
- **Auth system**: incorporated user authentication based on JWT tokens
- **Profile management**: update profile information from the front end
- **Registrations**: creation of new user accounts (activation not included)
- **Admin theme**: Unfold admin theme with user & group management
- **Visual Studio Code**: project configuration are already available with predefined tasks

### Front end dependencies

For the frontend project, it is bit more complicated to maintain fron end dependencies than in backend part. Dependencies, can be split into two parts. First part are general dependencies available for all projects under packages and apps folders. The second part are dependencies, which are project specific.

- **[next-auth](https://github.com/nextauthjs/next-auth)** - Next.js authentication
- **[react-hook-form](https://github.com/react-hook-form/react-hook-form)** - Handling of React forms
- **[tailwind-merge](https://github.com/dcastil/tailwind-merge)** - Tailwind CSS class names helper
- **[zod](https://github.com/colinhacks/zod)** - Schema validation

To install a global dependency for all packages and apps, use `-w` parameter. In case of development package, add `-D` argument to install it into development dependencies.

```bash
docker-compose exec web pnpm add react-hook-form -w
```

To install a dependency for specific app or package, use `--filter` to specify particular package.

```bash
docker-compose exec web pnpm --filter web add react-hook-form
```

## Front end project structure

Project structure on the front end, it is quite different from the directory hierarchy in the backend. Turbo counts with an option that front end have multiple front ends available on various domains or ports.

```text
frontend
| - apps       // available sites
|   - web      // available next.js project
| - packages   // shared packages between sites
|   - types    // exported types from backend - api
|   - ui       // general ui components
```

The general rule here is, if you want to have some shared code, create new package under packages/ folder. After adding new package and making it available for your website, it is needed to install the new package into website project by running a command below.

```bash
docker-compose exec web pnpm --filter web add @frontend/ui
```

## Auth

On the front end, next-auth is used to provide credentials authentication. The most important file on the front end related to authentication is `frontend/web/src/lib/auth.ts` which is containing whole business logic behind authentication.

### Authenticated paths on frontend

To ensure path is only for authenticated users, it is possible to use `getServerSession` to check the status of user.

This function accepts an argument with authentication options, which can be imported from `@/lib/auth` and contains credentials authentication business logic.

```tsx
import { getServerSession } from "next-auth";
import { redirect } from "next/navigation";
import { authOptions } from "@/lib/auth";

const SomePageForAuthenticatedUsers = async () => {
  const session = await getServerSession(authOptions);

  if (session === null) {
    return redirect("/");
  }

  return <>content</>;
};
```

To require authenticated user account on multiple pages, similar business logic can be applied in `layouts.tsx`.

```tsx
import { redirect } from "next/navigation";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";

const AuthenticatedLayout = async ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const session = await getServerSession(authOptions);

  if (session === null) {
    return redirect("/");
  }

  return <>{children}</>;
};

export default AuthenticatedLayout;
```

### Updating OpenAPI schema

After changes on the backend, for example adding new fields into serializers, it is required to update typescript schema on the frontend. The schema can be updated by running command below. In VS Code, there is prepared task which will update definition.

```bash
docker compose exec web pnpm openapi:generate
```

### Client side requests

At the moment, Turbo does not contain any examples of client side requests towards the backend. All the requests are handled by server actions. For client side requests, it is recommended to use [react-query](https://github.com/TanStack/query).
