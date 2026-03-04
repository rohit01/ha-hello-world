import logging

_LOGGER = logging.getLogger(__name__)

DOMAIN = "hello_world"

async def async_setup(hass, config):
    """Set up the Hello World integration."""
    _LOGGER.info("Hello World integration has been loaded!")
    
    # Create a simple state in the Developer Tools
    hass.states.async_set("hello_world.status", "Active")
    
    return True

