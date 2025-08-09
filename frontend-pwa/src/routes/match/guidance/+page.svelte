<script>
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto } from '$app/navigation';
  import { userSelection } from '$lib/stores/userSelection'; // Import your store
  
  let selectedGuidance = '';
  
  const guidanceOptions = [
    { label: "Customer Experience – Journey mapping, feedback, and loyalty", value: "Customer Experience" },
    { label: "Finance – Budgets, funding, pricing, and financial strategy", value: "Finance" },
    { label: "Marketing & Sales – Reaching customers and driving growth", value: "Marketing & Sales" },
    { label: "Operations – Day-to-day structure, efficiency, and systems", value: "Operations" },
    { label: "People & Culture – Hiring, leadership, team dynamics", value: "People & Culture" },
    { label: "Product & Innovation – Building and improving your offering", value: "Product & Innovation" },
    { label: "Risk & Compliance – Legal, ethical, and operational safeguards", value: "Risk & Compliance" },
    { label: "Strategy & Vision – Big picture thinking, long-term goals, and direction", value: "Strategy & Vision" },
    { label: "Sustainability & Social Impact – Doing good while doing business", value: "Sustainability & Social Impact" },
    { label: "Technology & Data – Tech tools, automation, and data insights", value: "Technology & Data" }
  ];

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
  