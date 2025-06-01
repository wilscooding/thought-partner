<script>
    import { goto } from '$app/navigation';
    const handleStart = () => goto('/'); // adjust path for your match/start screen
  </script>
  
  <div class="tour-container">
    <!-- Logo -->
    <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Heading -->
    <h2 class="tour-heading">Ready when you are.</h2>
  
    <!-- Play Icon -->
    <img src="" alt="Play Icon" class="tour-icon" />
  
    <!-- Description -->
    <p class="tour-description">
      Your Thought Partner is just a few steps away. Let’s start the conversation.
    </p>
  
    <!-- CTA Button -->
    <button class="tour-cta-btn mt-6" on:click={handleStart}>
      Find A Thought Partner
    </button>
  </div>
  