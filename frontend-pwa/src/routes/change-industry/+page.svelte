<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
  
    let industry = '';
    let guidance = '';
  
    const industries = [
      'Construction',
      'Education Services',
      'Entertainment',
      'Finance & Insurance',
      'Healthcare & Social Assistance',
      'Hospitality & Food Services',
      'Manufacturing',
      'Professional & Business Services',
      'Real Estate',
      'Retail & E-commerce',
      'Transportation & Logistics'
    ];
  
    const guidanceOptions = [
      'Customer Experience',
      'Finance',
      'Marketing & Sales',
      'Operations',
      'People & Culture',
      'Product & Innovation',
      'Risk & Compliance',
      'Strategy & Vision',
      'Sustainability & Social Impact',
      'Technology & Data'
    ];
  
    function handleConnect() {
      // Placeholder logic for now
      console.log(`Selected: ${industry} / ${guidance}`);
      goto('/connect'); // placeholder route
    }
  
    function goToContacts() {
      goto('/contacts');
    }
  </script>
  
  <MenuWrapper>
    <div class="industry-change-container">
      <!-- Question 1 -->
      <h2 class="industry-heading">
        What industry are you working in or thinking about today?
      </h2>
      <select bind:value={industry} class="industry-select">
        <option value="" disabled selected>Select industry</option>
        {#each industries as option}
          <option value={option}>{option}</option>
        {/each}
      </select>
  
      <!-- Question 2 -->
      <h2 class="industry-heading mt-6">
        What kind of guidance are you looking for today?
      </h2>
      <select bind:value={guidance} class="industry-select">
        <option value="" disabled selected>Select guidance</option>
        {#each guidanceOptions as option}
          <option value={option}>{option}</option>
        {/each}
      </select>
  
      <!-- Connect Button -->
      <button class="industry-connect-btn mt-8" on:click={handleConnect}>
        Connect
      </button>
  
      <div class="w-full max-w-xs mt-10">
      <button class="industry-back-btn text-left" on:click={goToContacts}>
        &lt; Contacts
      </button>
    </div>
  </div>
</MenuWrapper>