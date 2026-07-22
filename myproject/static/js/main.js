// main JS file 
// console.log("Hello World!");

function cClick(c) {
    const modal = document.getElementById('clue-modal');
        
    // Disable the button so players can't click it again
    // this.classList.add('used');
    // this.disabled = true;

    // Fetch the clue data from Django  AJAX
    fetch(`/clue/${c}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('modal-value').innerText = `$${data.value}`;
            document.getElementById('modal-text').innerText = data.text;
            document.getElementById('modal-answer').innerText = "";
            clue_value = data.value; 
            clue_answer = data.answer;
            clue_key = c;
            modal.style.display = 'block'; // Show the modal
        });
}

function getNames() {
    console.log("*** In getNames()")
    fetch('/names/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('player1_name').innerText = data.player1_name;
            document.getElementById('player2_name').innerText = data.player2_name;
            document.getElementById('player3_name').innerText = data.player3_name;
        });
}
function closeModal() {
    document.getElementById('clue-modal').style.display = 'none';
    document.getElementById(clue_key).innerText = "";
}

function showAnswer() {  // program stub
    document.getElementById('modal-answer').innerText = clue_answer;
}

function showScreen(screenId) {
    const screens = document.querySelectorAll('.screen');
    screens.forEach(screen => screen.classList.remove('active'));
        
    const targetScreen = document.getElementById(screenId);
    if (targetScreen) {
        targetScreen.classList.add('active');
    }
 }
