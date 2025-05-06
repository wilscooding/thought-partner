<script>
    import { goto } from '$app/navigation';
    let agreedToTerms = false;
    let isAdult = false;
  
    function handleSubmit() {
      // Optionally, validate agreedToTerms / isAdult here
      goto('/create-account/intro'); // Navigate to intro
    }
</script>
  
  <div class="register-container">
    <!-- Title and logo -->
    <div class="w-full flex flex-col items-center space-y-4">
      <h1 class="register-title text-left w-full">Create Account</h1>
      <img src="/logo.png" alt="Logo" class="w-14 h-14 self-end" />
    </div>
  
    <!-- Email -->
    <div class="w-full">
      <label class="register-label">Email</label>
      <input type="email" placeholder="Enter your email" class="register-input" />
    </div>
  
    <!-- Password -->
    <div class="w-full">
      <label class="register-label">Password</label>
      <input type="password" placeholder="Enter password" class="register-input" />
    </div>
  
    <!-- Confirm Password -->
    <div class="w-full">
      <label class="register-label">Confirm Password</label>
      <input type="password" placeholder="Re-enter password" class="register-input" />
    </div>
  
    <!-- Agree to terms -->
    <div class="register-toggle">
      <label class="relative inline-flex items-center cursor-pointer">
        <input type="checkbox" class="sr-only peer" bind:checked={agreedToTerms} />
        <div class="register-toggle-circle"></div>
      </label>
      <span class="register-toggle-label">
        I agree to the <a href="/terms" class="underline">terms and conditions</a>
      </span>
    </div>
  
    <!-- Confirm age -->
    <div class="register-toggle">
      <label class="relative inline-flex items-center cursor-pointer">
        <input type="checkbox" class="sr-only peer" bind:checked={isAdult} />
        <div class="register-toggle-circle"></div>
      </label>
      <span class="register-toggle-label">
        I confirm that I am 18 years of age or older.
      </span>
    </div>
  
     <!-- Submit button -->
    <div class="w-full flex justify-center mt-4">
        <button class="register-submit" on:click={handleSubmit}>Submit</button>
    </div>
  </div>
  