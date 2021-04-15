import argparse
import logging
import os
import resource
import sys
import timeit

from hurry.filesize import size

# setup the logger
logging.basicConfig(
    stream=sys.stdout, level=logging.INFO, format="%(asctime)s : %(message)s"
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_dirpath",
        type=str,
        default=os.path.join(
            os.environ.get("DATA_DIRPATH", "./.data"),
        ),
    )

    args = parser.parse_args()
    logging.info(f"Args: {args}")

    start_at = timeit.default_timer()
    try:
        logging.info("Run code segment here.")

        # ...
        # ... core logic
        # ...
    except Exception as exc:
        logging.error(exc)
        raise
    finally:
        elapsed = timeit.default_timer() - start_at
        logging.info(f"Process completed in : {elapsed} seconds")

        max_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1000
        logging.info(f"Peak Process Memory Utilization: {size(max_mem)}")


if __name__ == "__main__":
    main()
