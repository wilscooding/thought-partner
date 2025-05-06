<script>
    import { goto } from '$app/navigation';
    let selectedStrength = '';
  
    const handleNext = () => goto('/create-account/challenges');
    const handleBack = () => history.back();
  </script>
  
  <div class="strength-container">
    <!-- Logo -->
    <img src="/logo.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="strength-heading">
      What’s a strength that<br />
      comes naturally to you<br />
      at work?
    </h2>
    <p class="strength-subheading">
      (That thing you do so well it almost feels effortless.)
    </p>
  
    <!-- Strength Options -->
    <div class="w-full">
      {#each [
        'Building relationships or partnerships',
        'Coaching or mentoring',
        'Communicating & connecting with others',
        'Creativity & innovation',
        'Getting things done / execution',
        'Organizing chaos / creating structure',
        'Solving tough problems',
        'Staying calm under pressure',
        'Vision & big-picture thinking'
      ] as strength}
        <label class="strength-option-label">
          <input
            type="radio"
            class="strength-radio"
            bind:group={selectedStrength}
            value={strength}
          />
          {strength}
        </label>
      {/each}
    </div>
  
    <!-- Navigation Buttons -->
    <div class="strength-nav">
      <button class="strength-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="strength-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
  