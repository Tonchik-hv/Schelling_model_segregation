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
Run 2 scripts, which will install all necessary environment and build the program.
```
git clone https://github.com/Tonchik-hv/Schelling_model_segregation.git
cd Schelling_model_segregation/
chmod +x ./prereqs.sh ./test.sh ./build.sh ./run.sh
./prereqs.sh
./build.sh
```
Test the program
```
./test.sh
```
Run the program
Define the $1 size of the map and $2 threshold as params (or leave empty for default)
```
./run.sh

./run.sh 224 0.20
```
## Working inside docker
To build the project (tests and the default run are included)
```
git clone https://github.com/Tonchik-hv/Schelling_model_segregation.git
cd Schelling_model_segregation/
docker build -t fse_project_im .
```
Run the program with the custom params
$1 - size of the map
$2 - threshold
```
docker run --rm fse_project_im ./run.sh

docker run --rm fse_project_im ./run.sh 224 0.25
```
## Development

The decription of the project structure:

- **.github/workflows** - GitHub workflow-based deployment system;
- **Example/0.625.gif** - Demonstration gif with how the algorithm works for parameter **R** = 0.625;
- **app/Makefile** - build system to compile the code;
- **app/Schelling_model.ipynb** - demonstration jupyter notebook to show how the mode;l works;
- **app/func.cpp** - the function for counting the number of neighbours;
- **app/main.py** - the main python script to start the algorithm work;
- **app/source.py** - source code for the model;
- **app/test_source.py** - unit tests for checking the critical functionality of the modules of the project.
- **Dockerfile** - Dockerfile for building the image
- **build.sh** - script to build the code;
- **prereqs.sh** - script to install required libraries;
- **run.sh** - script to run the implementation;
- **test.sh** - script to test the implementation;
