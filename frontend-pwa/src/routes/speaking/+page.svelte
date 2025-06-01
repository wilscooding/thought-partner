<script>
    const tp = {
      name: 'Julian Park',
      image: '/Julian Park.png' // or adjust the path based on your static folder
    };
  </script>
  
  <div class="call-container">
    <!-- Top Name Text -->
    <h1 class="call-heading">Speaking To<br />{tp.name}</h1>
  
    <!-- Avatar & Logo -->
    <div class="avatar-wrapper">
      <img src={tp.image} alt={tp.name} class="avatar-img" />
    </div>
    <div>
      <img src="/logo.png" alt="Logo" class="avatar-logo" />
      
    </div>
  
    <!-- End Call Button -->
    <button class="call-end-btn">End Call</button>
  </div>
  