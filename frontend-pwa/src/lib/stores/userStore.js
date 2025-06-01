// src/lib/stores/userStore.js
import { writable } from 'svelte/store';
import { browser } from '$app/environment';
import { auth } from '$lib/firebase';
import { onAuthStateChanged } from 'firebase/auth';

export const currentUser = writable(null);

if (browser && auth) {
  // Listen for authentication state changes
  onAuthStateChanged(auth, (user) => {
    currentUser.set(user);
  });
}

// onAuthStateChanged(auth, (user) => {
//   currentUser.set(user);
// });