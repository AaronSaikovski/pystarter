"""
structured logging
"""

from typing import Any

import structlog

# ******************************************************************************** #

# Configure structlog once
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(10),
    cache_logger_on_first_use=True,
)

# ******************************************************************************** #


def get_logger(context: dict[Any, Any]):
    """Logger factory

    Args:
        context (dict[Any, Any]): _description_

    Returns:
        _type_: _description_
    """
    log = structlog.get_logger()
    if context:
        return log.bind(**context)
    return log


# ******************************************************************************** #

##Using structlog - https://www.structlog.org/en/stable/
##Usage
##
## main imports
### import get_logger as profiler
##
## main usage
## async def main():
##         context = {
##         "request_id": str(uuid.uuid4()),  # Random per execution
##     }
##     log = get_logger(context)
##      log.info("*** Starting URL processing ***")
##
## Log error
##  except Exception as e:
##       log.error("Unexpected error:", exception=str(e))
##
## Function Sample
# def process_order(order_id: int, logger):
#     logger.info("processing_started", order_id=order_id)
#     logger.info("processing_complete", order_id=order_id)
