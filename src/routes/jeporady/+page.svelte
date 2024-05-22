<script lang="ts">
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';
  import { Round } from '../../store';
  import { get } from 'svelte/store';

  let myarr: string[] = [];
  let header: string[] = [];
  let round: string;
  let playerScores: { name: string; score: number ; url: string}[] = [];
  let totalRounds: number;
  let numRows: number; // Number of rows
  let numCols : number; // Number of columns
  function nextRound() {
    if (parseInt(get(Round)) === totalRounds) {
      const response = confirm("This is the last round. Are you sure you want to end the game?");
      if (response) {
        if (typeof window !== 'undefined') {
        goto('/lastpage')
        }
    } 
      else {
        return;
}

      return;
    }
    Round.set((parseInt(round) + 1).toString());
    if (typeof window !== 'undefined') {
    goto('/placeholder');
    }
    console.log(get(Round))
  }
  function prevRound() {
    if (parseInt(get(Round)) === 1 ) {
      alert("This is the first round!")
      return;
    }
    Round.set((parseInt(round) - 1).toString());
    if (typeof window !== 'undefined') {
    goto('/placeholder');
    }
  }

  async function navigateToQuestion(question: string, value: string) {
    if (question === "-") {
      return;
    }
    const url = `/question?question=${encodeURIComponent(question)}&value=${value}`;
    if (typeof window !== 'undefined') {
    await goto(url);
    }
  }

  onMount(async () => {
    let url = window.location.href;
    const searchParams = new URLSearchParams(new URL(url).search);
    
    Round.subscribe(value => {
      round = value;
    });
    try {
      const response = await fetch(`http://localhost:5000/?round=${round}`);
      const data = await response.json();
      myarr = data.questions;
      header = data.headers;
      numCols = header.length;
      console.log(numCols)
      const response1 = await fetch('http://localhost:5000/players');
      playerScores = await response1.json();
      const response2 = await fetch('http://localhost:5000/rounds');
      const data1 = await response2.json();
      totalRounds = data1.rounds;
      console.log(playerScores)

      // Calculate the number of rows dynamically based on the number of questions
      numRows = Math.ceil(myarr.length / numCols);
      
    } catch (error) {
      console.error("Error fetching data:", error);
      alert("Something went wrong. please restart everyting")
    }
  });
</script>

<style>
  @import './+page.css';
</style>

<div class="nextroundContainer">
  <button class="button-10" on:click={prevRound}>Go To Previous Round</button>
  <button class="button-10" id="finale" on:click={nextRound}>Go To Next Round</button>
</div>

<table id="game" cellspacing="5" cellpadding="0">
  <thead>
    <tr>
      {#each header as col}
        <th>{col}</th>
      {/each}
    </tr>
  </thead>
  <tbody>
    {#each Array.from({ length: numRows }) as _, row}
      <tr>
        {#each Array.from({ length: numCols }) as _, i}
          {#if myarr[row * numCols + i] === "-"}
            <td class="cell clean"></td>
          {:else}
            <td id="tq{row}{i}" class="cell clean" on:click={() => navigateToQuestion(myarr[row * numCols + i], `${(row + 1) * 100}`)}>
              <h3>{((row + 1) * 100)}</h3>
            </td>
          {/if}
        {/each}
      </tr>
    {/each}
  </tbody>
  <tfoot>
    <tr>
      <td colspan="{numCols}" class="footer-cell">
        <h4>Player Scores</h4>
        <div class="player-scores-container">
          {#each playerScores as player}
            <div class="player-score">
              <span><img src={player.url} alt="pfp" height="64px" width="64px" /></span>
              <span>{player.name}</span>
              <span>{player.score}</span>
            </div>
          {/each}
        </div>
      </td>
    </tr>
  </tfoot>
</table>
