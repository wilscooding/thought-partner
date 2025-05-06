<script>
    import { goto } from '$app/navigation';
    const handleStartTour = () => goto('/tour/start');
    const handleSkip = () => goto('/'); // or dashboard route
  </script>
  
  <div class="complete-container">
    <!-- Logo -->
    <img src="/logo.png" alt="Logo" class="w-14 h-14 mb-4" />
  
    <!-- Heading -->
    <h2 class="complete-heading">You're all set<br />— nicely done!</h2>
  
    <!-- Subtext -->
    <p class="complete-subtext">
      Now let’s give you some quick tips so you can make the most of your Thought Partner experience.
    </p>
  
    <!-- Start Tour Button -->
    <button class="complete-start-btn mt-4" on:click={handleStartTour}>
      Start the Tour
    </button>
  
    <!-- Skip Tour aligned right -->
    <div class="w-full max-w-xs flex justify-end">
        <button class="complete-skip-btn" on:click={handleSkip}>
        Skip Tour
        </button>
    </div>
  
  </div>
  