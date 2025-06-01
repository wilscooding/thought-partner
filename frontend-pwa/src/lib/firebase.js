// Import the functions you need from the SDKs you need
import { getApp, initializeApp, getApps } from "firebase/app";
import { browser } from "$app/environment";
import { getAuth, GoogleAuthProvider } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

// Firebase config from .env
const firebaseConfig = {
  apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
  authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
  appId: import.meta.env.VITE_FIREBASE_APP_ID,
  measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID
};




// Initialize Firebase
const app = getApps().length ? getApp() : initializeApp(firebaseConfig);
console.log("✅ Firebase app initialized:", app.name);

let auth = null;
let provider = null;
if (browser) {
  auth = getAuth(app);
  provider = new GoogleAuthProvider();
}

// const auth = getAuth(app);
// const provider = new GoogleAuthProvider();
const db = getFirestore(app);


export { app, auth, provider, db };