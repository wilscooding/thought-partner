<script>
    import { goto } from '$app/navigation';
    let selectedAge = '';
  
  const handleNext = () => {
    if (selectedAge) {
      goto('/create-account/gender');
    } else {
      alert('Please select your age range to continue.');
    }
  };    
  const handleBack = () => history.back();

  const ageOptions = [
    '18–24', '25–34', '35–44', '45–54', '55–64', '65+', 'Prefer not to say'
  ];
  </script>
  
  <div class="create-container">
    <!-- Logo -->
    <div class="logo-container"> 

       <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
    </div>    
    <!-- Heading -->
     <div class="content-container">

       <h2 class="age-heading">What age range are you in? Optional.</h2>
       <p class="age-subheading">(Knowing your age range helps us fine-tune your experience.)</p>
     </div>
  
    <!-- Age Dropdown -->
  <select bind:value={selectedAge} class="drop-select">
    <option value="" disabled selected>Select your age range</option>
    {#each ageOptions as option}
      <option value={option}>{option}</option>
    {/each}
  </select>
  
  
  <!-- Navigation Buttons -->
    <div class="age-nav">
        <button class="age-nav-btn" on:click={handleBack}>
        &lt; Go Back
        </button>
        <button class="age-nav-btn" on:click={handleNext}>
         Next &gt;
        </button>
    </div>
  
  </div>
  