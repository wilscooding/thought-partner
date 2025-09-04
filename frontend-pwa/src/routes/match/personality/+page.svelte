<script>
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto } from '$app/navigation';
  import { userSelection } from '$lib/stores/userSelection'; // Import your store
  import { onMount } from 'svelte';
  import { fetchOptions } from '$lib/services/options';
  
  let selectedPersonality = '';
  let personalityOptions: Array<{ label: string; value: string }> = [];

  onMount(async () => {
    try {
      const data = await fetchOptions();
      personalityOptions = data?.personality?.options ?? []; // safe access
    } catch (err) {
      console.error('Failed to fetch personality options:', err);
      personalityOptions = []; // fallback so the page doesn't crash
    }
  });

  const handleNext = () => {
    if (!selectedPersonality) return;
    userSelection.update(s => ({ ...s, personality_type: selectedPersonality }));
    goto('/match/gender');
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
        <option value="" disabled>Select a personality type</option>
        {#each personalityOptions as option}
          <option value={option.value}>{option.label}</option>
        {/each}
      </select>
  
      <div class="match-nav">
        <button class="match-nav-btn" on:click={handleBack}>&lt; Back</button>
        <button class="match-nav-btn" on:click={handleNext}>Next &gt;</button>
      </div>
    </div>
  </MenuWrapper>
  