import streamlit as st

class AdventureGame:
    def __init__(self):
        # Initialize the game
        self.initialize_game()

    def initialize_game(self):
        """
        Initializes or resets the game to its starting state.
        """
        if "current_scene" not in st.session_state:
            st.session_state.current_scene = self.start_game

    def start_game(self):
        self.update_scene(
            text="Welcome to the Adventure Game! You find yourself in a dark forest. "
                 "There are two paths ahead:\n\n1. Take the left path.\n2. Take the right path.",
            choice1_text="Take the left path",
            choice1_action=self.left_path,
            choice2_text="Take the right path",
            choice2_action=self.right_path,
        )

    def left_path(self):
        self.update_scene(
            text="You take the left path and encounter a river. What do you do?\n\n"
                 "1. Try to swim across.\n2. Look for a bridge.",
            choice1_text="Swim across",
            choice1_action=self.swim_river,
            choice2_text="Look for a bridge",
            choice2_action=self.bridge_scene,
        )

    def swim_river(self):
        self.update_scene(
            text="The river is too strong, and you get swept away. Game Over!",
            choice1_text="Restart",
            choice1_action=self.start_game,
            choice2_text="Quit",
            choice2_action=self.quit_game,
        )

    def bridge_scene(self):
        self.update_scene(
            text="You find a bridge and cross the river safely. On the other side, you see a treasure chest. "
                 "What do you do?\n\n1. Open the chest.\n2. Ignore the chest.",
            choice1_text="Open the chest",
            choice1_action=self.open_chest,
            choice2_text="Ignore the chest",
            choice2_action=self.ignore_chest,
        )

    def open_chest(self):
        self.update_scene(
            text="Congratulations! You found the treasure and won the game!",
            choice1_text="Restart",
            choice1_action=self.start_game,
            choice2_text="Quit",
            choice2_action=self.quit_game,
        )

    def ignore_chest(self):
        self.update_scene(
            text="You walk away and miss the treasure. Game Over!",
            choice1_text="Restart",
            choice1_action=self.start_game,
            choice2_text="Quit",
            choice2_action=self.quit_game,
        )

    def right_path(self):
        self.update_scene(
            text="You take the right path and see a mysterious cave. What do you do?\n\n"
                 "1. Enter the cave.\n2. Walk past the cave.",
            choice1_text="Enter the cave",
            choice1_action=self.cave_scene,
            choice2_text="Walk past the cave",
            choice2_action=self.fall_trap,
        )

    def cave_scene(self):
        self.update_scene(
            text="Inside the cave, you find a sleeping dragon. What do you do?\n\n"
                 "1. Try to sneak past the dragon.\n2. Attack the dragon.",
            choice1_text="Sneak past",
            choice1_action=self.sneak_dragon,
            choice2_text="Attack",
            choice2_action=self.attack_dragon,
        )

    def sneak_dragon(self):
        self.update_scene(
            text="You sneak past the dragon and find a secret exit. You win!",
            choice1_text="Restart",
            choice1_action=self.start_game,
            choice2_text="Quit",
            choice2_action=self.quit_game,
        )

    def attack_dragon(self):
        self.update_scene(
            text="The dragon wakes up and burns you to ashes. Game Over!",
            choice1_text="Restart",
            choice1_action=self.start_game,
            choice2_text="Quit",
            choice2_action=self.quit_game,
        )

    def fall_trap(self):
        self.update_scene(
            text="You walk past the cave and fall into a trap. Game Over!",
            choice1_text="Restart",
            choice1_action=self.start_game,
            choice2_text="Quit",
            choice2_action=self.quit_game,
        )

    def quit_game(self):
        st.warning("Game Over! Thanks for playing.")
        st.stop()

    def update_scene(self, text, choice1_text, choice1_action, choice2_text, choice2_action):
        # Update the current scene in session state
        st.session_state.current_scene = lambda: self.display_scene(
            text, choice1_text, choice1_action, choice2_text, choice2_action
        )
        # Render the scene
        st.session_state.current_scene()

    def display_scene(self, text, choice1_text, choice1_action, choice2_text, choice2_action):
        st.write(f"### {text}")
        if st.button(choice1_text):
            st.session_state.current_scene = choice1_action
            st.session_state.current_scene()
        if st.button(choice2_text):
            st.session_state.current_scene = choice2_action
            st.session_state.current_scene()


# Run the game
if __name__ == "__main__":
    st.set_page_config(page_title="Adventure Game", layout="centered")
    game = AdventureGame()
    game.initialize_game()
    st.session_state.current_scene()
