#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

# Example usage:
fido = Dog("Fido")
print(fido.name)  # Output: Fido
print(fido.breed)  # Output: Mutt

snoopy = Dog("Snoopy", "Beagle")
print(snoopy.breed)  # Output: Beagle
