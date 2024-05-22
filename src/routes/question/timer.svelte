<script lang="ts">
	let s = 0;
	let m = 0;
	let active = false;
	let timer: any;
	function setActive(a: boolean) {
		active = a;
		if(!active) {
			clearInterval(timer)
		} else {
				timer = setInterval(() => {
					if(s == 59) {
						s = 0;
						m += 1;
					} else {
						s += 1;	
					}
			  }, 500);
		}
	}
</script>

<button on:click={() => setActive(!active)}>
	{!active ? 'start' : 'stop'}
</button>
<span>{m.toString().padStart(2,0)}</span>:<span>{s.toString().padStart(2,0)}</span>