<script>
    import { goto } from '$app/navigation';
    let selectedExperience = '';
  
    const handleNext = () => {
      if (selectedExperience) {
        goto('/create-account/strengths');
      } else {
        alert('Please select your years of experience to continue.');
      }
    };
    const handleBack = () => history.back();

    const experienceOptions = [
      'Less than 1 Year',
      '1–3 years',
      '4–7 Years',
      '8–15 Years',
      '15+ Years'
    ];
  </script>
  
  <div class="create-container">
    <!-- Logo -->
    <div class="logo-container"> 

       <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
    </div>    
    <!-- Heading -->
     <div class="content-container">

       <h2 class="experience-heading">Roughly how many<br />years of experience do<br />you have?</h2>
       <p class="experience-subheading">
         (Whether you’re building on it or switching things up,<br />
         this just helps give us some context.)
       </p>
     </div>
  
    <!-- Experience Dropdown -->
    <select bind:value={selectedExperience} class="drop-select">
      <option value="" disabled selected>Select your years of experience</option>
      {#each experienceOptions as option}
        <option value={option}>{option}</option>
      {/each} 
    </select>
    
    <!-- Navigation Buttons -->
    <div class="experience-nav">
      <button class="experience-nav-btn" on:click={handleBack}>&lt; Go Back</button>
      <button class="experience-nav-btn" on:click={handleNext}>Next &gt;</button>
    </div>
  </div>
  