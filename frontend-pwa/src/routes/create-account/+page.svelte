<script>
    import { goto } from '$app/navigation';
    import { getAuth, createUserWithEmailAndPassword } from 'firebase/auth';
    let agreedToTerms = false;
    let isAdult = false;
    let email = '';
    let password = '';
    let confirmPassword = '';

    const auth = getAuth();

    async function handleSubmit() {
    if (!agreedToTerms || !isAdult) {
      alert('You must agree to the terms and confirm you are 18 or older.');
      return;
    }

    try {
      const userCredential = await createUserWithEmailAndPassword(auth, email, password);
      console.log('User created:', userCredential.user);
      goto('/create-account/intro');
    } catch (error) {
      console.error('Error creating user:', error);
      alert('Failed to create account. Please try again.');
    }
  }

    const handleBack = () => {
      if (history.length > 1) {
        history.back();
      } else {
        goto('/login');
      }
    };
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
      <input type="email" bind:value={email} placeholder="Enter your email" class="register-input" />
    </div>
  
    <!-- Password -->
    <div class="w-full">
      <label class="register-label">Password</label>
      <input type="password" bind:value={password} placeholder="Enter password" class="register-input" />
    </div>
  
    <!-- Confirm Password -->
    <div class="w-full">
      <label class="register-label" >Confirm Password</label>
      <input type="password" bind:value={confirmPassword} placeholder="Re-enter password" class="register-input" />
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

    <!-- Back to Login button -->
    <div class="strength-nav">
       <button class="strength-nav-btn" on:click={handleBack}>&lt; Go Back</button>
    </div>
  </div>
  