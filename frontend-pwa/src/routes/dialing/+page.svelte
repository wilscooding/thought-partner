<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';

  let tp = { name: '', image: '' };

  let displayText = '';
  const fullText = "Dialing...";
  let index = 0;

  // Get query parameters from the URL
  $: queryParams = $page.url.searchParams;
  $: tp.name = queryParams.get('name') || 'Thought Partner';
  $: tp.image = queryParams.get('image') || '/default-avatar.png';

  onMount(() => {
    const animateLoop = () => {
      displayText = '';
      index = 0;
      const interval = setInterval(() => {
        displayText += fullText[index];
        index++;
        if (index >= fullText.length) {
          clearInterval(interval);
          setTimeout(animateLoop, 800);
        }
      }, 120);
    };
    animateLoop();
  });

  const handleEndCall = () => {
    alert("Call ended.");
  };
</script>

<div class="dialing-container">
  <!-- Dialing text -->
  <h2 class="dialing-title">{displayText}<br />{tp.name}</h2>

  <!-- Avatar + Logo -->
  <div class="avatar-wrapper">
    <img src={tp.image} alt={tp.name} class="avatar-image" />
    <img src="/Logo Beige.png" alt="Logo" class="dialing-logo" />
  </div>

  <!-- End Call -->
  <button class="end-call-btn" on:click={handleEndCall}>End Call</button>
</div>
