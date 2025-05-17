<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
  
    let selectedPersonality = '';
  
    const personalityTypes = [
      "Grounded Realist",
      "Bold Provocateur",
      "Curious Connector",
      "Clear-eyed Strategist",
      "Empathetic Challenger"
    ];
  
    const handleNext = () => {
      if (selectedPersonality) goto('/match/gender');
    };
  
    const handleBack = () => {
      goto('/match/guidance');
    };
  </script>
  
  <MenuWrapper>
    <div class="match-container">
      <h2 class="match-heading">
        What kind of personality<br />
        would you like to talk to?
      </h2>
  
      <select class="match-select" bind:value={selectedPersonality}>
        <option value="" disabled selected>Select a personality type</option>
        {#each personalityTypes as type}
          <option value={type}>{type}</option>
        {/each}
      </select>
  
      <div class="match-nav">
        <button class="match-nav-btn" on:click={handleBack}>&lt; Back</button>
        <button class="match-nav-btn" on:click={handleNext}>Next &gt;</button>
      </div>
    </div>
  </MenuWrapper>
  