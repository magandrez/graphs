# graphs
A small exercise in Python with the graph abstract data type. It generates a pseudo-randomly generated graph, saves it to a relational database, calculates its [strongly connected components](http://www.wikiwand.com/en/Strongly_connected_component) and profiles each functionality.

The pseudo-random graph is generated once the program is launched and after the user inserts the desired nodes and edges, then it creates the graph thanks to the implemented Vertex and Graph classes implemented in ```graph.py```.

The program uses the number of nodes as a maximum value for the ```random.randrange``` function and as the ID of each of the nodes (i.e.: if the user inputs a graph of 3 nodes, the program will generate 3 nodes named 0, 1 and 2).

The edges are generated based on the name of the nodes and the number input by the user (i.e.: if the user inputs a grap of 3 nodes and 3 edges the program will generate 3 nodes named 0, 1 and 2 with edges like (0,1), (2,0), (2,1)).


## Features
- Randomly generates a [graph](http://www.wikiwand.com/en/Graph_%28abstract_data_type%29) based in the number of nodes and edges defined by the user as input.
- DB persistence. Save the randomly generated graph to a DB. [See TO-DO](#todo)
- Counts, calculates and prints out to terminal the strongly connected components from the generated graph. [See TO-DO](#todo)
- Profiling of each feature.

## Requirements

I have developed this using the following setup:

- Python >3.0
- [virtualenv](http://virtualenv.readthedocs.org/en/latest/). Recommended to install requirements and overall as a good practice when installing Python packages to contain environments.
- pip >1.5. As a package manager for python packages.
- [SQLAlchemy](http://sqlalchemy.org/) 1.0.4. A Python SQL toolkit I used to talk with the database.
- line-profiler 1.0

## Usage

Assuming you already have [pip](https://pip.pypa.io/en/latest/installing.html) and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) installed in your machine. Clone this repository:

```
$ git clone https://github.com/magandrez/graphs
```
Create a virtual environment in the root of the cloned repo:

```
graphs$ virtualenv graphs

```

Activate the environment:

```
graphs$ source ./graphs/bin/activate

```

Install requirements listed in ```requirements.txt```:

```
(graphs)graphs$ pip install -r requirements.txt

```

And now test it. You can run this code in two ways, one with profiling activated (using line-profiler features) or using _good'ol_ Python:

```
(graphs)graphs$ kernprof -l -v main.py

```

OR

Comment lines 10, 51 and 71 from ```main.py``` with the ```@profile``` decorators used by line-profiler and run:

```
(graphs)graphs$ python main.py

```

## Todo

- Complete/fix the functionality that saves the graph to the DB. I was not able to find a way to fill the Edges table by looping over the randomly generated graph.

- Complete/fix the algorithm to calculate strongly connected graphs. At the moment, the solution generates each of the nodes from the graph generated as a strong component (which it is obviously wrong).

## Credits

I have implemented this following this information:

- [Python documentation](https://docs.python.org/3.4/tutorial/).
- [SQLAlchemy documentation](http://docs.sqlalchemy.org/en/improve_toc/index.html).
- [Wikipedia's definition of strongly connected components](http://www.wikiwand.com/en/Strongly_connected_component) and [graph data type](http://www.wikiwand.com/en/Graph_%28abstract_data_type%29).
- [Tarjan's algorithm definition in the Wikipedia](http://www.wikiwand.com/en/Tarjan%27s_strongly_connected_components_algorithm).
- [Python recipe implementing Tarjan's algorithm](http://code.activestate.com/recipes/578507-strongly-connected-components-of-a-directed-graph/) to calculate strongly connected components.
- [Graphs chapter from python-course.eu](http://www.python-course.eu/graphs_python.php).
- [Stackoverflow](http://stackoverflow.com/).
