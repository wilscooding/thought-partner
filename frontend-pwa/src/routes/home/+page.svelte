<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
  
    const goToReconnect = () => goto('/contacts');
    const goToMatch = () => goto('/match');
  </script>
  
  
  <MenuWrapper>
  <div class="flex flex-col justify-center items-center text-center mt-20 space-y-12">
    <div class="text-left">
      <button class="home-btn" on:click={goToReconnect}>
        Reconnect with a<br />Thought Partner
      </button>
      <p class="home-subtext button-aligned-text">
        (Reconnect with someone you’ve already talked to.)
      </p>
    </div>

    <div class="flex items-center gap-4">
      <div class="home-divider"></div>
      <span class="text-[#141420] font-serif text-sm">Or</span>
      <div class="home-divider"></div>
    </div>

    <div class="text-left">
      <button class="home-btn" on:click={goToMatch}>
        Find a new<br />Thought Partner
      </button>
      <p class="home-subtext button-aligned-text">
        (Search our network to match with someone new.)
      </p>
    </div>
  </div>
</MenuWrapper>
