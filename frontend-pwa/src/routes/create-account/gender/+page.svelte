<script>
    import { goto } from '$app/navigation';
    let selectedGender = '';
  
    const handleNext = () => goto('/create-account/identity');
    const handleBack = () => history.back();
  </script>
  
  <div class="gender-container">
    <!-- Logo -->
    <img src="/logo.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="gender-heading">What’s your gender?<br />Optional.</h2>
    <p class="gender-subheading">
      (Tell us how you identify — it helps us personalize your experience.)
    </p>
  
    <!-- Gender Options -->
    <div class="w-full">
      {#each [
        'As A Woman',
        'As A Man',
        'As Non-Binary',
        'Prefer Not to Say'
      ] as option}
        <label class="gender-option-label">
          <input
            type="radio"
            class="gender-radio"
            bind:group={selectedGender}
            value={option}
          />
          {option}
        </label>
      {/each}
    </div>
  
    <!-- Navigation Buttons -->
    <div class="gender-nav">
      <button class="gender-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="gender-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
  