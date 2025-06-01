<script>
    import { goto } from '$app/navigation';
    let selectedGender = '';
  
    const handleNext = () => {
      if (selectedGender) {
        goto('/create-account/identity');
      } else {
        alert('Please select your gender to continue.');
      }
    };
    const handleBack = () => history.back();

    const genderOptions = [
      'As A Woman',
      'As A Man',
      'As Non-Binary',
      'Prefer Not to Say'
    ];
  </script>
  
  <div class="create-container">
    <!-- Logo -->
     <div class="logo-container"> 

       <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
     </div>
  
     <!-- Heading + Subtext -->
    <div class="content-container">
      <h2 class="gender-heading">What’s your gender?<br />Optional.</h2>
      <p class="gender-subheading">
        (Tell us how you identify — it helps us personalize your experience.)
      </p>
    </div>
    <!-- gender dropdown -->
    <select bind:value={selectedGender} class="drop-select">
      <option value="" disabled selected>Select your gender</option>
      {#each genderOptions as option}
        <option value={option}>{option}</option>
      {/each} 
    </select>
  
    <!-- Navigation Buttons -->
    <div class="gender-nav">
      <button class="gender-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="gender-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
  