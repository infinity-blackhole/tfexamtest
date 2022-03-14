# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tensorflow as tf


def main():
    print("Available Devices: ", tf.config.list_physical_devices('GPU'))


if __name__ == '__main__':
    main()
