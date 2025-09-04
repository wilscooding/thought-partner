<script lang="ts">
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto } from '$app/navigation';
  import { userSelection } from '$lib/stores/userSelection'; // Import your store
  import { onMount } from 'svelte';
  import { fetchOptions } from '$lib/services/options';
  
  let selectedGuidance = '';
  let guidanceOptions: Array<{ label: string; value: string }> = [];

  onMount(async () => {
    try {
      const data = await fetchOptions();
      guidanceOptions = data?.guidance?.options ?? []; // safe access
    } catch (err) {
      console.error('Failed to fetch guidance options:', err);
      guidanceOptions = []; // fallback so the page doesn't crash
    }
  });

const handleNext = () => {
  if (!selectedGuidance) return;
  userSelection.update(s => {
    const updated = { ...s, capability_area: selectedGuidance };
    console.log('Updated userSelection (guidance):', updated);
    return updated;
  });
  goto('/match/personality');
};

    const handleBack = () => {
      goto('/match/industry');
    };
  </script>
  
  <MenuWrapper>
    <div class="match-container">
      <h2 class="match-heading">
        What kind of<br />
        guidance are you<br />
        looking for today?
      </h2>
  
      <select class="match-select" bind:value={selectedGuidance}>
        <option value="" disabled>Select a focus area</option>
        {#each guidanceOptions as option}
          <option value={option.value}>{option.label}</option>
        {/each}
      </select>
  
      <div class="match-nav">
        <button class="match-nav-btn" on:click={handleBack}>&lt; Back</button>
        <button class="match-nav-btn" on:click={handleNext}>Next &gt;</button>
      </div>
    </div>
  </MenuWrapper>
  