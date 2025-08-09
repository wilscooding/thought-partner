<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';

    let tp = { name: '', image: '' };

    $: queryParams = $page.url.searchParams;
    $: tp.name = queryParams.get('name');
    $: tp.image = queryParams.get('image') || `/${tp.name}.png`;
  
    function handleCallback() {
  goto(`/dialing?name=${encodeURIComponent(tp.name)}&image=${encodeURIComponent(`/${tp.name}.png`)}`);
}

  
    function handleNewPartner() {
      goto('/match');
    }
  </script>
  
  <MenuWrapper gray>
    <div class="call-ended-container">
      <h2 class="call-ended-title">Call Ended</h2>
      <p class="call-ended-message">
        Thanks for connecting with your Thought Partner. Every conversation brings new insights — you’re welcome to dive back in or explore a different perspective.
      </p>
  
      <div class="call-ended-actions">
        <button class="call-ended-btn solid" on:click={handleCallback}>
          Call Back
        </button>
        <button class="call-ended-btn" on:click={handleNewPartner}>
          Connect with a <br /> Different Thought <br /> Partner
        </button>
      </div>
    </div>
  </MenuWrapper>
  