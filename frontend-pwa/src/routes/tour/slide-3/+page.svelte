<script>
    import { goto } from '$app/navigation';
  
    const handleNext = () => goto('/tour/slide-4'); // update when ready
    const handleSkip = () => goto('/home'); // or wherever the user goes after tour
  </script>
  
  <div class="tour-container">
    <!-- Logo -->
    <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end" />

    

    <div class="tour-content mt-20">

        <!-- Heading -->
        <h2 class="tour-heading">Thoughtfully matched,<br />every time.</h2>
      
        <!-- Icon -->
        <img src="/tour-match-icon.png" alt="Matching Icon" class="tour-icon" />
      
        <!-- Description -->
        <p class="tour-description">
          We’ll ask you a few quick questions about what you want to focus on — and the kind of energy you need. From there, we’ll match you with a Thought Partner who fits your goals and style. Like a curated conversation, made just for you.
        </p>
    </div>

  
    <!-- Navigation -->
    <div class="tour-nav">
      <button class="tour-nav-btn" on:click={handleSkip}>&lt; Skip Tour</button>
      <button class="tour-nav-btn" on:click={handleNext}>Keep Going &gt;</button>
    </div>
  </div>
  