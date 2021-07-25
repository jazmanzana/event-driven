from finisher_worker.domain import finisher


def main():
    finisher.consume()


if __name__ == "__main__":
    main()
