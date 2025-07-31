const API_URL = "http://127.0.0.1:8000"; // adapte si besoin

export async function startGame() {
  const res = await fetch(`${API_URL}/start-game`, {
    method: "POST",
  });
  if (!res.ok) throw new Error("Erreur démarrage partie");
  return await res.json();
}

export async function playTurn(gameId, playerChoiceIndex) {
  const res = await fetch(`${API_URL}/play-turn`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ game_id: gameId, player_choice_index: playerChoiceIndex }),
  });
  if (!res.ok) throw new Error("Erreur lors du tour");
  return await res.json();
}
