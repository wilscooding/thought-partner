<!-- <script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';

  let tp = { name: '', image: '' };

  let displayText = '';
  const fullText = "Dialing...";
  let index = 0;

  // Get query parameters from the URL
  $: queryParams = $page.url.searchParams;
  $: tp.name = queryParams.get('name') || 'Thought Partner';
  $: tp.image = queryParams.get('image') || `/${tp.name}.png`;

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

  setTimeout(() => {
    // After 5 seconds, redirect to the dialing page
    goto(`/speaking?name=${encodeURIComponent(tp.name)}&image=${encodeURIComponent(tp.name)}`);
  }, 5000);

  const handleEndCall = () => {
    goto(`/call-ended?name=${encodeURIComponent(tp.name)}&image=${encodeURIComponent(tp.image)}`);
  };
</script>

<div class="dialing-container">
  Dialing text -->
  <!-- <h2 class="dialing-title">{displayText}<br />{tp.name}</h2>

  Avatar + Logo
  <div class="avatar-wrapper">
    <img src={tp.image} alt={tp.name} class="avatar-image" />
    <img src="/Logo Beige.png" alt="Logo" class="dialing-logo" />
  </div>

  End Call
  <button class="end-call-btn" on:click={handleEndCall}>End Call</button>
</div> -->


<script>
  import { onMount } from 'svelte';
  import { page } from '$app/stores';
  import { goto } from '$app/navigation';

  let tp = { name: '', image: '' };
  let displayText = '';
  const fullText = "Dialing...";
  let index = 0;

  // Load query parameters dynamically
  $: queryParams = $page.url.searchParams;
  $: tp.name = queryParams.get('name') || 'Thought Partner';
  $: tp.image = queryParams.get('image') || `/${tp.name}.png`;

  // Animate "Dialing..." text
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

    // Redirect to /speaking after 5 seconds
    setTimeout(() => {
      goto(`/speaking?name=${encodeURIComponent(tp.name)}&image=${encodeURIComponent(tp.image)}`);
    }, 5000);
  });

  const handleEndCall = () => {
    goto(`/call-ended?name=${encodeURIComponent(tp.name)}&image=${encodeURIComponent(tp.image)}`);
  };
</script>

<div class="dialing-container">
  <h2 class="dialing-title">{displayText}<br />{tp.name}</h2>

  <div class="avatar-wrapper">
    <img src={tp.image} alt={tp.name} class="avatar-image" />
    <img src="/Logo Beige.png" alt="Logo" class="dialing-logo" />
  </div>

  <button class="end-call-btn" on:click={handleEndCall}>End Call</button>
</div>
