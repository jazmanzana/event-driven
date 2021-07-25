from processor_worker.domain import processor


def main() -> None:
    processor.consume()


if __name__ == "__main__":
    main()
