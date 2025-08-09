<script>
    import { goto } from '$app/navigation';
    let selectedChallenge = '';
  
    const handleNext = () => {
      if (selectedChallenge) {
        goto('/create-account/complete');
      } else {
        alert('Please select a challenge to continue.');
      }
    };
    const handleBack = () => history.back();
    const challengeOptions = [
      'Balancing everything at once',
      'Building a team or finding support',
      'Communicating or influencing',
      'Creativity & innovation',
      'Making confident decisions',
      'Managing stress or burnout',
      'Solving tough problems',
      'Turning ideas into action',
      'Vision & big-picture thinking'
    ];
  </script>
  
  <div class="create-container">
    <!-- Logo -->
    <div class="logo-container"> 

       <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
    </div>    
    <!-- Heading -->
     <div class="content-container">

       <h2 class="challenge-heading">
         What's a challenge you<br />face in your work or<br />business?
       </h2>
       <p class="challenge-subheading">
         (We ask so we can better support you —<br />
         no judgment, promise.)
       </p>
     
     </div>
  
    <!-- Challenge Dropdown -->
    <select bind:value={selectedChallenge} class="drop-select">
      <option value="" disabled>Select your challenge</option>
      {#each challengeOptions as option}
        <option value={option}>{option}</option>
      {/each} 
    </select>
  
    <!-- Navigation Buttons -->
    <div class="challenge-nav">
      <button class="challenge-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="challenge-nav-btn" on:click={handleNext}>Done!</button>
    </div>
  </div>
  