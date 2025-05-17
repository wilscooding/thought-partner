<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
    import { goto } from '$app/navigation';
  
    const matchedTP = {
      name: 'Denise Okoro',
      image: '/Denise Okoro.png',
      bio: `Denise helps you move from possibility to action. 
      She's an energizing voice who brings clarity, momentum, and confidence when you’re ready to take the next step.`
    };
  
    const handleConnect = () => {
      goto('/dialing'); // Update path as needed
    };
    const handleStartOver = () => goto('/match');
  </script>
  
  <MenuWrapper>
    <div class="match-result-container">
      <h2 class="match-heading">You’ve Been Matched</h2>
  
      <div class="match-profile">
        <img src={matchedTP.image} alt={matchedTP.name} class="match-avatar" />
        <h3 class="match-name">{matchedTP.name}</h3>
      </div>
  
      <p class="match-bio">{matchedTP.bio}</p>
  
      <button class="match-connect-btn" on:click={handleConnect}>Connect</button>
      <button class="match-startover-btn" on:click={handleStartOver}>Start Over</button>
    </div>
  </MenuWrapper>
  