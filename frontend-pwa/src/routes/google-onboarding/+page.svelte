<script>
    import { goto } from '$app/navigation';
    import { currentUser } from '$lib/stores/userStore';
    let agreedToTerms = false;
    let isAdult = false;
  
    const handleContinue = () => {
      if (agreedToTerms && isAdult) {
        // Update user profile in backend if needed here
  
        goto('/home'); // Redirect to home/dashboard
      } else {
        alert("Please accept the terms and confirm your age to continue.");
      }
    };
  </script>
  
  <div class="onboarding-container flex flex-col items-center justify-center min-h-screen bg-[#141420] text-[#e9e4d3] font-serif px-8 py-10">
    <img src="/Logo Gold.png" alt="Logo" class="w-16 h-16 mb-6" />
  
    <h1 class="text-2xl font-bold mb-4 text-center">Almost there...</h1>
    <p class="text-sm text-center mb-8 max-w-xs">
      Please review and accept the terms before continuing.
    </p>
  
    <!-- Terms & Conditions Toggle -->
    <div class="onboarding-toggle mt-4">
      <button
        class={`w-12 h-6 rounded-full transition-colors duration-300 ${agreedToTerms ? 'bg-[#c6b06e]' : 'bg-[#3a3b4b]'}`}
        on:click={() => (agreedToTerms = !agreedToTerms)}
      >
        <div class={`h-6 w-6 bg-[#e9e4d3] rounded-full transform ${agreedToTerms ? 'translate-x-6' : ''} transition-transform duration-300`}></div>
      </button>
      <span class="text-sm">
        I agree to the <a href="/terms" class="underline">terms and conditions</a>.
      </span>
    </div>
  
    <!-- Age Confirmation Toggle -->
    <div class="onboarding-toggle mt-4">
      <button
        class={`w-14 h-6 rounded-full transition-colors duration-300 ${isAdult ? 'bg-[#c6b06e]' : 'bg-[#3a3b4b]'}`}
        on:click={() => (isAdult = !isAdult)}
      >
        <div class={`h-6 w-6 bg-[#e9e4d3] rounded-full transform ${isAdult ? 'translate-x-6' : ''} transition-transform duration-300`}></div>
      </button>
      <span class="text-sm">
        I confirm that I am 18 years of age or older.
      </span>
    </div>
  
    <!-- Continue Button -->
    <button
      class="bg-[#c6b06e] text-[#141420] font-bold text-lg py-2 px-8 rounded-full border border-transparent hover:border-[#e9e4d3] transition-all w-full max-w-xs"
      on:click={handleContinue}
    >
      Continue
    </button>
  </div>
  
  