<script>
    import { goto } from '$app/navigation';
    const handleNext = () => goto('/tour/slide-2');
    const handleSkip = () => goto('/');
  </script>
  
  <div class="tour-container">
    <!-- Logo -->
    <img src="/Logo Gold.png" alt="Logo" class="w-10 h-10 self-end mb-8" />
  
    <!-- Title -->
    <h2 class="tour-heading">Conversations,<br />Not Commands.</h2>
  
    <!-- Icon -->
    <img src="/chat-icon.png" alt="Chat" class="tour-icon" />
  
    <!-- Description -->
    <p class="tour-description">
      Your Thought Partner isn’t an assistant — they’re here to think with you, not just for you.
      There might be a slight pause as they reflect and respond, so take your time. Try not to rush.
      Ask questions, explore ideas, and treat it like a real conversation — because it is.
    </p>
  
    <!-- Navigation -->
    <div class="tour-nav">
      <button class="tour-nav-btn" on:click={handleSkip}>&lt; Skip Tour</button>
      <button class="tour-nav-btn" on:click={handleNext}>Keep Going &gt;</button>
    </div>
  </div>
  