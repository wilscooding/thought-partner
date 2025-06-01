<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  
    function handleCallback() {
      // Placeholder for callback logic
    }
  
    function handleNewPartner() {
      // Placeholder for connecting to different partner
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
  