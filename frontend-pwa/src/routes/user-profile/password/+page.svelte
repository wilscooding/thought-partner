<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  
    let currentPassword = '';
    let newPassword = '';
    let confirmPassword = '';
  
    const updatePassword = () => {
      console.log('Password updated:', { currentPassword, newPassword, confirmPassword });
      // Add API call to update password here
    };
  </script>
  
  <MenuWrapper dark>
    <div class="password-container">
      <h2 class="password-title">Update Password</h2>
  
      <div class="password-field">
        <label>Enter Current Password</label>
        <input type="password" bind:value={currentPassword} />
      </div>
  
      <div class="password-field">
        <label>Enter New Password</label>
        <input type="password" bind:value={newPassword} />
      </div>
  
      <div class="password-field">
        <label>Re-enter New Password</label>
        <input type="password" bind:value={confirmPassword} />
      </div>
  
      <button class="update-btn" on:click={updatePassword}>Update</button>
  
      <div class="terms-link">
        <a href="/terms">Terms and Conditions</a>
      </div>
    </div>
  </MenuWrapper>
  