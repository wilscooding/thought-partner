<script>
    import { goto } from '$app/navigation';
  
    let firstName = '';
    let lastName = '';
  
    function handleNext()  {
      if (firstName && lastName) {
        goto('/create-account/age');
      } else {
        alert('Please enter both your first and last name to continue.');
      }
    }
  </script>
  
  <div class="create-container items-center">
    <!-- Logo -->
    <div class="logo-container"> 

       <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
    </div>  
    <!-- Question -->
     <div class="content-container">

       <h2 class="name-heading">
         Let’s get personal –<br />
         what should we call you?
       </h2>
     </div>
  
    <!-- First Name -->
    <div class="w-full">
      <label class="name-label">First Name</label>
      <input type="text" placeholder="First Name" bind:value={firstName} class="name-input" />
    </div>
  
    <!-- Last Name -->
    <div class="w-full">
      <label class="name-label mt-4">Last Name</label>
      <input type="text" placeholder="Last Name" bind:value={lastName} class="name-input" />
    </div>
  
    <!-- Next Button -->
    <div class="w-full flex justify-end mt-8">
      <button class="name-next-btn" on:click={handleNext}>
        Next &gt;
      </button>
    </div>
  </div>
  