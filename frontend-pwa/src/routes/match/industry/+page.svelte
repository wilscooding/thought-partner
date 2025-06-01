<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
    import { userSelection } from '$lib/stores/userSelection';
  
    let selectedIndustry = '';
  
    const industries = [
      "Construction",
      "Education Services",
      "Entertainment",
      "Finance & Insurance",
      "Healthcare & Social Assistance",
      "Hospitality & Food Services",
      "Manufacturing",
      "Professional & Business Services",
      "Real Estate",
      "Retail & E-commerce",
      "Transportation & Logistics"
    ];
  
    // const handleNext = () => {
    //   if (selectedIndustry) {
    //     userSelection.update(selection => ({ ...selection, industry: selectedIndustry }));
    //     goto('/match/guidance');
    //   }
    // };

    const handleNext = () => {
  if (selectedIndustry) {
    userSelection.update(selection => {
      const updated = { ...selection, industry: selectedIndustry };
      console.log('Updated userSelection (industry):', updated);
      return updated;
    });
    goto('/match/guidance');
  }
};

  </script>
  
  <MenuWrapper>
    <div class="match-container">
      <h2 class="match-heading">
        What industry<br />
        are you working in or thinking<br />
        about today?
      </h2>
  
      <select class="match-select" bind:value={selectedIndustry}>
        <option value="" disabled selected>Select an industry</option>
        {#each industries as industry}
          <option value={industry}>{industry}</option>
        {/each}
      </select>
  
      <div class="match-nav">
        <span></span>
        <button class="match-nav-btn" on:click={handleNext}>Next&gt</button>
      </div>
    </div>
  </MenuWrapper>
  