<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
  
    const handleStart = () => goto('/match/industry');
  </script>
  
  <MenuWrapper>
    <div class="tp-match-container">
      <h1 class="tp-match-heading">Let's Find Your Thought Partner</h1>
  
      <p class="tp-match-description">
        We’ll match you based on your goals, style, and what you’re looking for right now.
        Think of it like flipping through a Rolodex — but way faster.
      </p>
  
      <button class="tp-match-button" on:click={handleStart}>Find A Partner</button>
  
     
    </div>
  </MenuWrapper>
  