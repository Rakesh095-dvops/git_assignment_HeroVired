import os
import random

def create_random_binary_file(filename="random_data.bin", size_mb=200):
    """
    Creates a binary file filled with random data.

    Args:
        filename (str): The name of the file to create.  Defaults to "random_data.bin".
        size_mb (int): The size of the file in megabytes. Defaults to 200.
    """

    size_bytes = size_mb * 1024 * 1024  # Convert MB to bytes

    try:
        with open(filename, "wb") as f:
            for _ in range(size_bytes // 1024):  # Write in 1KB chunks to avoid memory issues
                random_data = os.urandom(1024)  # Generates 1KB of cryptographically secure random bytes
                f.write(random_data)

            # Handle the remaining bytes if size is not a multiple of 1024
            remaining_bytes = size_bytes % 1024
            if remaining_bytes > 0:
                random_data = os.urandom(remaining_bytes)
                f.write(random_data)


        print(f"Successfully created file: {filename} ({size_mb} MB)")

    except Exception as e:
        print(f"Error creating file: {e}")


if __name__ == "__main__":
    #create_random_binary_file() # Create a 200 MB file named random_data.bin

    # Example usage to create a differently named and sized file:
    create_random_binary_file(filename="my_large_file.dat", size_mb=300) # Creates a 300MB file