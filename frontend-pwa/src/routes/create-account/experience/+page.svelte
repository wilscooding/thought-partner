<script>
    import { goto } from '$app/navigation';
    let selectedExperience = '';
  
    const handleNext = () => goto('/create-account/strengths');
    const handleBack = () => history.back();
  </script>
  
  <div class="experience-container">
    <!-- Logo -->
    <img src="/logo.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="experience-heading">Roughly how many<br />years of experience do<br />you have?</h2>
    <p class="experience-subheading">
      (Whether you’re building on it or switching things up,<br />
      this just helps give us some context.)
    </p>
  
    <!-- Experience Options -->
    <div class="w-full">
      {#each [
        'Less than 1 Year',
        '1–3 years',
        '4–7 Years',
        '8–15 Years',
        '15+ Years'
      ] as option}
        <label class="experience-option-label">
          <input
            type="radio"
            class="experience-radio"
            bind:group={selectedExperience}
            value={option}
          />
          {option}
        </label>
      {/each}
    </div>
  
    <!-- Navigation Buttons -->
    <div class="experience-nav">
      <button class="experience-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="experience-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
  