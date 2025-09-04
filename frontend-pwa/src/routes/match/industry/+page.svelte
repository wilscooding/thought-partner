<script>
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto } from '$app/navigation';
  import { userSelection } from '$lib/stores/userSelection';
  import { onMount } from 'svelte';
  import { fetchOptions } from '$lib/services/options';
  
  let selectedIndustry = '';
  let options: Array<{ label: string; value: string }> = [];


onMount(async () => {
  try {
    const data = await fetchOptions();
    options = data?.industry?.options ?? []; // safe access
  } catch (err) {
    console.error('Failed to fetch industries:', err);
    options = []; // fallback so the page doesn't crash
  }
});


const handleNext = () => {
  if (!selectedIndustry) return;
  userSelection.update(s => ({ ...s, industry: selectedIndustry }));
  goto('/match/guidance');  
};
</script>
  
<MenuWrapper>
  <div class="match-container">
    <h2 class="match-heading">What industry are you working in or thinking about today?</h2>

    <select bind:value={selectedIndustry} class="match-select">
      <option value="" disabled>Select an industry</option>
      {#each options as industry}
        <option value={industry.value}>{industry.label}</option>
      {/each}
    </select>

    <div class="match-nav">
      <button class="match-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
</MenuWrapper>
  