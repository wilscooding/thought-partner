<script>
    import { onMount } from 'svelte';
  
    const tp = {
      name: "Julian Park",
      image: "/Julian Park.png"
    };
  
    let displayText = '';
    const fullText = "Dialing...";
    let index = 0;
  
    onMount(() => {
      const animateLoop = () => {
        displayText = '';
        index = 0;
        const interval = setInterval(() => {
          displayText += fullText[index];
          index++;
          if (index >= fullText.length) {
            clearInterval(interval);
            setTimeout(animateLoop, 800); // wait, then restart loop
          }
        }, 120); // typing speed
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
  
    <!-- Avatar -->
    <div class="avatar-wrapper">
      <img src={tp.image} alt={tp.name} class="avatar-image" />
      <img src="/logo.png" alt="Thought Partner Logo" class="dialing-logo" />
    </div>
  
    <!-- End Call -->
    <button class="end-call-btn" on:click={handleEndCall}>End Call</button>
  </div>
  