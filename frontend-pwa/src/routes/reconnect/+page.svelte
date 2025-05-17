<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  
    const tp = {
      name: 'Julian Park',
      image: '/Julian Park.png',
      bio: `Sharp, methodical, and forward-thinking, Julian Park helps you bring structure to complexity. 
        With a calm and incisive approach, he turns uncertainty into clear, actionable paths.`,
      focusArea: 'Operations',
      industry: 'Construction Industry'
    };
  </script>
  
  <MenuWrapper>
    <div class="reconnect-container">
      <!-- Avatar & Name -->
      <div class="flex items-center justify-center gap-14 mt-4">
        <img src={tp.image} alt={tp.name} class="w-20 h-20 rounded-full object-cover object-top" />
        <h2 class="text-lg font-bold text-[#141420]">{tp.name}</h2>
      </div>
  
      <!-- Bio -->
      <p class="text-sm mt-4 max-w-xs text-center text-[#3a3b4b]">{tp.bio}</p>
  
      <!-- Divider -->
      <hr class="w-full max-w-xs border-t-2 border-[#3a3b4b] my-6" />  
      <!-- Last focus -->
      <p class="text-sm max-w-xs text-center text-[#3a3b4b]">
        The last time you spoke with this thought partner you chose to focus on
        <span class="font-semibold">{tp.focusArea}</span> in the
        <span class="font-semibold">{tp.industry}</span>.
      </p>
  
      <p class="text-sm mt-2 text-center text-[#3a3b4b]">
        Before we connect you do you want to change either of these?
      </p>
  
      <!-- Buttons -->
      <div class="mt-6 flex flex-col gap-4 w-full max-w-xs">
        <button class="reconnect-btn">No, connect me.</button>
        <button class="reconnect-btn">Yes, I want to change.</button>
      </div>
    </div>
  </MenuWrapper>
  