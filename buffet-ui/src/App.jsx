import { useState } from "react";
import { startGame, playTurn } from "./api";
import "./App.css";

function App() {
  const [gameId, setGameId] = useState(null);
  const [cards, setCards] = useState([]);
  const [playerScore, setPlayerScore] = useState(0);
  const [aiScore, setAiScore] = useState(0);
  const [message, setMessage] = useState("");
  const [isPlaying, setIsPlaying] = useState(false);

  const handleStartGame = async () => {
    const data = await startGame();
    setGameId(data.game_id);
    setCards(data.available_cards);
    setPlayerScore(data.player_score);
    setAiScore(data.ia_score);
    setMessage("");
    setIsPlaying(true);
  };

  const handleCardClick = async (index) => {
    const data = await playTurn(gameId, index);
    setMessage(data.message);
    setPlayerScore(data.player_score);
    setAiScore(data.ia_score);
    setCards(data.remaining_deck_size > 0 ? await startGame().then(d => d.available_cards) : []);
    if (data.remaining_deck_size <= 0) setIsPlaying(false);
  };

  return (
    <div className="container">
      <h1>🎉 Panique au Buffet 🎉</h1>

      <div className="score-board">
        <div>👤 Joueur : {playerScore}</div>
        <div>🤖 IA : {aiScore}</div>
      </div>

      {!isPlaying ? (
        <button onClick={handleStartGame}>Démarrer une partie</button>
      ) : (
        <>
          <h2>Choisis ta carte :</h2>
          <div className="card-container">
            {cards.map((card, index) => (
              <div key={index} className="card" onClick={() => handleCardClick(index)}>
                <h3>{card.name}</h3>
                <p>Valeur : {card.value}</p>
                {card.effect && <p>Effet : {card.effect}</p>}
              </div>
            ))}
          </div>
        </>
      )}

      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default App;
