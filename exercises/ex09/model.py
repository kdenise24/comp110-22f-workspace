"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730566062"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, two: Point) -> float:
        """Calculates the distance between two points."""
        the_distance: float = sqrt(((self.x - two.x) ** 2) + ((two.y - self.y)**2))
        return the_distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """DOCSTRING."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()
    
    def contract_disease(self) -> None:
        """Assigns the INFECTED constant to the sickness atribute."""
        self.sickness = constants.INFECTED 

    def is_vulnerable(self) -> bool:
        """Finds if the cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Finds if the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Assigns the color to cell depending on if the cell is infected or not."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "purple"
        if self.is_immune():
            return "pink"

    def contact_with(self, other: Cell) -> None:
        """When two cells make contact, if one is already infect it will infect the other."""
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()
        if other.is_vulnerable() and self.is_infected():
            other.contract_disease()

    def immunize(self) -> None:
        """Assigns the IMMUNE constant to the sickness atribute."""
        self.sickness = constants.IMMUNE 

    def is_immune(self) -> bool:
        """Finds if the cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, sick_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if sick_cells >= cells or sick_cells <= 0:
            raise ValueError
        if immune_cells >= cells or immune_cells <= 0:
            raise ValueError
        for _ in range(immune_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            cell.immunize()
        for _ in range(sick_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            cell.contract_disease()
        for _ in range(cells - immune_cells - sick_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X 
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
        
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False

    def check_contacts(self) -> None:
        """Tests for when two cell values come in contact with eachother."""
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1