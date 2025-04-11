import React from "react";
import ReactDOM from "react-dom/client";

import * as Sentry from "@sentry/react";

import App from "./App";
import { AuthProvider } from "./context/AuthContext";

Sentry.init({
  dsn: "https://6c8d6c75dfeae8fd34d7697c20b5bea6@o4508100133978112.ingest.de.sentry.io/4509136158589008",
  integrations: [
    Sentry.browserTracingIntegration(),
    Sentry.replayIntegration(),
  ],
  tracesSampleRate: 1.0,
  tracePropagationTargets: ["localhost", /^https:\/\/spbetu\.ru\/api/],
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
});

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>,
);
