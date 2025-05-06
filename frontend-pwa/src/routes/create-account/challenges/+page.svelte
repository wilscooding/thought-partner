<script>
    import { goto } from '$app/navigation';
    let selectedChallenge = '';
  
    const handleNext = () => goto('/create-account/complete'); // or wherever you route next
    const handleBack = () => history.back();
  </script>
  
  <div class="challenge-container">
    <!-- Logo -->
    <img src="/logo.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="challenge-heading">
      What's a challenge you<br />face in your work or<br />business?
    </h2>
    <p class="challenge-subheading">
      (We ask so we can better support you —<br />
      no judgment, promise.)
    </p>
  
    <!-- Challenge Options -->
    <div class="w-full">
      {#each [
        'Balancing everything at once',
        'Building a team or finding support',
        'Communicating or influencing',
        'Creativity & innovation',
        'Making confident decisions',
        'Managing stress or burnout',
        'Solving tough problems',
        'Turning ideas into action',
        'Vision & big-picture thinking'
      ] as challenge}
        <label class="challenge-option-label">
          <input
            type="radio"
            class="challenge-radio"
            bind:group={selectedChallenge}
            value={challenge}
          />
          {challenge}
        </label>
      {/each}
    </div>
  
    <!-- Navigation Buttons -->
    <div class="challenge-nav">
      <button class="challenge-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="challenge-nav-btn" on:click={handleNext}>Done!</button>
    </div>
  </div>
  