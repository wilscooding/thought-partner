<script>
    import { goto } from '$app/navigation';
    const handleStart = () => goto('/create-account/main');
  </script>
  
  <div class="min-h-screen flex flex-col items-center justify-center px-6 py-12 text-center space-y-6">
    <img src="/logo.png" alt="Logo" class="w-16 h-16 mb-4" />
  
    <h1 class="ca-title">
      Your Thought<br />
      Partner Awaits!
    </h1>
  
    <div class="ca-description">
      <p>A few quick questions</p>
      <p>to build your profile</p>
      <p>and personalize your</p>
      <p class="tracking-wide">experience.</p>
    </div>
  
    <p class="ca-tagline">(It’ll be worth it, we promise)</p>
  
    <button class="ca-btn-primary mt-6" on:click={handleStart}>
      Get Started
    </button>
  </div>
  