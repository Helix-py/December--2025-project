---

# **Chess Engine (Python \+ NumPy)**

## **Overview**

This project is a terminal-based chess engine written in Python using **NumPy** to represent and manipulate the game board. It implements core chess mechanics including legal move validation, turn-based play, check detection, and checkmate detection.

The engine focuses on **rules and logic**, not graphics or AI. Moves are entered using standard chess notation (e.g. `p e2 e4`) and translated into array coordinates internally.

---

## **Why I Built This**

I built this project primarily to:

* Learn **NumPy fundamentals** in a real, non-trivial context  
* Practice **object-oriented design** with interacting classes  
* Understand how complex rule systems (like chess) can be broken into verifiable logic  
* Improve confidence writing larger, stateful programs without tutorials guiding every step

Chess was chosen because it forces precision: one incorrect rule breaks the whole system.

---

## **What the Project Does**

* Represents an 8×8 chess board using a NumPy array  
* Defines a base piece class and specialized classes for:  
  * Pawn  
  * Rook  
  * Knight  
  * Bishop  
  * Queen  
  * King  
* Validates:  
  * Board bounds  
  * Piece ownership and color  
  * Legal movement patterns  
  * Path obstruction  
  * Self-check prevention  
* Detects:  
  * Check  
  * Checkmate  
* Alternates turns between white and black  
* Prints the board state after every move

This is a **fully playable rules-based chess game** in the terminal.

---

## **What I Learned**

Through this project, I learned:

* How to use **NumPy arrays** for structured state instead of nested Python lists  
* How to translate between **human-friendly input** and internal representations  
* Why separating **movement logic**, **legality checks**, and **state mutation** matters  
* How to simulate actions (make / undo moves) to test conditions like check  
* How quickly complexity grows when systems interact—and how structure reduces bugs

I also learned that writing something “simple” like chess forces you to think carefully about **edge cases, validation order, and system consistency**.

---

## **Time & Development**

* **Total time spent:** \~24 hours  
* **Spread over:** 9 days  
* **Completion:** December 2025

Work was done incrementally, with frequent refactoring as rules became clearer or flaws were discovered.

---

## **Limitations & Future Improvements**

Current limitations:

* No AI or move evaluation  
* No castling, en passant, or pawn promotion  
* No draw detection (stalemate, repetition, etc.)  
* Terminal-only interface

Possible future extensions:

* Add missing chess rules  
* Implement a basic evaluation engine  
* Separate game logic from I/O  
* Build a GUI or web interface

---

## **Note to Readers & Contributors**

This repository is shared **primarily for learning and portfolio purposes**.

* The **original source file is not intended to be modified directly**.  
* You are welcome to **fork the project**, experiment freely, refactor, extend features, or build on top of it in your own copy.  
* Pull requests that alter the core file are not expected or required.

The goal of this project is to document my learning process, design decisions, and technical growth—not to serve as a collaborative production codebase.

If this project helps you learn something, that’s a win.

---

