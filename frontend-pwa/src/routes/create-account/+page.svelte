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
    <div class="register-header flex items-center justify-between w-full">
        <h1 class="register-title">Create Account</h1>
        <img src="/Logo Gold.png" alt="Logo" class="register-logo" />
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
    
      <!-- Agree to Terms -->
    <div class="toggle-row">
      <div class="toggle-switch" class:active={agreedToTerms} on:click={() => agreedToTerms = !agreedToTerms}></div>
      <span class="register-toggle-label">
        I agree to the <a href="/terms" class="underline">terms and conditions</a>
      </span>
    </div>

    <!-- Confirm Age -->
    <div class="toggle-row">
      <div class="toggle-switch" class:active={isAdult} on:click={() => isAdult = !isAdult}></div>
      <span class="register-toggle-label">
        I confirm that I am 18 years of age or older.
      </span>
    </div>
    
 
 
     <!-- Submit button -->
    <div class="w-full flex justify-center mt-4">
        <button class="register-submit" on:click={handleSubmit}>Submit</button>
    </div>
  </div>
  