<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
    import { userSelection } from '$lib/stores/userSelection.js'; // Import your store
  
    let selectedGender = '';
  
    const genderOptions = [
      "Woman",
      "Man",
      "Non-Binary",
      "No Preference"
    ];
  
  
  const handleNext = () => {
    let genderToSave = selectedGender;

    if (selectedGender === 'No Preference') {
      const options = ["Woman", "Man", "Non-Binary"];
      const randomIndex = Math.floor(Math.random() * options.length);
      genderToSave = options[randomIndex];
      console.log('🎲 No preference selected. Randomly assigned gender:', genderToSave);
    }

    userSelection.update(selection => {
      const updated = { ...selection, gender: genderToSave };
      console.log('✅ Updated userSelection (gender):', updated);
      return updated;
    });

    goto('/match/result');
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
  