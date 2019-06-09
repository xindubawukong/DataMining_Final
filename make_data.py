import csv
import random


def main():
    train_file = '../train.csv'
    test_file = '../test.csv'
    save_dir = '../new_data'

    with open(train_file, 'r') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        data = data[1:]
        random.shuffle(data)
        train_num = int(len(data) * 0.9)
        train_data = data[:train_num]
        dev_data = data[train_num:]
        with open(save_dir + '/new_train.csv', 'w', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerows(train_data)
        with open(save_dir + '/new_dev.csv', 'w', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerows(dev_data)

    with open(test_file, 'r') as f:
        reader = csv.reader(f)
        data = []
        for row in reader:
            data.append(row)
        data = data[1:]
        random.shuffle(data)
        with open(save_dir + '/new_test.csv', 'w', newline='') as f2:
            writer = csv.writer(f2)
            writer.writerows(data)


if __name__ == '__main__':
    main()
