from processor_worker.domain import processor


def main():
    processor.consume()


if __name__ == "__main__":
    main()
