<script>
    let showPassword = false;
    import { goto } from '$app/navigation';
    const handleStart = () => goto('/create-account/intro');
  </script>
  
  <div class="login-container items-center">
    <!-- Logo -->
    <img src="/logo.png" alt="Logo" class="w-12 h-12 mb-4" />
  
    <!-- Username -->
    <div class="w-full">
      <label class="login-label">Username:</label>
      <input type="email" placeholder="Enter your email" class="login-input" />
    </div>
  
    <!-- Password -->
    <div class="w-full">
      <label class="login-label">Password:</label>
      <div class="relative">
        <input
          type={showPassword ? 'text' : 'password'}
          placeholder="Enter your password"
          class="login-input pr-10"
        />
        <span class="login-icon-button" on:click={() => (showPassword = !showPassword)}>👁️</span>
      </div>
      <div class="text-xs mt-1 text-right underline cursor-pointer">Forgot Password?</div>
    </div>
  
    <!-- Login button -->
    <button class="login-btn">Log In</button>
  
    <!-- Divider -->
    <div class="flex items-center w-full text-sm text-[#c6b06e] space-x-4">
      <hr class="login-divider-line" />
      <span class="shrink-0">Or continue with</span>
      <hr class="login-divider-line" />
    </div>
  
    <!-- Google -->
    <button class="login-oauth">
      <img src="https://www.svgrepo.com/show/475656/google-color.svg" class="w-5 h-5" alt="Google" />
      Continue with Google
    </button>
  
    <!-- Apple -->
    <button class="login-oauth">
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
  