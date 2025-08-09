<script>
  import { goto } from '$app/navigation';
  import { auth, provider, appleProvider } from '$lib/firebase'; // Your Firebase setup
  import { signInWithPopup, signInWithEmailAndPassword, onAuthStateChanged } from 'firebase/auth';
  import { onMount } from 'svelte';
  

  let showPassword = false;
  let email = '';
  let password = '';  

  const handleStart = () => goto('/create-account/intro');

  onMount(() => {

    if (!auth) {
      console.error('Firebase auth is not initialized.');
      return;
    }
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      console.log('👀 Auth state changed:', user);
      if (user) {
        goto('/home');
      }
    });
    return () => {
      unsubscribe();
      console.log('🛑 Auth state change listener removed.');
    };
});


  // Google Auth Handler
  async function handleGoogleLogin() {
    try {
      const result = await signInWithPopup(auth, provider);
      const user = result.user;
      console.log('Google user:', user);
      // Example: navigate to dashboard or homepage
      goto('/home'); // Adjust the route as needed
    } catch (error) {
      console.error('Google Sign-In Error:', error);
    }
  }

  // Apple Auth Handler
  async function handleAppleLogin() { 
    try {
      if (!auth || !appleProvider) throw new Error('Auth or Apple provider unavailable');
      const result = await signInWithPopup(auth, appleProvider);
      const user = result.user;
      console.log('Apple user:', user);
      goto('/home');
    } catch (error) {
      console.error('Apple Sign-In Error:', error);
    }
    
  }

  // email/password login handler
  async function handleLogin() {
    try {
      if (!auth) throw new Error('Auth unavailable');
      if (!email || !password) {
        console.warn('Email and password are required.');
        return;
      }
      const { user } = await signInWithEmailAndPassword(auth, email, password);
      console.log('Email/password user:', user);
      goto('/home');
    } catch (err) {
      console.error('Login error:', err);
    }
  }
  
</script>
  
  <div class="login-container items-center">
    <!-- Logo -->
    <img src="/Logo Gold.png" alt="Logo" class="w-20 h-20 mb-4" />
  
    <!-- Username -->
    <div class="w-full">
      <label for="username" class="login-label">Email:</label>
      <input id="username" type="email" placeholder="Enter your email" class="login-input" bind:value={email}/>
    </div>
  
    <!-- Password -->
    <div class="w-full">
      <label for="password" class="login-label">Password:</label>
      <div class="relative">
        <input
          id="password"
          type={showPassword ? 'text' : 'password'}
          placeholder="Enter your password"
          class="login-input pr-10"
          bind:value={password}
        />
        <button
          class="login-icon-button"
          on:click={() => (showPassword = !showPassword)}
          aria-label="Toggle password visibility"
          type="button"
        >
          {#if showPassword}
            <!-- Eye off -->
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#141420" viewBox="0 0 24 24" class="w-5 h-5">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M13.875 18.825A10.05 10.05 0 0112 19c-4.418 0-8.268-2.943-9.542-7a10.05 10.05 0 011.49-2.678M9.88 9.88a3 3 0 014.24 4.24M3 3l18 18" />
            </svg>
          {:else}
            <!-- Eye on -->
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#141420" viewBox="0 0 24 24" class="w-5 h-5">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M2.458 12C3.732 7.943 7.522 5 12 5s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7s-8.268-2.943-9.542-7z" />
            </svg>
          {/if}
        </button>

        
       </div>
      <div class="text-xs mt-1 text-right underline cursor-pointer">Forgot Password?</div>
    </div>
  
    <!-- Login button -->
    <button class="login-btn" on:click={handleLogin} type="button">Log In</button>
  
    <!-- Divider -->
    <div class="flex items-center w-full text-sm text-[#c6b06e] space-x-4">
      <hr class="login-divider-line" />
      <span class="shrink-0">Or continue with</span>
      <hr class="login-divider-line" />
    </div>
  
    <!-- Google -->
    <button class="login-oauth" on:click={handleGoogleLogin} type="button">
      <img src="https://www.svgrepo.com/show/475656/google-color.svg" class="w-5 h-5" alt="Google" />
      Continue with Google
    </button>
    
  
    <!-- Apple -->
    <button class="login-oauth" on:click={handleAppleLogin} type="button">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 fill-black" viewBox="0 0 24 24">
        <path d="M16.7 13.7c-.1-1.3.5-2.3 1.6-3.1-.6-.9-1.5-1.3-2.6-1.3-1.2 0-2.2.7-2.7.7s-1.4-.6-2.3-.6c-1.7 0-3.3 1.4-3.3 4.2 0 1.3.3 2.8.9 4 .5 1 1.2 2.1 2.2 2.1.9 0 1.2-.6 2.2-.6 1 0 1.2.6 2.2.6 1 0 1.6-1 2.2-2 .5-.9.7-1.8.8-2.3zM13.7 6.5c.5-.6.8-1.3.7-2.1-.8.1-1.6.5-2.1 1.1-.5.5-.8 1.3-.7 2.1.8-.1 1.5-.5 2.1-1.1z"/>
      </svg>
      Continue with Apple
    </button>
  
    <!-- Sign Up -->
    <div class="login-footer">
      Don't have an account? <a href="/create-account" class="font-bold">Create One</a>
    </div>
  </div>
  