// src/lib/stores/userStore.js
import { writable } from 'svelte/store';
import { browser } from '$app/environment';
import { auth } from '$lib/firebase';
import { onAuthStateChanged } from 'firebase/auth';
import type { User } from 'firebase/auth';

export const currentUser = writable<User | null>(null);
export const userLoaded = writable(false);

export function resetUser() {
  currentUser.set(null);
  userLoaded.set(true);
}

if (browser) {
  // Initialize the current user state
  onAuthStateChanged(auth, (user) => {
    currentUser.set(user);
    userLoaded.set(true); // Set userLoaded to true once the user state is determined
  });
}


// if (browser) {
//   onAuthStateChanged(auth, (user) => {
//     console.log("User state changed:", user);
//     currentUser.set(user);

//   });
// }

// if (browser && auth) {
//   // Listen for authentication state changes
//   onAuthStateChanged(auth, (user) => {
//     currentUser.set(user);
//   });
// }

// onAuthStateChanged(auth, (user) => {
//   currentUser.set(user);
// });