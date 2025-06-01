<script>
    import { goto } from '$app/navigation';
    const handleStart = () => goto('/create-account/name');
  </script>
  
  <div class="ca-container items-center text-center">
    <img src="/Logo Gold.png" alt="Logo" class="w-16 h-16 mb-4" />
  
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
  