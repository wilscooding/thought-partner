<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { page } from '$app/stores';
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
  
    let name = '';
    let selectedIndustry = '';
    let selectedCapability = '';
  
    const industryOptions = [
      "Construction", "Education Services", "Entertainment", "Finance & Insurance",
      "Healthcare & Social Assistance", "Hospitality & Food Services", "Manufacturing",
      "Professional & Business Services", "Real Estate", "Retail & E-commerce", "Transportation & Logistics"
    ];
  
    const capabilityOptions = [
      "Customer Experience", "Finance", "Marketing & Sales", "Operations", "People & Culture",
      "Product & Innovation", "Risk & Compliance", "Strategy & Vision", "Sustainability & Social Impact",
      "Technology & Data"
    ];
  
    $: name = $page.params.name?.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
  
    function connect() {
      // Here’s where you’d route or submit values to backend
      console.log(`Connecting with ${name} on ${selectedIndustry} & ${selectedCapability}`);
    }
  
    function goBack() {
      goto('/tp-profiles');
    }
  </script>
  
  <MenuWrapper>
    <div class="tp-connect-container">
      <h2 class="tp-connect-heading">Before We Connect You</h2>
  
      <hr class="tp-divider" />
  
      <p class="tp-connect-description">
        You haven’t connected with {name} yet.
        <br />
        Make a few quick selections below to help guide your conversation and let {name} know where to focus.
      </p>
  
      <hr class="tp-divider" />
  
      <div class="tp-connect-field">
        <label class="tp-label">What industry are you working in or thinking about today?</label>
        <select bind:value={selectedIndustry} class="tp-select">
          <option value="" disabled selected>-- Select Industry --</option>
          {#each industryOptions as industry}
            <option value={industry}>{industry}</option>
          {/each}
        </select>
      </div>
  
      <div class="tp-connect-field">
        <label class="tp-label">What kind of guidance are you looking for today?</label>
        <select bind:value={selectedCapability} class="tp-select">
          <option value="" disabled selected>-- Select Guidance --</option>
          {#each capabilityOptions as option}
            <option value={option}>{option}</option>
          {/each}
        </select>
      </div>
  
      <button class="tp-connect-button" on:click={handleConnect}>Connect Me</button>
      <button class="tp-change-button" on:click={() => goto('/tp-profiles')}>Change Thought Partner</button>

    </div>
  </MenuWrapper>
  