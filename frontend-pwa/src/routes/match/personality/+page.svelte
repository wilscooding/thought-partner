<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
    import { userSelection } from '$lib/stores/userSelection.js'; // Import your store
  
    let selectedPersonality = '';
  
    const personalityTypes = [
      "The Adaptive Chameleon",
      "The Analytical Architect",
      "The Bold Provocateur",
      "The Curious Explorer",
      "The Empathetic Listener",
      "The Grounded Realist",
      "The Humble Sage",
      "The Quiet Catalyst",
      "The Strategic Optimist"
    ];
  
    // const handleNext = () => {
    //   if (selectedPersonality) {
    //     // Store the selected personality type in a store or pass it to the next page
    //     // For example, using a store like userSelection
    //     userSelection.update(selection => ({ ...selection, personality_type: selectedPersonality }));
    //     goto('/match/gender');
    //   }
    // };

    const handleNext = () => {
  if (selectedPersonality) {
    userSelection.update(selection => {
      const updated = { ...selection, personality_type: selectedPersonality };
      console.log('Updated userSelection (personality):', updated);
      return updated;
    });
    goto('/match/gender');
  }
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
  