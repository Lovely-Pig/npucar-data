import os


def write_train_path(image_dir: str):
    with open('train.txt', 'a') as fp:
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                fp.write(f'data/custom/{image_dir}/{file}\n')


def write_valid_path(image_dir: str):
    with open('valid.txt', 'a') as fp:
        num = 0
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                num = num + 1
                if num == 10:
                    break
                fp.write(f'data/custom/{image_dir}/{file}\n')


if __name__ == '__main__':
    write_train_path(image_dir='images/bedroom')
    write_train_path(image_dir='images/dining')
    write_train_path(image_dir='images/living')

    write_valid_path(image_dir='images/bedroom')
    write_valid_path(image_dir='images/dining')
    write_valid_path(image_dir='images/living')
