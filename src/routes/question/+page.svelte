<script lang="ts">
  import { get } from "svelte/store";
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";
  import { Modal, Content, Trigger } from "sv-popup";
  import { Round } from "../../store";

  let time = 60; // initial time in seconds
  let interval: number;
  let incrementPlayer: number[] = [];
  let decrementPlayer: number[] = [];

  function startTimer() {
    interval = setInterval(() => {
      if (time > 0) {
        time--;
      } else {
        clearInterval(interval);
        alert("Time's up!");
      }
    }, 1000);
  }

  function resetTimer() {
    clearInterval(interval);
    time = 60;
  }

  function incrementPlayerScore(playerId: number) {
    if (incrementPlayer.includes(playerId)) {
      incrementPlayer = incrementPlayer.filter((id) => id !== playerId);
    } else if (decrementPlayer.includes(playerId)) {
      decrementPlayer = decrementPlayer.filter((id) => id !== playerId);
      incrementPlayer = [...incrementPlayer, playerId];
    } else {
      incrementPlayer = [...incrementPlayer, playerId];
    }
    console.log(incrementPlayer);
  }

  function decrementPlayerScore(playerId: number) {
    if (decrementPlayer.includes(playerId)) {
      decrementPlayer = decrementPlayer.filter((id) => id !== playerId);
    } else if (incrementPlayer.includes(playerId)) {
      incrementPlayer = incrementPlayer.filter((id) => id !== playerId);
      decrementPlayer = [...decrementPlayer, playerId];
    } else {
      decrementPlayer = [...decrementPlayer, playerId];
    }
    console.log(decrementPlayer);
  }

  let url: string;
  let value: string = "a";
  let question: string = "a";
  let answer: string = "a";
  let score: string = "a";
  let round: string = get(Round);
  let playerScores: { id: number; name: string; score: number, url: string }[] = [];
  let fontSize: number = 3;
  function goToBoard() {
    goto("/jeporady");
  }
  async function finishQuestion() {
    const response = await fetch(
      "http://localhost:5000/questionDone?question=" +
        value +
        "&round=" +
        round,
    );
    const response1 = await fetch('http://localhost:5000/updateScore', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json; charset=utf-8'
  },
  body: JSON.stringify({
    incrementPlayer,
    decrementPlayer,
    score: parseInt(score),
  })
})

    const data: { done: boolean } = await response.json();
    if (data.done == true) {
      goto("/jeporady");
    } else {
      alert("Something went wrong!");
    }
  }
  onMount(async () => {
    // Create a URLSearchParams object from the query parameters
    url = window.location.href;
    const searchParams = new URLSearchParams(new URL(url).search);

    if (searchParams.has("question")) {
      console.log("yes");

      // @ts-ignore: Object is possibly 'null'.
      value = searchParams.get("question").slice(4) || "a";
      score = searchParams.get("value") || "a";
      round = get(Round);
      const response = await fetch(
        "http://localhost:5000/question?question=" + value + "&round=" + round,
      );
      const data = await response.json();
      question = data.question;
      answer = data.answer;
      console.log(answer);
      const response1 = await fetch("http://localhost:5000/players");
      playerScores = await response1.json();
      const questionLength = question.length;
      if (questionLength > 20) {
        fontSize = 2.5;
      } else if (questionLength > 10) {
        fontSize = 3;
      }
    }
  });
</script>

<div class="div">
  <div class="div-2">
    <div class="div-3">
      <div class="div-5">{score} - Category</div>
      <div class="div-4" style="font-size: {fontSize}vw">{question}</div>
      <div class="timer">
        {time}
      </div>
      <div id="buttons">
        <button color="blue" class="button-10" id="left" on:click={goToBoard}
          >Go Back to Board</button
        >
        <button color="blue" class="button-10" id="right" on:click={startTimer}
          >Start Timer</button
        >
        <button color="blue" class="button-10" id="right" on:click={resetTimer}
          >Reset Timer</button
        >

        <Modal basic>
          <Content class="div">
            <h2>{answer}</h2>
          </Content>
          <Trigger>
            <button class="button-10">Show answer</button>
          </Trigger>
        </Modal>
        <button
          color="blue"
          class="button-10"
          id="right"
          on:click={finishQuestion}>Finish Question</button
        >
      </div>
    </div>
  </div>
  <table>
    <tfoot>
      <tr>
        <h4>Player Scores</h4>

        <div class="player-scores-container">
          {#each playerScores as player}
            <div class="player-score">
              <div>
                <span
                  ><img
                    src={player.url}
                    alt="pfp"
                    height="64px"
                    width="64px"
                  /></span
                >
              </div>
              <span>{player.name}</span>
              <span>{player.score}</span>
              <div class="playerscore-buttons">
                <button
                  class="button-10 {incrementPlayer.includes(player.id)
                    ? 'selected'
                    : ''}"
                  on:click={() => incrementPlayerScore(player.id)}
                  ><i class="arrow up"></i></button
                >
                <button
                  class="button-10 {decrementPlayer.includes(player.id)
                    ? 'selected'
                    : ''}"
                  on:click={() => decrementPlayerScore(player.id)}
                  ><i class="arrow down"></i></button
                >
              </div>
            </div>
          {/each}
        </div>
      </tr>
    </tfoot>
  </table>
</div>

<style>
  @import "./+page.css";
</style>
