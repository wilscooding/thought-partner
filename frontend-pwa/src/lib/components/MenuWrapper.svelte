<script>
    export let logo = "/logo.png";
    let menuOpen = false;
  
    const toggleMenu = () => {
      menuOpen = !menuOpen;
    };
  </script>
  
  <div class="home-container relative">
    <!-- Top Bar -->
    <div class="flex justify-between items-center w-full">
      <!-- Burger Icon -->
      <div class="relative">
        <button
          class="menu-icon"
          on:click={toggleMenu}
          aria-label="Toggle navigation menu"
        >
          <svg class="w-6 h-6" fill="none" stroke="#141420" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
  
        <!-- Dropdown Menu -->
        {#if menuOpen}
        <div class="dropdown-menu absolute top-10 left-0 bg-[#c6b06e] text-[#141420] w-56 py-6 px-4 rounded-xl shadow-lg z-50">
        <ul class="space-y-6">
            <li><a href="/profile">👤 <span class="side-link">My Profile</span></a></li>
            <li><a href="/contacts">📞 <span class="side-link">Contacts</span></a></li>
            <li><a href="/match">🤝 <span class="side-link">Match Me</span></a></li>
            <li><a href="/thought-partners">⚙️ <span class="side-link">Thought Partner Profiles</span></a></li>
            <li><a href="/security">🔒 <span class="side-link">Security & Privacy</span></a></li>
        </ul>
        </div>
        {/if}

      </div>
  
      <!-- Logo -->
      <img src={logo} alt="Logo" class="w-10 h-10" />
    </div>
  
    <!-- Main content -->
    <div class="pt-10">
      <slot />
    </div>
  </div>
  