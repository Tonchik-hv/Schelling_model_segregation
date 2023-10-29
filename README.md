# Schelling's model of segregation

1) Suppose there are two types of agents. Two agent types are initially placed into random locations of a neighborhood represented by a grid.
2) Now we must determine if each agent is satisfied with its current location. A satisfied agent is one that is surrounded by at least **R** percent of agents of the same type. This threshold R is one that will apply to all agents in the model.
3) When an agent is not satisfied, it can be randomly moved to any vacant location in the grid.
4) All dissatisfied agents must be moved in the same round. After the round is complete, a new round begins, and dissatisfied agents are once again moved to new locations in the grid. 

### Step-by-step algorithm:
- Randomize the map with half white and half black points (0 and 1).
- Define the value of **R** (0, 1/8, 2/8,3/8, 4/8, 5/8, 6/8, 7/8, 1), start the game.
- On each step for each cell find out if the cell wants to move - this cell is now on the market (considered free for moving in).
- After you finished with the whole map - cells that want to move can move into free cells
- Repeat the whole procedure

## Demostration of the algorithm work

Below the demonstration of how the algorithm works is presented. The threshold value **R** = 0.625:

<img src="Example/0.625.gif" width="400">

## Quickstart

## Development
