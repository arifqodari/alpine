import logging


from alpine.settings import general_settings


def create_logger(name):
    logger = logging.getLogger(name)
    if general_settings.is_debug:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO
    logger.setLevel(log_level)

    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        handler.setLevel(log_level)

        formatter = logging.Formatter(
            fmt="%(asctime)s [%(process)d] [%(levelname)s] [%(name)s] %(message)s",
            datefmt="[%Y-%m-%d %H:%M:%S %z]"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
    return logger


# setup package-level
_ = create_logger(__package__.split(".")[0])


if __name__ == "__main__":
    logger = create_logger(__name__)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")