<script>
    import { goto } from '$app/navigation';
  
    let firstName = '';
    let lastName = '';
  
    function handleNext() {
      goto('/create-account/age');
    }
  </script>
  
  <div class="ca-container items-center">
    <!-- Logo -->
    <img src="/logo-small.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Question -->
    <h2 class="name-heading">
      Let’s get personal –<br />
      what should we call you?
    </h2>
  
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
  