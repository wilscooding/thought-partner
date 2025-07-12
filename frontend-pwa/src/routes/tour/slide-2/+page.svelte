<script>
    import { goto } from '$app/navigation';
  
    const handleNext = () => goto('/tour/slide-3');
    const handleSkip = () => goto('/home'); // or wherever you want to send them
  </script>
  
  <div class="tour-container">
    <!-- Logo -->
    <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="tour-heading">Executive-level insight —<br />made accessible.</h2>
  
    <!-- Icon -->
    <img src="/tour-icon.png" alt="Accessible Icon" class="tour-icon" />
  
    <!-- Description -->
    <p class="tour-description">
      Not everyone has a strategist on speed dial. That’s why we built this space — for people who want a sounding board, a safe place to explore, or guidance that feels out of reach. But the real magic? It happens when you take what you build here and apply it out there.
    </p>
  
    <!-- Navigation -->
    <div class="tour-nav">
      <button class="tour-nav-btn" on:click={handleSkip}>&lt; Skip Tour</button>
      <button class="tour-nav-btn" on:click={handleNext}>Keep Going &gt;</button>
    </div>
  </div>
  