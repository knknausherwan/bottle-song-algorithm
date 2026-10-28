# Bottle Song Sequence Algorithm

An algorithmic implementation in Python designed to generate a deterministic, linear decrement sequence—classically known as the "99 Bottles of Beer" song. 

This project demonstrates modular procedural design, separating the system into a **state-rendering function** and a **state-transition driver loop**, executing with linear time complexity.

## 📐 Algorithmic Architecture

The implementation relies on two core components:

1. **State-Rendering Function (`bottle_song`)**: 
   * Acts as a template function that maps an integer state ($n$) to a formatted string output.
   * Performs an immediate mathematical decrement ($n - 1$) to compute the subsequent state within the current frame.

2. **State-Transition Driver (`bottle_verse`)**: 
   * Utilizes a discrete step-down iterator (`range(number, 0, -1)`) to govern the lifecycle of the sequence.
   * Iteratively invokes the renderer until the termination condition ($n = 0$) is satisfied.
