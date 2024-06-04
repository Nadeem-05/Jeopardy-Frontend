
<script>
    import {goto} from "$app/navigation";
    async function goToJeopardy() {
      if (typeof window !== 'undefined') {
        goto("/jeporady");
      }
    }
    async function goToJson() {
      if (typeof window !== 'undefined') {
        goto("/uploadjson");
      }
    }

</script>
<div class="div">
    <div class="div-2">
      <div class="div-3">
        <h1>Welcome to Jeopardy!</h1>
        <p>Click the button below to start the game</p>
        <small>Check the config before you start!</small>
        <button on:click={() => goToJeopardy()} class="button-10">
            Start</button>
        <button on:click={() => goToJson()} class="button-10">
              Upload Json</button>
       </div></div>
  </div>
  
  <style>
    /* CSS */
.div {
    border-color: rgba(0, 0, 0, 1);
    border-style: solid;
    border-width: 5px;
    background-color: #2a3698;
    color: #000;
    font-weight: 400;
    text-align: center;
    justify-content: center;
    align-items: center;
    padding: 5vh 5vw;
    margin : auto;  
    box-sizing: content-box;
    height: 85vh;
    width : 80vw; /* Ensure the div fills the entire viewport height */
    overflow: hidden; /* Hide overflow to prevent scrolling */
  }
  
  .div-2 {
    background-color: #d9d9d9;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 25vh;
    width: 80vw; /* Set width to match the parent div */
    margin: auto; /* Center horizontally */
    padding: 15vh 0;
    margin-top: 18vh; /* Adjust vertical margin */
    padding-top: 11px; /* Adjust vertical padding */
    background: rgba(255, 255, 255, .5);
    backdrop-filter: blur(3px);
    text-align: center;
    border-radius: 10px;
  }
  
  .div-3 {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    margin: 10vh 0;
    padding-top:10vh;
  }
  p{
    padding-bottom: 5px;
    margin-bottom: 5px;
  }
  small{
    padding-bottom: 5vh;
  }
  .button-10 {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 6px 14px;
  font-family: -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif;
  border-radius: 6px;
  border: none;

  color: #fff;
  background: linear-gradient(180deg, #4B91F7 0%, #367AF6 100%);
   background-origin: border-box;
  box-shadow: 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-10:focus {
  box-shadow: inset 0px 0.8px 0px -0.25px rgba(255, 255, 255, 0.2), 0px 0.5px 1.5px rgba(54, 122, 246, 0.25), 0px 0px 0px 3.5px rgba(58, 108, 217, 0.5);
  outline: 0;
}
.div{
    background-image: url('https://m.media-amazon.com/images/G/01/DeveloperBlogs/AmazonDeveloperBlogs/Alexa/jeopardy._CB523168147_.jpg?t=true') !important;
    background-size:cover;
    background-repeat: no-repeat;
    background-position: top;}
    </style>