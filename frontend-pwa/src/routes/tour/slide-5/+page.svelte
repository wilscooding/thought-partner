<script>
    import { goto } from '$app/navigation';
  
    const handleNext = () => goto('/tour/end'); // or complete route
    const handleSkip = () => goto('/home'); // adjust as needed
  </script>
  
  <div class="tour-container">
    <!-- Logo -->
    <img src="" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="tour-heading">Something to take<br />with you.</h2>
  
    <!-- Icon -->
    <img src="/tour-summary-icon.png" alt="Email Icon" class="tour-icon" />
  
    <!-- Description -->
    <p class="tour-description">
      After your session, your Thought Partner will email you a short summary. It may include a few tools or ideas to help you move forward — just a light touchpoint to keep the momentum going.
    </p>
  
    <!-- Navigation -->
    <div class="tour-nav">
      <button class="tour-nav-btn" on:click={handleSkip}>&lt; Skip Tour</button>
      <button class="tour-nav-btn" on:click={handleNext}>Keep Going &gt;</button>
    </div>
  </div>
  