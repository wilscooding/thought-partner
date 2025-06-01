<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
    import { userSelection } from '$lib/stores/userSelection.js'; // Import your store
  
    let selectedGuidance = '';
  
    const guidanceOptions = [
      "Customer Experience",
      "Finance",
      "Marketing & Sales",
      "Operations",
      "People & Culture",
      "Product & Innovation",
      "Risk & Compliance",
      "Strategy & Vision",
      "Sustainability & Social Impact",
      "Technology & Data"

    ];
  
    // const handleNext = () => {
    //   if (selectedGuidance) {
    //     userSelection.update(selection => ({ ...selection, capability_area: selectedGuidance }));
    //     goto('/match/personality');
    //   }
    // };
    const handleNext = () => {
  if (selectedGuidance) {
    userSelection.update(selection => {
      const updated = { ...selection, capability_area: selectedGuidance };
      console.log('Updated userSelection (guidance):', updated);
      return updated;
    });
    goto('/match/personality');
  }
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
        <option value="" disabled selected>Select a focus area</option>
        {#each guidanceOptions as option}
          <option value={option}>{option}</option>
        {/each}
      </select>
  
      <div class="match-nav">
        <button class="match-nav-btn" on:click={handleBack}>&lt; Back</button>
        <button class="match-nav-btn" on:click={handleNext}>Next &gt;</button>
      </div>
    </div>
  </MenuWrapper>
  