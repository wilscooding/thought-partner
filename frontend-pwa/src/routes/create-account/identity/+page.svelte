<script>
    import { goto } from '$app/navigation';
    let selectedIdentity = '';
  
    const handleNext = () => {
      if (selectedIdentity) {
        goto('/create-account/experience');
      } else {
        alert('Please select your professional identity to continue.');
      }
    };

    const handleBack = () => history.back();

    const identityOptions = [
      'Career Changer / Explorer',
      'Entrepreneur / Founder',
      'Independent Consultant / Coach',
      'Individual Contributor (non-manager)',
      'Nonprofit or Mission-Driven Professional',
      'People Manager / Team Lead',
      'Senior Leader / Executive',
      'Side Hustler / Aspiring Founder',
      'Student / Early Career Professional'
    ];
  </script>
  
  <div class="create-container">
    <!-- Logo -->
    <div class="logo-container"> 

       <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
    </div>  
    <!-- Heading -->
     <div class="content-container">

       <h2 class="identity-heading">What's your<br />professional identity?</h2>
       <p class="identity-subheading">
         (Pick the one that feels closest right now — you can always update it later.)
       </p>
     </div>
  
  <!-- identity Drop down -->
  <select bind:value={selectedIdentity} class="drop-select">
    <option value="" disabled selected>Select your professional identity</option>
    {#each identityOptions as option}
      <option value={option}>{option}</option>
    {/each}   
  </select>
  
    <!-- Navigation Buttons -->
    <div class="identity-nav">
      <button class="identity-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="identity-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
  