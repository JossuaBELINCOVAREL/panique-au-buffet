import { useEffect, useState } from "react";
import { startGame, playTurn } from "./api";
import "./App.css";

function App() {
  const [gameId, setGameId] = useState(null);
  const [availableCards, setAvailableCards] = useState([]);
  const [playerScore, setPlayerScore] = useState(0);
  const [iaScore, setIaScore] = useState(0);
  const [message, setMessage] = useState("");

  useEffect(() => {
    handleStartGame();
  }, []);

  async function handleStartGame() {
    const data = await startGame();
    setGameId(data.game_id);
    setAvailableCards(data.available_cards);
    setPlayerScore(data.player_score);
    setIaScore(data.ia_score);
    setMessage("");
  }

  async function handleCardClick(index) {
    const result = await playTurn(gameId, index);
    setPlayerScore(result.player_score);
    setIaScore(result.ia_score);
    setAvailableCards(result.available_cards);
    setMessage(result.message);
  }

  return (
    <div className="container">
      <h1>Panique au Buffet 🎉</h1>

      <div className="scores">
        <p>👤 Joueur : {playerScore} pts</p>
        <p>🤖 IA : {iaScore} pts</p>
      </div>

      <div className="cards">
        {availableCards.map((card, index) => (
          <div key={index} className="card" onClick={() => handleCardClick(index)}>
            {/* Remplace "img" par une vraie image plus tard */}
            <img src={`/images/${card.image}`} alt={card.name} onError={(e) => e.target.style.display = 'none'} />
            <h3>{card.name}</h3>
            <p>Valeur : {card.value}</p>
            {card.effect && <p>Effet : {card.effect}</p>}
          </div>
        ))}
      </div>

      {message && <p style={{ textAlign: "center" }}>{message}</p>}

      <div style={{ textAlign: "center", marginTop: "20px" }}>
        <button onClick={handleStartGame}>🔄 Nouvelle Partie</button>
      </div>
    </div>
  );
}

export default App;
