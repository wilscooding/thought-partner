<script>
    import { goto } from '$app/navigation';
    let selectedStrength = '';
  
    const handleNext = () => {
      if (selectedStrength) {
        goto('/create-account/challenges');
      } else {
        alert('Please select a strength to continue.');
      }
    };
    const handleBack = () => history.back();
    const strengthOptions = [
      'Building relationships or partnerships',
      'Coaching or mentoring',
      'Communicating & connecting with others',
      'Creativity & innovation',
      'Getting things done / execution',
      'Organizing chaos / creating structure',
      'Solving tough problems',
      'Staying calm under pressure',
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

       <h2 class="strength-heading">
         What’s a strength that<br />
         comes naturally to you<br />
         at work?
       </h2>
       <p class="strength-subheading">
         (That thing you do so well it almost feels effortless.)
       </p>
     </div>
  
    <!-- Strength Drop Down -->
    <select bind:value={selectedStrength} class="drop-select">
      <option value="" disabled selected>Select your strength</option>
      {#each strengthOptions as option}
        <option value={option}>{option}</option>
      {/each} 
    </select>
  
    <!-- Navigation Buttons -->
    <div class="strength-nav">
      <button class="strength-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="strength-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
  