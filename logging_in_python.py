import logging

# ================= LOGGING SETUP =================

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# format define
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# file handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# handlers add karo
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# ================= FUNCTION =================

def add(a, b):
    try:
        logger.debug("add() called with a=%s, b=%s", a, b)

        result = a + b

        logger.debug("Result calculated: %s", result)

        return result

    except Exception as e:
        logger.exception("Error occurred in add()")
        return None


# ================= RUN =================

output = add(10, 5)
print("Output:", output)
