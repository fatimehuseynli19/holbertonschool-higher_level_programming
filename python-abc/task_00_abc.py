#!/usr/bin/env python3
"""Module that defines Animal, Dog and Cat classes."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal."""
        pass


class Dog(Animal):
    """A dog class that inherits from Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """A cat class that inherits from Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
