<script>
  import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  import { goto } from '$app/navigation';
  import { userSelection } from '$lib/stores/userSelection'; // Import your store
  
  let selectedPersonality = '';

  const personalityOptions = [
    { label: "Someone flexible who can meet me wherever I’m at today", value: "The Adaptive Chameleon" },
    { label: "Someone analytical who can help me think through complex ideas", value: "The Analytical Architect" },
    { label: "Someone direct who’ll challenge my thinking (in a good way)", value: "The Bold Provocateur" },
    { label: "Someone curious and energetic who helps me explore new possibilities", value: "The Curious Explorer" },
    { label: "Someone supportive who really listens and gets where I’m coming from", value: "The Empathetic Listener" },
    { label: "Someone practical who keeps things clear and grounded", value: "The Grounded Realist" },
    { label: "Someone wise and calm who helps me reflect and grow", value: "The Humble Sage" },
    { label: "Someone thoughtful who helps me see things differently, without pushing", value: "The Quiet Catalyst" },
    { label: "Someone hopeful and future-focused who helps me see what’s possible", value: "The Strategic Optimist" }
  ];
 
     
  const handleNext = () => {
    if (selectedPersonality) {
      userSelection.update(selection => {
        const updated = { ...selection, personality_type: selectedPersonality };
        console.log('Updated userSelection (personality):', updated);
        return updated;
      });
    goto('/match/gender');
    } 
  };

  
  const handleBack = () => {
    goto('/match/guidance');
  };
  </script>
  
  <MenuWrapper>
    <div class="match-container">
      <h2 class="match-heading">
        What kind of personality<br />
        would you like to talk to?
      </h2>
  
      <select class="match-select" bind:value={selectedPersonality}>
        <option value="" disabled>Select a personality type</option>
        {#each personalityOptions as option}
          <option value={option.value}>{option.label}</option>
        {/each}
      </select>
  
      <div class="match-nav">
        <button class="match-nav-btn" on:click={handleBack}>&lt; Back</button>
        <button class="match-nav-btn" on:click={handleNext}>Next &gt;</button>
      </div>
    </div>
  </MenuWrapper>
  