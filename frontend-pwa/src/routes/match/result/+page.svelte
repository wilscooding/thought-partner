<script>
    import { onMount } from 'svelte';
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
    import { userSelection } from '$lib/stores/userSelection.js'; // Import your store
    import { get } from 'svelte/store'; // Import Svelte's get function to access store values
  
    let matchedTP = null;
    let error = null;
    let loading = true;
  
    let currentSelection;
  
    onMount(async () => {
        const currentSelection = get(userSelection);  // Use Svelte's get() to fetch store value

        try {
            const response = await fetch('http://localhost:8000/api/generate_prompt', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                industry: currentSelection.industry,
                capability_area: currentSelection.capability_area,
                personality_type: currentSelection.personality_type,
                gender: currentSelection.gender,
                user_input_text: "connect me with a Thought Partner.",
                is_first_message: true
            })
            });

            if (!response.ok) throw new Error('Failed to fetch match.');

            const data = await response.json();
            matchedTP = {
            name: data.avatar.name,
            image: `/${data.avatar.name}.png`,
            bio: data.avatar.avatar_blurb
            };

        } catch (err) {
            error = err.message;
        } finally {
            loading = false;
        }
        });

  
    const handleConnect = () => {
      goto(`/dialing?name=${encodeURIComponent(matchedTP.name)}&image=${encodeURIComponent(matchedTP.image)}`);
    };

    const handleStartOver = () => goto('/match');
  </script>
  
  <MenuWrapper>
    <div class="match-result-container">
      {#if loading}
        <div class="typing-loader"> 
          <span class="typed-text">Finding your Thought Partner...</span>
        </div>
      {:else if error}
        <p class="text-red-500">{error}</p>
      {:else if matchedTP}
        <h2 class="match-heading">You’ve Been Matched</h2>
  
        <div class="match-profile">
          <img src={matchedTP.image} alt={matchedTP.name} class="match-avatar" />
          <h3 class="match-name">{matchedTP.name}</h3>
        </div>
  
        <p class="match-bio">{matchedTP.bio}</p>
  
        <button class="match-connect-btn" on:click={handleConnect}>Connect</button>
        <button class="match-startover-btn" on:click={handleStartOver}>Start Over</button>
      {/if}
    </div>
  </MenuWrapper>
  