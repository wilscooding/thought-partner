<script>
    import { goto } from '$app/navigation';
    let selectedIdentity = '';
  
    const handleNext = () => goto('/create-account/experience');
    const handleBack = () => history.back();
  </script>
  
  <div class="identity-container">
    <!-- Logo -->
    <img src="/logo.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="identity-heading">What's your<br />professional identity?</h2>
    <p class="identity-subheading">
      (Pick the one that feels closest right now — you can always update it later.)
    </p>
  
    <!-- Identity Options -->
    <div class="w-full">
      {#each [
        'Career Changer / Explorer',
        'Entrepreneur / Founder',
        'Independent Consultant / Coach',
        'Individual Contributor (non-manager)',
        'Nonprofit or Mission-Driven Professional',
        'People Manager / Team Lead',
        'Senior Leader / Executive',
        'Side Hustler / Aspiring Founder',
        'Student / Early Career Professional'
      ] as identity}
        <label class="identity-option-label">
          <input
            type="radio"
            class="identity-radio"
            bind:group={selectedIdentity}
            value={identity}
          />
          {identity}
        </label>
      {/each}
    </div>
  
    <!-- Navigation Buttons -->
    <div class="identity-nav">
      <button class="identity-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="identity-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
  