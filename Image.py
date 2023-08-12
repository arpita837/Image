from PIL import Image
import os

class ImageRepository:
    def __init__(self, repo_folder):
        self.repo_folder = repo_folder
        if not os.path.exists(self.repo_folder):
            os.makedirs(self.repo_folder)

    def add_image(self, image_path, image_name):
        dest_path = os.path.join(self.repo_folder, image_name)
        os.rename(image_path, dest_path)
        print(f"Image '{image_name}' added to the repository.")

    def remove_image(self, image_name):
        image_path = os.path.join(self.repo_folder, image_name)
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Image '{image_name}' removed from the repository.")
        else:
            print(f"Image '{image_name}' not found in the repository.")

    def list_images(self):
        image_names = os.listdir(self.repo_folder)
        if not image_names:
            print("No images in the repository.")
        else:
            print("Images in the repository:")
            for name in image_names:
                print(name)

    def display_image(self, image_name):
        image_path = os.path.join(self.repo_folder, image_name)
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img.show()
        else:
            print(f"Image '{image_name}' not found in the repository.")

    def rotate_image(self, image_name, degrees):
        image_path = os.path.join(self.repo_folder, image_name)
        if os.path.exists(image_path):
            img = Image.open(image_path)
            rotated_img = img.rotate(degrees)
            return rotated_img
        else:
            print(f"Image '{image_name}' not found in the repository.")
            return None

    def save_image(self, img, image_name, save_folder):
        save_path = os.path.join(save_folder, image_name)
        if os.path.exists(save_folder):
            img.save(save_path)
            print(f"Transformed image saved as '{save_path}'.")
        else:
            print("Destination folder does not exist.")

def main():
    repo = ImageRepository("image_repository")

    while True:
        print("\nImage Repository Menu:")
        print("1. Add Image")
        print("2. Remove Image")
        print("3. List Images")
        print("4. Display Image")
        print("5. Rotate Image")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            image_path = input("Enter image file path: ")
            image_name = input("Enter image name: ")
            repo.add_image(image_path, image_name)

        elif choice == "2":
            image_name = input("Enter image name to remove: ")
            repo.remove_image(image_name )

        elif choice == "3":
            repo.list_images()

        elif choice == "4":
            image_name = input("Enter image name to display: ")
            repo.display_image(image_name)

        elif choice == "5":
            image_name = input("Enter image name to rotate: ")
            degrees = int(input("Enter rotation degrees: "))
            rotated_img = repo.rotate_image(image_name, degrees)

            if rotated_img:
                display_choice = input("Display rotated image? (y/n): ")
                if display_choice.lower() == "y":
                    rotated_img.show()

                save_folder = input("Enter destination folder for the transformed image: ")
                repo.save_image(rotated_img, image_name, save_folder)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
