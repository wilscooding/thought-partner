<script>
    import { page } from '$app/stores';
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
	import { onMount } from 'svelte';
  
    let tp = null;
    let error = null;

    $: name = $page.params.name;


    onMount(async () => {
        try {
            const response = await fetch(`http://localhost:8000/api/tp-profiles/${name}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            tp = await response.json();
        } catch (err) {
            error = err.message;
        }
    })
  </script>
  
  <MenuWrapper>
    {#if error}
      <p class="text-center text-red-600 p-6">{error}</p>
    {:else if tp}
      <div class="tp-profile-container">
        <img src={`/${tp.name}.png`} alt={tp.name} class="tp-profile-avatar" />
        <h2 class="tp-profile-name">{tp.name}</h2>
        <p class="tp-profile-bio">{tp.description}</p>
  
        <button class="tp-profile-connect">Connect</button>
  
        <div class="tp-profile-back">
          <a href="/tp-profiles" class="text-lg font-bold">&lt; Back</a>
        </div>
      </div>
    {:else}
      <p class="text-center p-6">Loading...</p>
    {/if}
  </MenuWrapper>
  