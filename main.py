from helper_functions import *


def copy_images(parent_folder_func, new_subset_func, dataset, target_labels_func):
    """
    Copies `labels[target_labels]` images from `parent_folder` to
    `new_subset` (named after `dataset`) folder.

    E.g. move steak images to data/steak_subset/train/ &
    data/steak_subset/test/

    Parameters
    --------
    parent_folder (str) - original folder path with all data
    new_subset (str) - name of parent folder to copy to
    dataset (str) - which dataset? (train or test)
    labels (list) - list of training or test labels
    target_labels (list) - list of target labels to copy e.g. ["steak", "pizza"]
    """
    # Get the appropriate labels
    print(f"\nUsing {dataset} labels...")
    labels = get_labels("data/meta/meta/" + dataset + ".json")

    # Loop through target labels
    for i1 in target_labels_func:
        path = os.path.join(parent_folder_func + "/" + new_subset_func + "/" + dataset + "/", i1)
        os.umask(0)
        # Make target directory
        os.makedirs(path, exist_ok=True)

        # Go through labels and get appropriate classes
        images_moved = []  # Keep track of images moved
        for j in labels[i1]:
            # Create original image path and new path
            og_path = parent_folder_func + "data/images/" + j + ".jpg"
            new_path = parent_folder_func + "/" + new_subset_func + "/" + dataset + "/" + j + ".jpg"

            # Copy images from old path to new path
            shutil.copy2(og_path, new_path)
            images_moved.append(new_path)
        print(f"Copied {len(images_moved)} images from {dataset} dataset {i1} class...")


train_labels = get_labels("data/meta/meta/train.json")
test_labels = get_labels("data/meta/meta/test.json")

# Make binary data (pizza and steak)
# Two classes: steak and pizza.

parent_folder = "/Users/ivanmarkovski/Documents/PythonProjects/tensorflow-cert/create_dataset/"
target_labels = ["steak", "pizza"]
new_subset = "pizza_steak"
datasets = ["train", "test"]

# Copy training/test images
for i in datasets:
    copy_images(parent_folder_func=parent_folder,
                new_subset_func=new_subset,
                dataset=i,
                # labels=labels,
                target_labels_func=target_labels)


# Should be 750 for training set and 250 for test set
print("Number of images in training set:", len(os.listdir("pizza_steak/train/steak")))
print("Number of images in test set:", len(os.listdir("pizza_steak/test/steak")))

# Make sure there are no overlaps in the training and test sets
# Get two sets of filenames from train/test and make sure the output equals 0
train_files = set(os.listdir("pizza_steak/train/steak"))
test_files = set(os.listdir("pizza_steak/test/steak"))

# There should be no intersection of file names in training/test set
assert len(train_files.intersection(test_files)) == 0
# Make sure there are no overlaps in the training and test sets
# Get two sets of filenames from train/test and make sure the output equals 0
train_files = set(os.listdir("pizza_steak/train/pizza"))
test_files = set(os.listdir("pizza_steak/test/pizza"))

# There should be no intersection of file names in training/test set
assert len(train_files.intersection(test_files)) == 0
