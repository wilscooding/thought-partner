<script>
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import { matchedTP } from '$lib/stores/matchedTP.js'; // Import the store

   
  let thoughtPartners = [];

  onMount(async () => {
    // Simulate fetching data from an API or database
    const response = await fetch('http://localhost:8000/api/tp-profiles'); 
    const data = await response.json();

    thoughtPartners = data.sort((a, b) => a.name.localeCompare(b.name)); // Sort alphabetically by name

  });



const navigateToProfile = (tp) => {
  console.log('🧠 Selected Thought Partner:', tp); // Log everything in the object

  matchedTP.set(tp); // Save to store
  const slug = tp.name.toLowerCase().replace(/\s+/g, '-');
  goto(`/tp-profiles/${slug}`);
};


  // const navigateToProfile = (name) => {
  // const slug = name.toLowerCase().replace(/\s+/g, '-');
  // goto(`/tp-profiles/${slug}`);
  // };
</script>
  
<MenuWrapper>
    <div class="tp-container">
      <h2 class="tp-title">Our Thought Partners</h2>
      <div class="tp-grid">
        {#each thoughtPartners as tp}
          <div class="tp-card" on:click={() => navigateToProfile(tp)} style="cursor: pointer;">
            <img src={`/${tp.name}.png`} alt={tp.name} class="tp-avatar" />
            <span class="tp-name">{tp.name}</span>
          </div>
        {/each}
      </div>
    </div>
</MenuWrapper>