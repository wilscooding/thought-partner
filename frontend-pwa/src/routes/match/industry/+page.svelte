<script>
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto } from '$app/navigation';
  import { userSelection } from '$lib/stores/userSelection';
  import { onMount } from 'svelte';
  
  let selectedIndustry = '';
  let options = [];


onMount(async () => {
  try {
    const res = await fetch('http://localhost:8000/api/options');
    const data = await res.json();
    options = data.industry.options; // ✅ Make sure you're accessing `data.industry.options`
  } catch (err) {
    console.error('Failed to fetch industries:', err);
  }
});


const handleNext = () => {
  if (selectedIndustry) {
    userSelection.update(s => ({ ...s, industry: selectedIndustry }));
    goto('/match/guidance');
  }
};

</script>
  
<MenuWrapper>
  <div class="match-container">
    <h2 class="match-heading">What industry are you working in or thinking about today?</h2>

    <select bind:value={selectedIndustry} class="match-select">
      <option value="" disabled selected>Select an industry</option>
      {#each options as industry}
        <option value={industry.value}>{industry.label}</option>
      {/each}
    </select>

    <div class="match-nav">
      <button class="match-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
</MenuWrapper>
  