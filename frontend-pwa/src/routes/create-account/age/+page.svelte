<script>
    import { goto } from '$app/navigation';
    let selectedAge = '';
  
    const handleNext = () => goto('/create-account/gender');
    const handleBack = () => history.back();
  </script>
  
  <div class="ca-container">
    <!-- Logo -->
    <img src="/logo-small.png" alt="Logo" class="w-16 h-16 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="age-heading">What age range are you in? Optional.</h2>
    <p class="age-subheading">(Knowing your age range helps us fine-tune your experience.)</p>
  
    <!-- Age Options -->
    <div class="w-full">
      {#each [
        '18–24', '25–34', '35–44', '45–54', '55–64', '65+', 'Prefer not to say'
      ] as age}
        <label class="age-option-label">
          <input
            type="radio"
            class="age-radio"
            bind:group={selectedAge}
            value={age}
          />
          {age}
        </label>
      {/each}
    </div>
  
    <!-- Navigation Buttons -->
    <div class="age-nav">
        <button class="age-nav-btn" on:click={handleBack}>
        &lt; Go Back
        </button>
        <button class="age-nav-btn" on:click={handleNext}>
         Next &gt;
        </button>
    </div>
  
  </div>
  