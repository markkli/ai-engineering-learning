let score = JSON.parse(localStorage.getItem('score')) || {
        wins: 0,
        losses: 0,
        ties: 0
      };

      updateScoreDisplay();

      function playGame(playerMove) {
        const computerMove = pickComputerMove();

        let result = '';

        if (playerMove === 'Rock') {
          if (computerMove === 'Rock') {
            result = 'It\'s a tie!';
          } else if (computerMove === 'Paper') {
            result = 'You lose!';
          } else {
            result = 'You win!';
          }

        } else if (playerMove === 'Paper') {
          if (computerMove === 'Rock') {
            result = 'You win!';
          } else if (computerMove === 'Paper') {
            result = 'It\'s a tie!';
          } else {
            result = 'You lose!';
          }
          
        } else {
          if (computerMove === 'Scissors') {
            result = 'You lose!';
          } else if (computerMove === 'Paper') {
            result = 'You win!';
          } else {
          result = 'It\'s a tie!';
          }
        }

        if (result === 'You win!') {
          score.wins ++;
        } else if (result === 'You lose!') {
          score.losses ++;
        } else {
          score.ties ++;
        }

        localStorage.setItem('score', JSON.stringify(score));

        updateScoreDisplay();
        
				document.querySelector('.js-moves')
					.innerHTML = `You <img src="images/${playerMove}-emoji.png" class="move-icon"><img src="images/${computerMove}-emoji.png" class="move-icon"> Computer`;

				document.querySelector('.js-result')
					.innerHTML = `${result}`;
			}

      function updateScoreDisplay() {
        document.querySelector('.js-score')
          .innerHTML = `Wins: ${score.wins}, Losses: ${score.losses}, Ties: ${score.ties}`;
      }

      function pickComputerMove() {
        const randomNumber = Math.random();

        let computerMove = '';
        if (randomNumber < 1/3 && randomNumber > 0) {
          computerMove = 'Rock';
        } else if (randomNumber < 2/3 && randomNumber >= 1/3) {
          computerMove = 'Paper';
        } else {
          computerMove = 'Scissors';
        }

        return computerMove;
      }