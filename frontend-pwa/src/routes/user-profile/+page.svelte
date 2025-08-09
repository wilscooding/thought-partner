<script>
    import MenuWrapper from '$lib/components/MenuWrapper.svelte';
  
    let userProfile = {
      firstName: '',
      lastName: '',
      ageRange: '',
      gender: '',
      professionalIdentity: '',
      yearsOfExperience: '',
      strength: '',
      challenge: ''
    };
  
    const updateProfile = () => {
      console.log('Profile updated:', userProfile);
      // Add backend API call later here
    };
  </script>
  
  <MenuWrapper dark>
    <div class="profile-container">
      <div class="profile-field">
        <label>First Name</label>
        <div class="input-wrapper">
          <input type="text" bind:value={userProfile.firstName} />
          <span class="pencil-icon">✏️</span>
        </div>
      </div>
  
      <div class="profile-field">
        <label>Last Name</label>
        <div class="input-wrapper">
          <input type="text" bind:value={userProfile.lastName} />
          <span class="pencil-icon">✏️</span>
        </div>
      </div>
  
      <div class="profile-field">
        <label>What age range are you in? Optional.</label>
        <select class= 'user-select' bind:value={userProfile.ageRange}>
          <option disabled>Select an option</option>
          <option>18-24</option>
          <option>25-34</option>
          <option>35-44</option>
          <option>45-54</option>
          <option>55-64</option>
          <option>65+</option>
        </select>
      </div>
  
      <div class="profile-field">
        <label>What’s your gender? Optional.</label>
        <select class= 'user-select'  bind:value={userProfile.gender}>
          <option disabled>Select an option</option>
          <option>Woman</option>
          <option>Man</option>
          <option>Non-Binary</option>
          <option>Prefer not to say</option>
        </select>
      </div>
  
      <div class="profile-field">
        <label>What’s your professional identity?</label>
        <select class= 'user-select' bind:value={userProfile.professionalIdentity}>
          <option disabled>Select an option</option>
          <option>Career Changer/Explorer</option>
          <option>Entrepreneur/Founder</option>
          <option>Independent Consultant/Coach</option>
          <option>Individual Contributor</option>
          <option>Nonprofit or Mission-Driven Professional</option>
          <option>People Manager/Team Lead</option>
          <option>Senior Leader/Executive</option>
          <option>Side Hustler/Aspiring Founder</option>
          <option>Student/Early Career Professional</option>
        </select>
      </div>
  
      <div class="profile-field">
        <label>Roughly how many years of experience do you have?</label>
        <select class='user-select' bind:value={userProfile.yearsOfExperience}>
          <option disabled>Select an option</option>
          <option>Less than 1 year</option>
          <option>1-3 years</option>
          <option>4-7 years</option>
          <option>8-15 years</option>
          <option>15+ years</option>
        </select>
      </div>
  
      <div class="profile-field">
        <label>What’s a strength that comes naturally to you at work?</label>
        <select class='user-select' bind:value={userProfile.strength}>
          <option disabled>Select an option</option>
          <option>Building relationships</option>
          <option>Coaching or mentoring</option>
          <option>Creativity & innovation</option>
          <option>Organizing chaos</option>
          <option>Vision & big-picture thinking</option>
        </select>
      </div>
  
      <div class="profile-field">
        <label>What’s a challenge you face in your work or business?</label>
        <select class='user-select' bind:value={userProfile.challenge}>
          <option disabled>Select an option</option>
          <option>Balancing everything</option>
          <option>Communicating or influencing</option>
          <option>Managing stress</option>
          <option>Making decisions</option>
          <option>Solving tough problems</option>
        </select>
      </div>
  
      <button class="update-btn" on:click={updateProfile}>Update</button>
    </div>
  </MenuWrapper>
  