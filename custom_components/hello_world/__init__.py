import logging
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

_LOGGER = logging.getLogger(__name__)
DOMAIN = "hello_world"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Hello World from a config entry."""
    username = entry.data.get("username")
    
    _LOGGER.info(f"Hello {username}! Integration loaded via UI.")
    
    hass.states.async_set(f"{DOMAIN}.status", f"Hello {username}")
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    hass.states.async_remove(f"{DOMAIN}.status")
    return True
