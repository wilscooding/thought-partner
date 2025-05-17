<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
  
    let selectedGender = '';
  
    const genderOptions = [
      "Woman",
      "Man",
      "Non-Binary",
      "No Preference"
    ];
  
    const handleNext = () => {
      if (selectedGender) goto('/match/result');
    };
  
    const handleBack = () => {
      goto('/match/personality');
    };
  </script>
  
  <MenuWrapper>
    <div class="match-container">
      <h2 class="match-heading">
        Do you have a gender<br />
        preference for your match?
      </h2>
  
      <select class="match-select" bind:value={selectedGender}>
        <option value="" disabled selected>Select a preference</option>
        {#each genderOptions as gender}
          <option value={gender}>{gender}</option>
        {/each}
      </select>
  
      <div class="match-nav">
        <button class="match-nav-btn" on:click={handleBack}>&lt; Back</button>
        <button class="match-nav-btn" on:click={handleNext}>Next &gt;</button>
      </div>
    </div>
  </MenuWrapper>
  