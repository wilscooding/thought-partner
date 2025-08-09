<script>
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';
  import { auth, db } from '$lib/firebase';
  import { matchedTP } from '$lib/stores/matchedTP';
  import { serverTimestamp, doc, setDoc } from 'firebase/firestore';
  import { get } from 'svelte/store';


  
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
  
  

  const handleConnect = async () => {
    const user = auth.currentUser;
    
    if (!user) {
      console.error('❌ User not authenticated');
      return; 
    }

    const tp = get(matchedTP);
    console.log('🤝 Matched Thought Partner:', tp);

    if (!tp || !tp.name) {
      console.error('❌ No matched Thought Partner found:', tp);
      return;
    }

    if (!selectedIndustry || !selectedCapability) {
      alert('⚠️ Please select both industry and guidance before connecting.');
      console.warn('⚠️ Missing selections:', { selectedIndustry, selectedCapability });
      return;
    }

    try {
      const partnerId = tp.id || tp.name.replace(/\s+/g, '-').toLowerCase();
      console.log('📌 Connecting Thought Partner with ID:', partnerId);

      const tpRef = doc(db, 'users', user.uid, 'thoughtPartners', partnerId);
      console.log('📂 Firestore doc ref path:', tpRef.path);

      const tpData = {
        ...tp, // Spread the matched TP data
        industry: selectedIndustry,
        capability: selectedCapability,
        connectedAt: serverTimestamp(), // Use Firestore server timestamp
        notes: []
      };

      console.log('💾 Saving Thought Partner data:', tpData);

      await setDoc(tpRef, tpData);

      console.log('✅ Thought Partner connected successfully');
      goto(`/tp-profiles`); // Use partnerId here!
    } catch (error) {
      console.error('❌ Error connecting Thought Partner:', error);
    }
  };
  
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
          <option value="" disabled>-- Select Industry --</option>
          {#each industryOptions as industry}
            <option value={industry}>{industry}</option>
          {/each}
        </select>
      </div>
  
      <div class="tp-connect-field">
        <label class="tp-label">What kind of guidance are you looking for today?</label>
        <select bind:value={selectedCapability} class="tp-select">
          <option value="" disabled>-- Select Guidance --</option>
          {#each capabilityOptions as option}
            <option value={option}>{option}</option>
          {/each}
        </select>
      </div>
  
      <button class="tp-connect-button" on:click={handleConnect}>Connect Me</button>
      <button class="tp-change-button" on:click={() => goto('/tp-profiles')}>Change Thought Partner</button>

    </div>
  </MenuWrapper>
  