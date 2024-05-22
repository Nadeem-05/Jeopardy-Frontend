<script lang="ts">
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';
  
    let playerScores: { name: string; score: number, url: string }[] = [];
  
    onMount(async () => {
      try {
        const response1 = await fetch('http://localhost:5000/players');
        playerScores = await response1.json();
        playerScores = playerScores.sort((a, b) => b.score - a.score);
  
      } catch (error) {
        console.error("Error fetching player scores:", error);
      }
    });
  
    function goToHome() {
      goto("/");
    }
  </script>
  
  <div class="div">
    <div class="div-2">
      <div class="div-3">
        <h1>Jeopardy Standings</h1>
        <p>Here are the final scores:</p>
        <table class="standings-table">
          <thead>
            <tr>
              <th>Player</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {#each playerScores.slice(0, 3) as player}
              <tr>
                <td>
                  <div class="player-info">
                    <img src={player.url} alt="pfp" />
                    <small>{player.name}</small>
                  </div>
                </td>
                <td>{player.score}</td>
              </tr>
            {/each}
          </tbody>
        </table>
        <button on:click={goToHome} class="button-10">
          Main Menu
        </button>
      </div>
    </div>
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
      margin: auto;  
      box-sizing: content-box;
      height: 85vh;
      width: 80vw; 
      overflow: hidden;
    }
  
    .div-2 {
      background-color: #d9d9d9;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 50vh;
      width: 80vw;
      margin: auto;
      padding: 20vh 0;
      margin-top: 10vh;
      margin-bottom: 10vh;
      padding-top : 1vh;
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
      padding-top: 10vh;
      margin-top : 5vh;
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
  
    .standings-table {
      width: 100%;
      border-collapse: collapse;
      align-items: center;
      justify-content: center;
      margin: 20px 0;
      font-size: 1.2em;
      text-align: left;
      background-color: rgba(255, 255, 255, 0.4);
      color: #000;
      color: #fff;
    }
  
    .standings-table th,
    .standings-table td {
      padding: 12px 15px;
      color: #000;
      border: 1px solid #ddd;
    }
  
    .standings-table th {
      background-color: #4B91F7;
      color: #fff;
    }
  
    .standings-table tr:nth-child(even) {
      background-color: rgba(255, 255, 255, 0.1);
    }
  
    .div {
      background-image: url('https://m.media-amazon.com/images/G/01/DeveloperBlogs/AmazonDeveloperBlogs/Alexa/jeopardy._CB523168147_.jpg?t=true') !important;
      background-size: cover;
      background-repeat: no-repeat;
      background-position: top;
    }
  
    .player-info {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  
    .player-info img {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      margin-bottom: 5px;
    }
  </style>
  