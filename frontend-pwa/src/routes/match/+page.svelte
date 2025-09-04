<script lang="ts">
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto, preloadCode, preloadData } from '$app/navigation';
  import { onMount } from 'svelte';
  import { fetchOptions } from '$lib/services/options'; // the memoized helper we added

  onMount(async () => {
    // Preload route code so next screens feel instant
    const routes = [
      '/match/industry',
      '/match/guidance',
      '/match/personality',
      '/match/gender',
      '/match/result'
    ];
    // ignore individual failures; this is just a hint
    await Promise.all(routes.map((r) => preloadCode(r).catch(() => {})));

    // Optionally warm data for the *first* route if it uses +page.(ts|js) load()
    // (If your page fetches in onMount, this won't affect it; we also call fetchOptions() below.)
    preloadData('/match/industry').catch(() => {});

    // Warm the options cache used by all match pages
    fetchOptions().catch(() => {});
  });

  const handleStart = () => goto('/match/industry');
</script>

<MenuWrapper>
  <div class="tp-match-container">
    <h1 class="tp-match-heading">Let's Find Your Thought Partner</h1>

    <p class="tp-match-description" id="intro">
      We’ll match you based on your goals, style, and what you’re looking for right now.
      Think of it like flipping through a Rolodex — but way faster.
    </p>

    <button class="tp-match-button" type="button" aria-describedby="intro" on:click={handleStart}>
      Find A Partner
    </button>
  </div>
</MenuWrapper>
