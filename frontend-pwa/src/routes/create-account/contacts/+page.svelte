<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  
    const contacts = [
      { name: 'Ellis Reed', image: '/Ellis Reed.png' },
      { name: 'Julian Park', image: '/Julian Park.png' },
      { name: 'Drew Taylor', image: '/Drew Taylor.png' },
      { name: 'Emery Jules', image: '/Emery Jules.png' },
      { name: 'Avery Sky', image: '/Avery Sky.png' }
    ];
  </script>
  
  <MenuWrapper>
    <div class="contact-container">
      <h1 class="contact-title">My Thought Partner<br />Contacts</h1>
  
      <div class="contact-box">
        <ul>
          {#each contacts as contact}
            <li class="contact-item">
              <img src={contact.image} alt={contact.name} class="contact-avatar" />
              <span class="contact-name">{contact.name}</span>
            </li>
          {/each}
        </ul>
      </div>
  
      <button class="contact-button">
        Find New Partner
      </button>
    </div>
  </MenuWrapper>
  