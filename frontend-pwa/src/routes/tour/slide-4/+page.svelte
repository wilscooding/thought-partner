<script>
    import { goto } from '$app/navigation';
  
    const handleNext = () => goto('/tour/slide-5');
    const handleSkip = () => goto('/home');
  </script>
  
  <div class="tour-container">
    <!-- Logo -->
    <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="tour-heading">Pick up where you left<br />off — or shift direction.</h2>
  
    <!-- Icon -->
    <img src="/tour-shift-icon.png" alt="Restart Icon" class="tour-icon" />
  
    <!-- Description -->
    <p class="tour-description">
      You can always reconnect with a Thought Partner you’ve already met. And when you do, you’ll have the chance to adjust the focus of your next conversation. Because you’re always evolving — and so are your needs.
    </p>
  
    <!-- Navigation -->
    <div class="tour-nav">
      <button class="tour-nav-btn" on:click={handleSkip}>&lt; Skip Tour</button>
      <button class="tour-nav-btn" on:click={handleNext}>Keep Going &gt;</button>
    </div>
  </div>
  