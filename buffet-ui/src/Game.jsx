import React, { useState } from "react";
import { startGame, playTurn } from "./api";

export default function Game() {
  const [gameId, setGameId] = useState(null);
  const [availableCards, setAvailableCards] = useState([]);
  const [playerScore, setPlayerScore] = useState(0);
  const [iaScore, setIaScore] = useState(0);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleStart = async () => {
    setError("");
    try {
      const res = await startGame();
      setGameId(res.game_id);
      setAvailableCards(res.available_cards);
      setPlayerScore(res.player_score);
      setIaScore(res.ia_score);
      setMessage("");
    } catch (err) {
      setError(err.message);
    }
  };

  const handlePlay = async (index) => {
    setError("");
    try {
      const res = await playTurn(gameId, index);
      setAvailableCards(res.available_cards || []); // peut être vide si fin du deck
      setPlayerScore(res.player_score);
      setIaScore(res.ia_score);
      setMessage(res.message || "");
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>🎮 Panique au Buffet</h1>

      {!gameId && (
        <button onClick={handleStart} style={{ padding: "10px 20px", fontSize: 16 }}>
          Démarrer une partie
        </button>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {gameId && (
        <>
          <div style={{ marginBottom: 10 }}>
            <strong>Score Joueur :</strong> {playerScore} |{" "}
            <strong>Score IA :</strong> {iaScore}
          </div>

          <h2>Choisis une carte :</h2>
          <div style={{ display: "flex", gap: 10 }}>
            {availableCards.map((card, index) => (
              <button
                key={index}
                onClick={() => handlePlay(index)}
                style={{
                  padding: 10,
                  width: 180,
                  border: "1px solid #ccc",
                  borderRadius: 6,
                  cursor: "pointer",
                  background: "#f9f9f9",
                }}
              >
                <div><strong>{card.name}</strong></div>
                <div>Valeur : {card.value}</div>
                {card.effect && <div>Effet : {card.effect}</div>}
              </button>
            ))}
          </div>

          {message && <p style={{ marginTop: 20 }}>{message}</p>}

          <button
            onClick={handleStart}
            style={{ marginTop: 20, padding: "6px 16px", fontSize: 14 }}
          >
            🔄 Rejouer
          </button>
        </>
      )}
    </div>
  );
}
